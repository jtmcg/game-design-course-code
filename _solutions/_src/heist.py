# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:47:57 2019

@author: J. Tyler McGoffin
"""

# Scavenger Hunt
import time
import _src.looper as looper
import _src.scale as scale
import _src.fusebypass as fusebypass
import webbrowser

loops = looper.Loops()
numberPatch = scale.Scales()
fuseBypass = fusebypass.FuseBypass()

def start():
    print("\nWelcome to the Heist!! You are attempting to hack into a vault containing a powerful secret...")
    print("You will be given a series of tasks to complete using the coding principles we've gone over in class.")
    time.sleep(5.000)
    print("\nSuccessful completion of each task will yield a character of the vault's access key. They are not given in order.")
    time.sleep(5.000)
    print("Once you have collected all 4 characters, you must find the correct order of them to access the vault and complete the hack.")
    time.sleep(5.000)
    print("\nFor initializing the first system, you will be rewarded a character.")
    time.sleep(5.000)
    print(".\n")
    time.sleep(2.000)
    print(".\n")
    time.sleep(2.000)
    print(".\n")
    time.sleep(2.000)
    print("The first character is &\n")
    time.sleep(10.000)
    print("To access the next task, enter the following command: heist.loops.start()")
    
def access(password):
    if password == "Y7&5":
        print("Hacking attempt detected... Password is key plus 4 more characters: GL8T... These are not in order. Try again with all 8 characters...")
        return True
    elif password == "G78T&5LY":
        print("Password authentication complete...")
        time.sleep(4.000)
        print("Retrieving data...")
        time.sleep(2.000)
        print(".\n")
        time.sleep(2.000)
        print(".\n")
        time.sleep(2.000)
        print(".\n")
        
        unlock()
        return True
    else:
        #print("Invalid Key Entry")
        return False

def unlock():
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ?t=42")
    print("\nCongratulations! You've successfully unlocked the vault. Don't spoil the Rickroll for anyone else ;)")
