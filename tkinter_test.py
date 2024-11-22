from tkinter import Canvas, Tk
import tkinter
print("Tkinter version:", tkinter.TkVersion)
print("Tcl version:", tkinter.TclVersion)

gui = Tk()
gui.title("Test Canvas")
canvas = Canvas(gui, width=500, height=300, background="white")
canvas.pack()

canvas.create_text(250, 150, text="Hello, Canvas!", fill="blue", font=("Arial", 20))
gui.mainloop()