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
