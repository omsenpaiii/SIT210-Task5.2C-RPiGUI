from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(14)
green = LED(15)
yellow = LED(18)

win = Tk()
win.title("Traffic Light Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

def toggle_led(led, other_leds):
    if led.is_lit:
        led.off()
    else:
        led.on()
        for ol in other_leds:
            ol.off()

def RedLed():
    toggle_led(red, [green, yellow])

def GreenLed():
    toggle_led(green, [red, yellow])

def YellowLed():
    toggle_led(yellow, [red, green])

def close():
    RPi.GPIO.cleanup()
    win.destroy()

selected_led = IntVar()

redButton = Radiobutton(win, text='Red LED', font=myFont, variable=selected_led, value=1, command=RedLed, bg='red')
redButton.grid(row=0, column=1)

greenButton = Radiobutton(win, text='Green LED', font=myFont, variable=selected_led, value=2, command=GreenLed, bg='green')
greenButton.grid(row=1, column=1)

yellowButton = Radiobutton(win, text='Yellow LED', font=myFont, variable=selected_led, value=3, command=YellowLed, bg='yellow')
yellowButton.grid(row=2, column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='grey', height=1, width=6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
