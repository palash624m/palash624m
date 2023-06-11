from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("DIGITAL CLOCK")

def clock():
    Time_str = strftime('%I:%M:%S %p')
    Time.config(text=Time_str)

    date_str=strftime("%B %d, %Y")
    Date.config(text=date_str)
    
    day_str=strftime("%A")
    Day.config(text=day_str)
    
    Time.after(1000,clock)
    
Day = Label(root,font=("ds-digital",40),background="blue",foreground="lime")
Day.pack(anchor="center")

Date = Label(root,font=("ds-digital",40),background="blue",foreground="lime")
Date.pack(anchor="center")

Time = Label(root,font=("ds-digital",70),background="blue",foreground="lime")
Time.pack(anchor="center")

clock()
mainloop()