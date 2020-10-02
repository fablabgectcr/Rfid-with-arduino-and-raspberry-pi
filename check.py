#!/usr/bin/env python

import serial
import subprocess as sp
import time


ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600

#dictionary with rfid number and bed number
dict_rfid = {}  
active_bed = () # fetched from main server
left_turn = () 
extProc = sp.Popen(['python','motion.py']) # motion func running init util cond met

motion_var = 0
#mainly two variables declares turn_var and motion_var-dependent variable


while True:
    read_ser=ser.readline()
    print(read_ser)
    turn_var = 0
    
    #refer to Active beds list

    if (motion_var == 1):
        extProc2 = sp.Popen(['python','motion.py'])
        

    if (read_ser == read_ser):
        time.sleep(2)
        bed = dict_rfid.get("A")
        if bed in active_bed:

            print("opening interaction")
            if bed in left_turn:
                turn_var = 1
                left_turn = sp.Popen(['python', 'interact_left.py'])
            else:
                right_turn = sp.Popen(['python', 'interact_right.py'])
            
            time.sleep(5)

            while True: # i need some conditions to trigger this
                if (user_control == 1 ): #some condition user disturb
                    if (turn_var == 1):
                        right_turn2 = sp.Popen(['python', 'interact_right.py'])
                    else:
                        left_turn2 = sp.Popen(['python', 'interact_left.py'])
                    
                    break
                    
                else:
                    continue


                        
                
        else:
            motion_var = 1
            continue
    else:
        motion_var = 0
        continue    

                

        
        

        
        
        
        
        
        
