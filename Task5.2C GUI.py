# Import the required modules from tkinter and gpiozero
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set the GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Initialize LED objects for red, green, and yellow lights
red = LED(14)
green = LED(15)
yellow = LED(18)

# Create the main Tkinter window
win = Tk()
win.title("Traffic Light Toggler")

# Define a custom font for the user interface
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Function to toggle the state of an LED
def toggle_led(led, other_leds):
    if led.is_lit:
        led.off()
    else:
        led.on()
        for ol in other_leds:
            ol.off()

# Functions to control the red, green, and yellow LEDs
def RedLed():
    toggle_led(red, [green, yellow])

def GreenLed():
    toggle_led(green, [red, yellow])

def YellowLed():
    toggle_led(yellow, [red, green])

# Function to clean up GPIO and close the window
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create an IntVar to hold the selected LED
selected_led = IntVar()

# Create radio buttons for the red, green, and yellow LEDs
redButton = Radiobutton(win, text='Red LED', font=myFont, variable=selected_led, value=1, command=RedLed, bg='red')
redButton.grid(row=0, column=1)

greenButton = Radiobutton(win, text='Green LED', font=myFont, variable=selected_led, value=2, command=GreenLed, bg='green')
greenButton.grid(row=1, column=1)

yellowButton = Radiobutton(win, text='Yellow LED', font=myFont, variable=selected_led, value=3, command=YellowLed, bg='yellow')
yellowButton.grid(row=2, column=1)

# Create an exit button to clean up and close the application
exitButton = Button(win, text='Exit', font=myFont, command=close, bg='grey', height=1, width=6)
exitButton.grid(row=3, column=1)

# Handle window close event to ensure cleanup
win.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter event loop
win.mainloop()
