# Import necessary modules
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

import RPi.GPIO as GPIO # Import the RPi.GPIO library for controlling Raspberry Pi GPIO pins
#import time
GPIO.setmode(GPIO.BOARD)    # Set the GPIO mode to use the physical pin numbering
# Configure GPIO pins 18, 15, and 16 as output pins
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# Define a function to be called when the "Red" button is clicked
def clickMethodRed():
    print("Red Button Clicked")
     # Turn on the Red LED (pin 18) and turn off the Green (pin 15) and White (pin 16) LEDs
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)

# Define a function to be called when the "Green" button is clicked
def clickMethodGreen():
    print("Green Button Clicked")
     # Turn on the Green LED (pin 15) and turn off the Red (pin 18) and White (pin 16) LEDs
    GPIO.output(18, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)

# Define a function to be called when the "White" button is clicked
def clickMethodWhite():
    print("White Button Clicked")
    # Turn on the White LED (pin 16) and turn off the Red (pin 18) and Green (pin 15) LEDs
    GPIO.output(18, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    
# Define a function to be called when the "Exit" button is clicked
def clickExit():
    print("Exit Button Clicked")
    # Turn off all the LEDs (Red, Green, White)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    
     

app = QApplication([])  # Create a PyQt application instance
win = QMainWindow() # Create a main window
# Set the main window's title, size, and position
win.setWindowTitle("Button Led")
win.resize(500,200)
win.move(400,200)

# Create a "Blink Red" button with a red background
buttonRed = QPushButton("Blink Red", win)
buttonRed.setStyleSheet("background-color : red")
buttonRed.move(20,40)
buttonRed.clicked.connect(clickMethodRed)

# Create a "Blink Green" button with a green background
buttonGreen = QPushButton("Blink Green", win)

buttonGreen.setStyleSheet("background-color : green")
buttonGreen.move(20,80)
buttonGreen.clicked.connect(clickMethodGreen)

# Create a "Blink White" button with a white background
buttonWhite = QPushButton("Blink White", win)

buttonWhite.setStyleSheet("background-color : White")
buttonWhite.move(20,120)
buttonWhite.clicked.connect(clickMethodWhite)

# Create an "Exit Button" with a grey background
buttonExit = QPushButton("Exit Button", win)

buttonExit.setStyleSheet("background-color : grey")
buttonExit.move(20,160)
buttonExit.clicked.connect(clickExit)

win.show()  # Show the main window
sys.exit(app.exec_())   # Start the PyQt application event loop and exit when the window is closed
    
