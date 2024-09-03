import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the motor
motor_pin = 18

# Set up the GPIO pin as an output
GPIO.setup(motor_pin, GPIO.OUT)

try:
    # Run the motor for 2 seconds
    GPIO.output(motor_pin, GPIO.HIGH)
    print("Motor is ON")
    time.sleep(2)

    # Turn off the motor
    GPIO.output(motor_pin, GPIO.LOW)
    print("Motor is OFF")

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

finally:
    # Clean up GPIO on normal exit
    GPIO.cleanup()
