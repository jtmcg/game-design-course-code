# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:28:44 2019

@author: J. Tyler McGoffin
"""

import time, numpy
    
class FuseBypass:
    
    def __init__(self):
        self.blownFuses = 0
        self.numberOfAttempts = 0
        self.targetFuse = self.randomFuse()
    
    def start(self):
        print("To unlock the next character in the password, we'll need to bypass a fuse in the computer system.")
        time.sleep(3.000)
        print("The fuses are numbered 0-999. To test a fuse, you must enter which fuse to test in the parenthesis of heist.fuseBypass.test() and run.")
        time.sleep(3.000)
        print("If you test a fuse higher than the target, the fuse will blow and the test will return False. If you test a fuse lower than the target, the test will return True")
        time.sleep(3.000)
        print("You only get 2 blown fuses before you have to commit to the bypass.")
        time.sleep(3.000)
        print("\nTo bypass the target, run heist.fuseBypass.bypass()")
        time.sleep(3.000)
        print("If you guess wrong, the system will reset, and the bypass fuse will change.")
        time.sleep(2.000)
        print("\nUse what you know of python to write some code to help you test as many fuses as possible quickly. If you take too many attempts, \nthe code will tell you whether or not you got the right fuse, but will make you try again to guess faster")
        time.sleep(6.000)
        print("Good Luck!\n")
    
    def test(self, fuse):
        
        if self.blownFuses >= 2:
            print("That's 2 blown fuses. You have to commit to the bypass now. Run heist.fuseBypass.bypass()")
            return
        
        if not isinstance(fuse, int):
            print("The fuse number must be an integer")
            return
        
        self.numberOfAttempts += 1
        
        if fuse > self.targetFuse:
            print("You blew fuse "+str(fuse)+"\n")
            self.numberOfAttempts -= 1
            return False
        else:
            print("Nothing happened at "+str(fuse)+".\n")
            return True
    
        if self.numberOfAttempts <= 0:
            print("You are out of fuses! You must commit to the bypass by running heist.fuseBypass.bypass()")
        elif self.blownFuses == 1:
            print("You have 1 fuse remaining...")
        
    def randomFuse(self):
        return numpy.random.randint(1000)
        
    def reset(self):
        self.numberOfAttempts = 0
        self.blownFuses = 0
        self.targetFuse = self.randomFuse()
        
    def bypass(self):
        guess = input("Input the target fuse: ")
        
        try:
            guess = int(guess)
        except:
            print("The target fuse must be an integer!")
        else:
            if guess == self.targetFuse and self.numberOfAttempts <= (self.targetFuse//2 + 1):
                print("Correct fuse bypass detected....\n")
                time.sleep(5.000)
                print("Authorization verified. Bypassing...\n")
                time.sleep(4.000)
                print("The next character is 7")
                time.sleep(4.000)
                print("Now, you must unscramble the characters to find the passcode. Enter the password into the parenthesis in heist.access(). If you guess the password correctly, it will return 'True', otherwise it will return 'False'.")
                print("You may have to write some code to guess the correct combination")             
            elif guess != self.targetFuse:
                print("Unauthorized access detected. Fuse bypass incorrect. Reseting system...")
                time.sleep(2.000)
                self.reset()
            else:
                print("Correct fuse bypass detected....\n")
                time.sleep(5.000)
                print("Unauthorized user suspected. Number of attempts too high. Reseting system...\n (Try again, but with fewer trials)")
                time.sleep(2.000)
                self.reset()
            
    def cheat(self):
        print(self.targetFuse)