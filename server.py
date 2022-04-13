#!/usr/bin/env pybricks-micropython
import sys
import socket
import re
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port as Evport

ev3 = EV3Brick()
motora = Motor(Evport.A)
motorc = Motor(Evport.C)

try:
    ev3.speaker.beep(500, 2000)
except Exception as e:
    #print(e)
    pass

#PORT = int(input('Port: '))
PORT = 57182
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("192.168.44.28", PORT))
s.listen(5)


running = True
while running:
    clientsocket, adress = s.accept()
    if clientsocket:
        #msg = input("What do you wish to send?: ")
        pass
    
    #clientsocket.send(bytes(f"{msg}", "utf-8"))

    fullevent1 = ''
    fullevent2 = ''
    event = []
    is_event1_full = False
    do = ''

    running_event = ''
    direction = 'forward'

    def stop():
        motora.stop()
        motorc.stop()
    

    while clientsocket:
        clientres = clientsocket.recv(1024)
        if clientres.decode('utf-8') != '':
            #fullevent1 += clientres.decode('utf-8')
            event.append(clientres.decode('utf-8'))
            if clientres.decode('utf-8').find('\n') > -1:
                fullevent1 += clientres.decode('utf-8')
                is_event1_full = True
            fullevent1 += clientres.decode('utf-8').split('\n')[0]
            if is_event1_full:
                is_event1_full = False
                event.append(fullevent1)
                fullevent1 = ''
                fullevent1 += clientres.decode('utf-8').split('\n')[1]
            #print(fullevent1)
            #print(str(event[-1]).split('\n')[0])
            do = str(event[-1]).split('\n')[0]
        else:
            clientsocket = None

        if do == 'MAB1':
            direction = 'forward'
            if running_event == do:
                #print('stopping')
                running_event = ''
                stop()
            else:
                running_event = do
                motora.run(-1000)
                motorc.run(-1000)
                #print('Moving forward')

        elif do == 'MA1':
            if running_event == do:
                #print('stopping')
                running_event = ''
                stop()
            else:
                running_event = do
                if direction == 'forward':
                    motora.run(-1000)
                    motorc.run(-250)
                    #print('MA_speed = 750; MB_speed = 1000')
                else:
                    motora.run(1000)
                    motorc.run(250)
                    #print('MA_speed = -750; MB_speed = -1000')

        elif do == 'MB1':
            if running_event == do:
                #print('stopping')
                running_event = ''
                stop()
            else:
                running_event = do
                if direction == 'forward':
                    motorc.run(-1000)
                    motora.run(-250)
                    #print('MB_speed = 750; MA_speed = 1000')
                else:
                    motorc.run(1000)
                    motora.run(250)
                    #print('MB_speed = -750; MA_speed = -1000')

        elif do == 'MAB-1':
            direction = 'backwards'
            if running_event == do:
                #print('stopping')
                running_event = ''
                stop()
            else:
                running_event = do
                motora.run(1000)
                motorc.run(1000)
                #print('Moving backwards')

        elif do == 'scream':
            try:
                ev3.speaker.beep(500, 4000)
            except Exception as e:
                pass
                #print(e)
            #print('scream')



        
#s.close()
