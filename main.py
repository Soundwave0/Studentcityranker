import tkinter as tk
import pandas as pd
def calculate():
    pass

def runapp():
    window = tk.Tk()
    window.geometry("600x900")


    window.title("Welcome to application")
    # add labels before input fields
    welcomelabel =tk.Label(window)
    welcomelabel.config(text="Welcome! please enter the various fields and press calculate")

    citylabel = tk.Label(window)
    citylabel.config(text="enter city: ")

    oceanlabel = tk.Label(window)
    oceanlabel.config(text="enter ocean dist factor: ")

    mountainlabel = tk.Label(window)
    mountainlabel.config(text="enter mountain dist factor: ")

    costlabel = tk.Label(window)
    costlabel.config(text="enter cheapness: ")

    educationlabel = tk.Label(window)
    educationlabel.config(text="enter education quality: ")

    sociallabel = tk.Label(window) #night life, clubs, nature of people
    sociallabel.config(text="enter social life: ")

    joblabel = tk.Label(window)
    joblabel.config(text="enter ease of finding part time job: ")

    transitionlabel = tk.Label(window)
    transitionlabel.config(text="enter ease of transition: ")





    calculate = tk.Button(window)
    calculate.config(text="calculate",command = calculate)











    window.mainloop()


if __name__ == '__main__':
    runapp()



