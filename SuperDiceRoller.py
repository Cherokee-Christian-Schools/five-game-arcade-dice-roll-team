# Test
from tkinter import *
import dice


class DiceRoll(Frame):
    """Dice rolling simulation program."""

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Dice Rolling Simulator")


        # Set up buttons

        # Button 1 --> Maps to 'result'
        self.button1d6 = Button(self, text="Die 1", command=self.pressed1d6)
        self.button1d6.grid(row=0, column=1)

        # Button 2 --> Maps to 'result2'
        self.button1d6_2 = Button(self, text="Die 2", command=self.pressed1d6_2)
        self.button1d6_2.grid(row=1, column=1)

        # Button 3 --> Maps to 'result' and 'result2'
        self.buttonBoth = Button(self, text="Roll Both", command=self.pressedBoth)
        self.buttonBoth.grid(row=2, column=2)

        # Initialize the results for die 1
        self.result = StringVar()
        self.resultLine = Label(self, textvariable=self.result)
        self.result.set("Click to roll")
        self.resultLine.grid(row=0, column=2)

        # Initialize the results for die 2
        self.result2 = StringVar()
        self.resultLine2 = Label(self, textvariable=self.result2)
        self.result2.set("Click to roll")
        self.resultLine2.grid(row=1, column=2)

    ####
    def pressed1d6(self):
        #Roll the first die
        self.result.set(dice.roll('1d6'))

    def pressed1d6_2(self):
        # Roll the second die
        self.result2.set(dice.roll('1d6'))

    def pressedBoth(self):
        # Roll both dice. Update both result sets
        self.result.set(dice.roll('1d6'))
        self.result2.set(dice.roll('1d6'))


def main():
    DiceRoll().mainloop()


if __name__ == "__main__":
    main()
#from tkinter import *
#import dice
#
#class DiceRoll(Frame):
#    """Dice rolling simulation program."""
#    
#    def __init__(self):
#
#        Frame.__init__(self)
#        self.pack(expand = YES, fill = BOTH)
#        self.master.title("Dice Rolling Simulator")
##### 
#        self.button1d6 = Button(self, text = "1d6", command = self.pressed1d6)
#        self.button1d6.grid(row = 0, column = 1)
#        
#        self.button1d6_2 = Button(self, text = "1d6", command = self.pressed1d6_2)
#        self.button1d6_2.grid(row = 1, column = 1)
#        
#        self.button2d6 = Button(self, text = "2d6", command = self.pressed1d6 and self.pressed1d6_2) #and? what to put to command both
#        self.button2d6.grid(row = 2, column = 1)
#
#        self.result = StringVar()
#        self.resultLine = Label(self, textvariable = self.result)
#        self.result.set("Click to roll die")
#        self.resultLine.grid(row = 0, column = 2)
#####
#        self.result2 = StringVar()
#        self.resultLine2 = Label(self, textvariable = self.result2)
#        self.result2.set("Click to roll dice")
#        self.resultLine2.grid(row = 1, column = 2)
#        
##        self.result3 = StringVar()
##        self.resultLine3 = Label(self, textvariable = self.result)
##        self.result3.set("Click to roll dice")
##        self.resultLine3.grid(row = 2, column = 2)
#####
#    def pressed1d6(self):
#        """Roll one 6-sided die."""
#        
#        self.result.set(dice.roll('1d6'))
#        
#    def pressed1d6_2(self):
#        """Roll one 6-sided die."""
#        
#        self.result2.set(dice.roll('1d6'))
#        
##    def pressed2d6(self):
##        """Roll the both 6-sided dice."""
##        
##        self.result3.set(dice.roll('2d6'))
#        
#def main():
#    DiceRoll().mainloop()
#    
#if __name__ == "__main__":
#    main()
#    
##########################
#
##import random
##min = 1
##max = 6
## 
##roll_next = "yes"
## 
##while roll_next == "yes" or roll_next == "y":
##    print("Rolling the dice...")
##    print("The two values are....")
##    print(random.randint(min, max))
##    print(random.randint(min, max))
## 
##    roll_next = input("Roll the dice again? If so, type 'yes':")
#
########################
#from tkinter import *
#import dice
#
#class DiceRoll(Frame):
#    """Dice rolling simulation program."""
#    
#    def __init__(self):
#
#        Frame.__init__(self)
#        self.pack(expand = YES, fill = BOTH)
#        self.master.title("Dice Rolling Simulator")
##### 
#        self.button1d6 = Button(self, text = "1d6", command = self.pressed1d6)
#        self.button1d6.grid(row = 0, column = 1)
#        
#        self.button1d6_2 = Button(self, text = "1d6", command = self.pressed1d6_2)
#        self.button1d6_2.grid(row = 1, column = 1)
#        
#        self.button2d6 = Button(self, text = "2d6", command = self.pressed1d6 and self.pressed1d6_2) #and? what to put to command both
#        self.button2d6.grid(row = 2, column = 1)
#
#        self.result = StringVar()
#        self.resultLine = Label(self, textvariable = self.result)
#        self.result.set("Click to roll die")
#        self.resultLine.grid(row = 0, column = 2)
#####
#        self.result2 = StringVar()
#        self.resultLine2 = Label(self, textvariable = self.result2)
#        self.result2.set("Click to roll dice")
#        self.resultLine2.grid(row = 1, column = 2)
#        
##        self.result3 = StringVar()
##        self.resultLine3 = Label(self, textvariable = self.result)
##        self.result3.set("Click to roll dice")
##        self.resultLine3.grid(row = 2, column = 2)
#####
#    def pressed1d6(self):
#        """Roll one 6-sided die."""
#        
#        self.result.set(dice.roll('1d6'))
#        
#    def pressed1d6_2(self):
#        """Roll one 6-sided die."""
#        
#        self.result2.set(dice.roll('1d6'))
#        
##    def pressed2d6(self):
##        """Roll the both 6-sided dice."""
##        
##        self.result3.set(dice.roll('2d6'))
#        
#def main():
#    DiceRoll().mainloop()
#    
#if __name__ == "__main__":
#    main()