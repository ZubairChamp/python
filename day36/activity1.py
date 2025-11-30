from tkinter import *
window=Tk()
window.title("event handler")
window.geometry("100x100")
def handlekeypress(event):
    print(event.char)
window.bind("<Key>",handlekeypress)
def handleclick(event):
    print("\n the button was clicked")
button=Button(text="click me!")
button.pack()
button.bind("<Button-1>",handleclick)
window.mainloop()