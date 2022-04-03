
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x970")
root.title("Calculator By CodeWithHarry")
#root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=15, pady=10, padx=15)
frame=Frame(root,bg="grey")
b1 = Button(frame , text="C", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="red")
b1.grid(row=0,column=0)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="/", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="green")
b1.grid(row=0,column=1)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="*", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="green")
b1.grid(row=0,column=2)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="-", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="green")
b1.grid(row=0,column=3)
b1.bind('<Button-1>', click)

b1 = Button(frame , text="7", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=1,column=0)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="8", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=1,column=1)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="9", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=1,column=2)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="+", padx=30, pady=28, font="lucida 35 bold", width=3,height=3,activebackground="green")
b1.grid(row=1,column=3,rowspan=2)
b1.bind('<Button-1>', click)

b1 = Button(frame , text="4", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=2,column=0)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="5", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=2,column=1)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="6", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=2,column=2)
b1.bind('<Button-1>', click)

b1 = Button(frame , text="1", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=3,column=2)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="2", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=3,column=0)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="3", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=3,column=1)
b1.bind('<Button-1>', click)
b1 = Button(frame , text="=", padx=30, pady=28, font="lucida 35 bold", width=3,height=3,activebackground="red")
b1.grid(row=3,column=3,rowspan=2)
b1.bind('<Button-1>', click)

b1 = Button(frame , text="0", padx=108, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=4,column=0,columnspan=2)
b1.bind('<Button-1>', click)
b1 = Button(frame , text=".", padx=30, pady=18, font="lucida 35 bold", width=3,activebackground="skyblue")
b1.grid(row=4,column=2)
b1.bind('<Button-1>', click)

frame.pack()
root.mainloop()