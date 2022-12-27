import serial
import time
import tkinter
from tkinter import ttk
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

ser = serial.Serial('/dev/ttyUSB0', 9600) # Arduino porti (Windows uchun COM_X ko'rinishida beriladi)
#time.sleep(3)

def button_on():
	ser.write(bytes('1', 'UTF-8'))

def button_off():
	ser.write(bytes('2', 'UTF-8'))

def button_m1():
	ser.write(bytes('3', 'UTF-8'))

def button_m2():
	ser.write(bytes('4', 'UTF-8'))

def button_m3():
	ser.write(bytes('5', 'UTF-8'))

def button_up():
	ser.write(bytes('6', 'UTF-8'))

def button_down():
	ser.write(bytes('7', 'UTF-8'))

def aboutprogram():
	about_win = tkinter.Toplevel(win)
	ws = win.winfo_screenwidth()
	hs = win.winfo_screenheight()
	about_win.resizable(0, 0)
	sx = (ws/2) - (160/2)
	sy = (hs/2) - (100/2)
	about_win.geometry('%dx%d+%d+%d' % (160, 100, sx, sy))
	about_win.resizable(0, 0)
	about_win.title("Dastur haqida")
	
	comp = tkinter.Label(about_win, text ="Yetim dasturchi\npiradakshin :)\n\nwww.manu.uno\n@yetimdasturchi")
	comp.pack(pady = 25, side = tkinter.RIGHT)
	comp.configure(font=("Courier", 12))
	comp.place(x=3, y=4)

def quit_window(icon, item):
   icon.stop()
   win.destroy()

def show_window(icon, item):
   icon.stop()
   win.after(0,win.deiconify())

def hide_window():
   win.withdraw()
   image=Image.open("favicon.ico")
   menu=(item('Ochish', show_window), item('Chiqish', quit_window))
   icon=pystray.Icon("name", image, "Manu Light", menu)
   icon.run()

win = tkinter.Tk()
#win.geometry("800x600")
win.title("Led") #Manu ledlight
#win.iconbitmap(default=resource_path("icon.ico"))
win.resizable(0, 0)
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
sx = (ws/2) - (166/2)
sy = (hs/2) - (166/2)
win.geometry('%dx%d+%d+%d' % (166, 166, sx, sy))
win.protocol('WM_DELETE_WINDOW', hide_window)

button_on = tkinter.Button(win,
    text="Yoqish",
    command=button_on,
    height = 1,
    fg = "black",
    width = 5,
    bd = 1,
)
button_on.pack(side='top', ipadx=5, padx=5, pady=5)
button_on.place(x=2, y=2)

button_off = tkinter.Button(win,
    text="O'chirish",
    command=button_off,
    height = 1,
    fg = "black",
    width = 5,
    bd = 1,
)
button_off.pack(side='top', ipadx=5, padx=5, pady=5)
button_off.place(x=90, y=2)

separator = ttk.Separator(win, orient='horizontal')
separator.place(relx=0, rely=0.22, relwidth=1, relheight=1)

button_m1 = tkinter.Button(win,
    text="M1",
    command=button_m1,
    height = 1,
    fg = "black",
    width = 2,
    bd = 1,
)
button_m1.pack(side='top', ipadx=5, padx=5, pady=5)
button_m1.place(x=2, y=42)

button_m2 = tkinter.Button(win,
    text="M2",
    command=button_m2,
    height = 1,
    fg = "black",
    width = 2,
    bd = 1,
)
button_m2.pack(side='top', ipadx=5, padx=5, pady=5)
button_m2.place(x=59, y=42)

button_m3 = tkinter.Button(win,
    text="M3",
    command=button_m3,
    height = 1,
    fg = "black",
    width = 2,
    bd = 1,
)
button_m3.pack(side='top', ipadx=5, padx=5, pady=5)
button_m3.place(x=117, y=42)

separator1 = ttk.Separator(win, orient='horizontal')
separator1.place(relx=0, rely=0.47, relwidth=1, relheight=1)

button_up = tkinter.Button(win,
    text="+",
    command=button_up,
    height = 1,
    fg = "black",
    width = 5,
    bd = 1,
)
button_up.pack(side='top', ipadx=5, padx=5, pady=5)
button_up.place(x=2, y=84)

button_down = tkinter.Button(win,
    text="-",
    command=button_down,
    height = 1,
    fg = "black",
    width = 5,
    bd = 1,
)
button_down.pack(side='top', ipadx=5, padx=5, pady=5)
button_down.place(x=90, y=84)

separator2 = ttk.Separator(win, orient='horizontal')
separator2.place(relx=0, rely=0.72, relwidth=1, relheight=1)

aboutprogram = tkinter.Button(win,
    text="Dastur haqida",
    command=aboutprogram,
    height = 1,
    fg = "black",
    width = 15,
    bd = 1,
)
aboutprogram.pack(side='top', ipadx=5, padx=5, pady=5)
aboutprogram.place(x=2, y=127)

#win.state("zoomed")
win.mainloop()