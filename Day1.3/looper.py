# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:57:06 2019

@author: J. Tyler McGoffin
"""

import time

class Loops:
    
    def __init__(self):
        self.timesCalled = 0

    def start(self):
        print("This firewall can be surpassed by brute force. To do so, you must call the following function 1001 times:\n\nhack()\n\nHowever, you must figure out the proper syntax for calling this function. Good Luck!")
        
    def hack(self):
        self.timesCalled += 1
        
        if self.timesCalled == 1:
            print("Congratulations! You've successfully hacked once. Now you need to hack 1000 more times...\n")
            time.sleep(1.000)
        elif self.timesCalled == 100:
            print("That's 100 hacks... 10% complete\n")
        elif self.timesCalled % 100 == 0 and self.timesCalled != 1000:
            print(str(self.timesCalled/1000*100)+"% complete...")
            time.sleep(1.000)
        elif self.timesCalled == 1000:
            print("Task completed. The next characer: 5")
        elif self.timesCalled > 1000:
            print("For your next task, run heist.numberPatch.start()")
        time.sleep(.025)