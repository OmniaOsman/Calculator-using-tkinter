from tkinter import *

root = Tk()
global variable, operator, expression, answer


class Calculator:

    def click(self, numbers):
        """ This Function continuously updates the
            input field whenever you enters a number """
        global expression
        self.expression += str(numbers)
        self.variable.set(self.expression)

    def clear(self):
        """ This method clears the input field """
        self.expression = ''
        self.variable.set('')

    def evaluate(self):
        """ This method calculates the expression
            present in input field"""
        self.answer = str(eval(self.expression))
        self.variable.set(self.answer)
        # self.expression = ''
        # self.operator = str(self.answer)

    def __init__(self, master):
        root.title('Calculator')  # set a title of window
        root.geometry('302x417')  # set a size for window
        root.resizable(0, 0)  # can't change the size of window
        icon = PhotoImage(file='calculator.png')
        root.iconphoto(False, icon)

        # Gets the requested values of the height and width.
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()

        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

        # Positions the window in the center of the page.
        root.geometry("+{}-150".format(positionRight, positionDown))

        self.operator = ''
        self.expression = ''
        self.answer = ''
        self.variable = StringVar()

        # screen
        frameScreen = Frame(master, height=50, width=300)
        frameScreen.pack(side=TOP, fill=BOTH, expand=False)

        self.entry = Entry(frameScreen, textvariable=self.variable, bg='light gray', width=300, font=('roboto', 16),
                           fg='black', justify=RIGHT)

        self.entry.grid(row=0, column=0)
        self.entry.place(height=50, width=300)

        # Buttons
        buttonFrame = Frame(root, width=300, height=200, bg='gray')
        buttonFrame.pack()

        # Row 1{clear and divide}
        clear = Button(buttonFrame, text='Clear', bg='black', width=30, cursor="hand2", height=4, font=('roboto', 10),
                       fg='white', command=lambda: self.clear()).grid(row=0, column=0, columnspan=3)

        divide = Button(buttonFrame, text='/', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                        cursor="hand2", command=lambda: self.click('/')).grid(row=0, column=3, pady=2)

        # Row 2{7, 8 , 9, *}
        seven = Button(buttonFrame, text='7', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                       cursor="hand2", command=lambda: self.click(7)).grid(row=1, column=0, padx=1, pady=1)

        eight = Button(buttonFrame, text='8', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                       cursor="hand2", command=lambda: self.click(8)).grid(row=1, column=1, padx=1, pady=1)

        nine = Button(buttonFrame, text='9', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                      cursor="hand2", command=lambda: self.click(9)).grid(row=1, column=2, padx=1, pady=1)

        mul = Button(buttonFrame, text='*', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click('*')).grid(row=1, column=3, padx=1, pady=1)

        # Row 3{4, 5, 6, +}
        four = Button(buttonFrame, text='4', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                      cursor="hand2", command=lambda: self.click(4)).grid(row=2, column=0, padx=1, pady=1)

        five = Button(buttonFrame, text='5', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                      cursor="hand2", command=lambda: self.click(5)).grid(row=2, column=1, padx=1, pady=1)

        six = Button(buttonFrame, text='6', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click(6)).grid(row=2, column=2, padx=1, pady=1)

        add = Button(buttonFrame, text='+', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click('+')).grid(row=2, column=3, padx=1, pady=1)

        # Row 4{1, 2 , 3, -}
        one = Button(buttonFrame, text='1', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click(1)).grid(row=3, column=0, padx=1, pady=1)

        two = Button(buttonFrame, text='2', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click(2)).grid(row=3, column=1, padx=1, pady=1)

        Button(buttonFrame, text='3', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                       cursor="hand2", command=lambda: self.click(3)).grid(row=3, column=2, padx=1, pady=1)

        minus = Button(buttonFrame, text='-', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                       cursor="hand2", command=lambda: self.click('-')).grid(row=3, column=3, padx=1, pady=1)

        # Row 5{0, ., =}
        zero = Button(buttonFrame, text='0', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                      cursor="hand2", command=lambda: self.click(0)).grid(row=4, column=0, padx=1, pady=1)

        dot = Button(buttonFrame, text='.', bg='black', width=9, height=4, fg='white', font=('roboto', 10),
                     cursor="hand2", command=lambda: self.click('.')).grid(row=4, column=1, padx=1, pady=1)

        equal = Button(buttonFrame, text='=', bg='black', width=20, height=4, fg='white', font=('roboto', 10),
                       cursor="hand2", command=lambda: self.evaluate()).grid(row=4, column=2, padx=1, pady=1,
                                                                             columnspan=2)

        root.mainloop()


cal = Calculator(root)
