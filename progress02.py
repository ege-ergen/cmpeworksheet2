
"""
    Stage: Development-01
    @author:Ege Ergen 120202011
    @author:Cem Cereb 119202062
    @author:Wafaa Al Bacha 121202106

"""

import tkinter as Supermarket

import tk as tk


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = Supermarket.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()


    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.
        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """
    def _initializeGUI(self):
        self.lbl01 = Supermarket.Label(text="username")
        self.lbl02 = Supermarket.Label(text="password")

        self.txt01 = Supermarket.Entry()
        self.txt02 = Supermarket.Entry()

        self.btn01 = Supermarket.Button(text="login")
        self.btn02 = Supermarket.Button(text="register")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-1>", self.handle_click)


    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """
    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)


    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.
        :param event: action event for detecting which button is clicked
    """
    def handle_click(self, event):
        self.txt01.get()
        self.txt02.get()
        if self.txt01 != ("admin")  & self.txt02 != (123):
            def __init__(self):
                self.window = Supermarket.Tk()
        return


# main method for testing the application
if __name__ == "__main__":
    LoginWindow()



"""
    Stage: Development-02
    @author: Omar Al-Shareef , 119200019
    @author: Hüseyin Enes Tandoğan , 119200040
"""

# Python program to create a table

from tkinter import *
import tkinter as tk


class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='yellow', font=('Arial', 18, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = [(1, 'Rice', 'Available'),
       (2, 'Egg', 'Available'),
       (3, 'Milk', 'Available'),
       (4, 'Water', 'Not Available!!!'),
       (5, 'Pepsi', 'Not Available!!!')]


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

def check_availability():
  items = ['Rice', 'Egg', 'Milk', 'Water', 'Pepsi']
  available_items = ['Rice', 'Egg','Milk']

  for item in items:
    if item in available_items:
      print(f'{item} is available in the Supermarket')
    else:
      print(f'{item} is not available in the Supermarket')

# Create a button widget and place it in the main window
button = tk.Button(text='Search', command=check_availability)
button.pack(side = BOTTOM, padx=70, pady=70)
#button1.pack(side = BOTTOM, padx=<x_coordinate, pady=<y_coordinate>)


# create root window
root = Tk()
root.title('Supermarket Item List')
t = Table(root)
root.mainloop()

