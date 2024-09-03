import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas

def get_device():
    # Define your I2C interface and device here
    serial = i2c(port=1, address=0x3C)  # Adjust the address based on your OLED display
    return sh1106(serial)

def right():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "RIGHT", fill="white")
    time.sleep(20)

def up():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "UP", fill="white")
    time.sleep(20)

def left():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "LEFT", fill="white")
    time.sleep(20)

def down():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "DOWN", fill="white")
    time.sleep(20)

def yes():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "YES", fill="white")
    time.sleep(20)

def no():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "NO", fill="white")
    time.sleep(20)

def go():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "GO", fill="white")
    time.sleep(20)

def stop():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "STOP", fill="white")
    time.sleep(20)

def printOLED(command):
    if command == 'up':
        up()
    elif command == 'down':
        down()
    elif command == 'left':
        left()
    elif command == 'right':
        right()
    elif command == 'go':
        go()
    elif command == 'stop':
        stop()
    elif command == 'yes':
        yes()
    elif command == 'no':
        no()
