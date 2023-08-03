from tkinter import *
import os


def shutdown():
    os.system("shutdown /s /t 1")


w = Tk()
btn = Button(w,
             text="Shut Down Your Computer",
             font=("Times", 40, "bold"),
             command=shutdown
             )
btn.pack()


w.mainloop()
