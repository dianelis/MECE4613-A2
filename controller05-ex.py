"""
You need to complete this script on your own in the lab.

This is how this script should work:
    pressing touch 1 -> turns LED to blue.
    pressing touch 2 -> turns LED to green.
    pressing touch 3 -> turns LED to red.
    pressing touch 4 -> exits the script.
"""

# import required libraries
from adafruit_crickit import crickit
import time


# define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF)
crickit.onboard_pixel.brightness = 0.01


def main():
    # YOUR CODE STARTS HERE
    print("Touch 1=blue, 2=green, 3=red, 4=exit")

    while True:
        if crickit.touch_1.value:
            crickit.onboard_pixel.fill(RGB["blue"])
        elif crickit.touch_2.value:
            crickit.onboard_pixel.fill(RGB["green"])
        elif crickit.touch_3.value:
            crickit.onboard_pixel.fill(RGB["red"])
        elif crickit.touch_4.value:
            break

        time.sleep(0.05)
    # YOUR CODE ENDS HERE


if __name__ == "__main__":
    main()
