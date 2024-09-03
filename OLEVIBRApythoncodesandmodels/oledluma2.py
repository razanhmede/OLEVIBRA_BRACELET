import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
def get_device():
    # Define your I2C interface and device here
    serial = i2c(port=1, address=0x3C)  # Adjust the address based on your OLED display
    return sh1106(serial)

def main():
    device = get_device()

    with canvas(device) as draw:
        draw.text((10, 10), "WELCOME TO OLEVIBRA!", fill="white")

    time.sleep(60)  

if __name__ == "__main__":
    main()



