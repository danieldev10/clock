from tkinter import Label, Tk
from time import ctime
import calendar

app_window = Tk()
app_window.title("Digital Clock")
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#003366"
foreground = "#fff"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=2, column=1)

def digital_clock(): 
   time_live = ctime()
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()