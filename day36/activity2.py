from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
def message():
    messagebox.showwarning("Alert!","stop virus found!")
button=Button(window,text="scan for virus",command=message)
button.place(x=40,y=80)
window.mainloop()