# BEAPER Nano I/O Test project
# September 21, 2024
# Example program to test digital pins and PWM function

# Import machine and time functions
from machine import Pin, PWM
import time

# Configure Educational Starter I/O devices
SW2 = Pin(44, Pin.IN, Pin.PULL_UP)
SW3 = Pin(43, Pin.IN, Pin.PULL_UP)
SW4 = Pin(5, Pin.IN, Pin.PULL_UP)
SW5 = Pin(6, Pin.IN, Pin.PULL_UP)
LED2 = Pin(7, Pin.OUT)
LED3 = Pin(8, Pin.OUT)
LED4 = Pin(9, Pin.OUT)
LED5 = Pin(10, Pin.OUT)
BEEPER = Pin(17, Pin.OUT)

# Define toggle button variables
SW4IsPressed = False
LED4State = 0

# Tone functions
def tone(frequency,duration=None):
    beeperPin = PWM(Pin(17), duty_u16 = 32768)
    beeperPin.freq(frequency)
    if duration is not None:
        time.sleep(duration)
        noTone()

def noTone(duration=None):
    beeperPin = PWM(Pin(17))
    beeperPin.deinit()
    if duration is not None:
        time.sleep(duration)

# Start-up sound
tone(4000,0.1)

while True:
    if SW2.value() == 0:
        # Sweep LEDs
        LED2.value(1)
        time.sleep(0.1)
        LED3.value(1)
        time.sleep(0.1)
        LED4.value(1)
        time.sleep(0.1)
        LED5.value(1)
        time.sleep(0.1)
        
        LED2.value(0)
        time.sleep(0.1)
        LED3.value(0)
        time.sleep(0.1)
        LED4.value(0)
        time.sleep(0.1)
        LED5.value(0)
        time.sleep(0.1)
    
    if SW3.value() == 0:
        # Beep, boop
        LED3.value(1)
        tone(700, 0.16)
        noTone(0.05)
        tone(600, 0.16)
    else:
        LED3.value(0)
    
    # Toggle button
    if SW4.value() == 0 and SW4IsPressed == False:
        SW4IsPressed = True
        if LED4State == 0:
            LED4State = 1
        else:
            LED4State = 0
            
    LED4.value(LED4State)
    
    if SW4.value() == 1:
        SW4IsPressed = False
    
    if SW5.value() == 0:
        # Fade-out LED5
        pwmLED = PWM(Pin(10), freq=1000)
        for brightness in range(65535, 0, -1024):
            pwmLED.duty_u16(brightness)
            time.sleep_ms(10)
        pwmLED.deinit()
        LED5 = Pin(10, Pin.OUT)

    time.sleep(0.01)
