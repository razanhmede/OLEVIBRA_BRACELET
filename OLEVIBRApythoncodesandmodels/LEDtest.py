import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
led_pin = 17

# Set up the GPIO pin as an output
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Loop indefinitely
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED on")
        # Wait for 1 second
        time.sleep(1)
        # Turn the LED off
        GPIO.output(led_pin, GPIO.LOW)
        print("LED off")
        # Wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    # If CTRL+C is pressed, clean up GPIO settings
    GPIO.cleanup()
