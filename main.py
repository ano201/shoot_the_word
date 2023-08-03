# Import required modules
from tkinter import *
import sys
from Classes import Objects
from Functions import center_window, newWave, shoot
from wonderwords import RandomWord

# Add necessary paths to the system
sys.path.append("/Functions/")
sys.path.append("/Classes/")

# Import required classes and functions from modules
Objects = Objects.Objects
center_window = center_window.center_window
newWave = newWave.newWave
shoot = shoot.shoot


def start():
    # List of texts for objects
    # textList = ['run', 'jump', 'swim', 'go', 'write']
    rw = RandomWord()
    textList = rw.random_words(5)

    # Start a new wave of objects
    newWave(canvas, main, Objects, textList, objectList)


# Create the main window
window = Tk()
window.title("Shoot")

# Create the canvas
canvas = Canvas(window, width=500, height=650, bg="black")
canvas.pack()

window.update()

# Center the window on the screen
center_window(window, canvas)

# Create the main object
main = canvas.create_oval(
    0, 0, 15, 15,
    fill="purple"
)
canvas.move(
    main,
    (canvas.winfo_width() // 2) - 7,
    (canvas.winfo_height() - 25)
)

# Create a line at the bottom of the canvas
line = canvas.create_line(
    0,
    canvas.winfo_height() - 25,
    canvas.winfo_width(),
    canvas.winfo_height() - 25,
    width=2,
    fill="coral"
)

# Create an empty list to store objects
objectList = []

start()

# Bind the shoot function to the key event
foundObject = []
tag = []

window.bind("<Key>", lambda event:
            shoot(event, start, canvas, objectList, foundObject, tag))

# Start the main event loop
window.mainloop()
