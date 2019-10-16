# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:30:10 2019

@author: J. Tyler McGoffin
"""

import time, numpy

class Scales:
    
    def __init__(self):
        None
        
    def start(self):
        print("This task is a bit more tricky... We have 8 numbers in a list that should all be the same, but one of them is bigger than the others.") 
        time.sleep(4.000)
        print("You must determine which of these numbers is the biggest, and you can only do so by comparing the sums of other numbers a maximium of 2 times before the system resets.")
        time.sleep(4.000)
        print("If you select the wrong number, the system will lock you out for 1 minute before reseting to try again.")
        time.sleep(6.000)
        print("To compare sums, you must enter the indices of the numbers in the list you wish to add for the first sum, then again for the second. You may add any number of the numbers together.\n")
        time.sleep(6.000)
        
        while(True):
            numbers = [1,1,1,1,1,1,1,1]
            bigNumber = numpy.random.randint(0,8)
            numbers[bigNumber] = 2
            
            results = self.compareNumbers(numbers, bigNumber)
            
            if results == 'restart':
                continue
            elif results == 'winner':
                print("\nRepairing list....")
                time.sleep(2.000)
                print("Repair successful, access granted...")
                time.sleep(2.000)
                print("The next character is Y")
                print("To begin the next challenge, input heist.fuseBypass.start()")
                return
            elif results == 'wrong':
                print("Sorry, you guessed incorrectly. Now you must wait one minute before trying again.")
                time.sleep(60.000)
            
    def compareNumbers(self, numbers, bigNumber):
        
        numberOfCompares = 0
        
        while(True):
            
            sumOne, sumTwo = 0, 0
            
            print("\nThe Indices: [0, 1, 2, 3, 4, 5, 6, 7]")
            print("Input your two sets (lists) of number indices to be weighed, one at a time. They should look like this - XXXX - and may be up to 8 long. The X's represent the indices of the number in the list of numbers.")
            firstSet = input("First set of numbers to add: ")
            
            try:
                firstSet = list(firstSet)
                for num in firstSet:
                    sumOne += numbers[int(num)]
            except:
                print("You input the first set of number indices incorrectly. The input should look like this - XXXX - and of any length up to 8")
            else:
                secondSet = input("Second set of numbers to add: ")
                try:
                    secondSet = list(secondSet)
                    for num in secondSet:
                        sumTwo += numbers[int(num)]
                except:
                    print("You input the second set of number indices incorrectly. The input should look like this - XXXX - and of any length up to 8")
                else:
                    numberOfCompares += 1
                        
                    if sumOne > sumTwo:
                        print("The first set of numbers, "+str(firstSet)+" has a larger sum than the second set of numbers, "+str(secondSet))
                    elif sumOne == sumTwo:
                        print("The two sets, "+str(firstSet)+" and "+str(secondSet)+" are of equal sum")
                    else:
                        print("The first set of numbers, "+str(firstSet)+" has a smaller sum than the second set of numbers, "+str(secondSet))
                finally:
                    time.sleep(5.000)
                    if numberOfCompares == 2:
                        guess = input("Enter your answer for the index of the one larger number.\nIf you would like to skip your guess and try again, enter anything but a number\n")
                        try:
                            guess = int(guess)
                            if guess == bigNumber:
                                return 'winner'
                            else:
                                return 'wrong'
                        except:
                            return 'restart'