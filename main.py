#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by HYOUG

from pynput.mouse import Button, Controller
from random import randint, random
from time import sleep, strftime

mouse = Controller()                                                                                    # declare the controller object

claim_button = {"xmin": 390,                                                                            # claim button dimensions
                "xmax": 570,                                                                            # //
                "ymin": 415,                                                                            # //
                "ymax": 455}                                                                            # //

close_button = {"xmin": 942,                                                                            # close button dimensions
                "xmax": 952,                                                                            # //
                "ymin": 158,                                                                            # //
                "ymax": 168}                                                                            # //

cycle_time = 1800                                                                                       # free spin cooldown
cycle_randomizer = 200                                                                                  # free spin cooldown randomizer
wait_time = 8                                                                                           # spin animation cooldown
wait_randomizer = 2                                                                                     # spin animation cooldown randomizer

claim_num = 1                                                                                           # free spin claim number

print("[!] Epics.gg Auto-Clicker is now running !")                                                     # UI infos
print("[i] The program will start in 5 seconds")                                                        # //
print("[i] Press Ctrl + C to exit the script")                                                          # //

sleep(5)                                                                                                # start delay 

def random_move(object_zone) -> None:                                                                   # reproduce a human-like mouse movement
    """Reproduce a human-like mouse movement"""
    x_target = randint(object_zone["xmin"], object_zone["xmax"])                                        # define a random x target in the given zone
    y_target = randint(object_zone["ymin"], object_zone["ymax"])                                        # define a random y target in the given zone
    (posX, posY) = mouse.position                                                                       # get the current mouse position
    
    x_gap = (x_target - posX) / 1000                                                                    # define the x gap of every step of the movement
    y_gap = (y_target - posY) / 1000                                                                    # define the y gap of every step of the movement
    
    for i in range(1000):                                                                               # repeat the x and y gap 1000 times
        mouse.position = (posX + x_gap * (i + 1), posY + y_gap * (i + 1))                               # make the step from the x and y gap
        
        
def random_click() -> None:                                                                             # reporduce a human-like click
    """Reporduce a human like click"""
    mouse.press(Button.left)                                                                            # press the mouse's left button
    sleep(random())                                                                                     # wait between 0 and 1 second
    mouse.release(Button.left)                                                                          # release the mouse's left button

        
    
if __name__ == "__main__":
    while True:                                                                                         # infinite loop
        random_move(claim_button)                                                                       # move to the 'free spin' button
        random_click()                                                                                  # click
        sleep(wait_time + wait_randomizer * random())                                                   # wait the spin to end
        random_move(close_button)                                                                       # move to the 'x' button
        random_click()                                                                                  # click
        
        print(strftime(f"[V] Free spin n°{claim_num} claimed at : %H:%M:%S"))                           # print a log message
        claim_num += 1                                                                                  # increment the next free spin number
        
        sleep(cycle_time + cycle_randomizer * random())                                                 # wait the next free spin to be avaible
        
        

"""
#TODO
- pattern recognition
- more randomization
- requirments.txt
- .cfg file (?)
- librarization (?)
- command line arguments (?)
"""