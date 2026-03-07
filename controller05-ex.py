"""
Touch-to-LED Controller

This is how this script works:
    pressing touch 1 -> turns LED to blue.
    pressing touch 2 -> turns LED to green.
    pressing touch 3 -> turns LED to red.
    pressing touch 4 -> exits the script.

Improvements over base version:
    - Debouncing to prevent rapid color flickering
    - Only updates LED when color actually changes (fewer I2C writes)
    - Console feedback showing active color
    - Graceful cleanup on exit (LED turns off)
    - Error handling for hardware issues and KeyboardInterrupt
"""

# import required libraries
from adafruit_crickit import crickit
import time


# define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF, off=0x000000)
BRIGHTNESS = 0.01
DEBOUNCE_DELAY = 0.15   # seconds to wait after a touch (prevents flickering)
POLL_INTERVAL = 0.05    # seconds between sensor reads


def set_led(color_name):
    """Set the onboard LED to a named color and print feedback."""
    crickit.onboard_pixel.fill(RGB[color_name])
    print(f"  LED -> {color_name}")


def cleanup():
    """Turn off the LED on exit."""
    crickit.onboard_pixel.fill(RGB["off"])
    print("LED off. Goodbye!")


def main():
    # initialize LED brightness
    crickit.onboard_pixel.brightness = BRIGHTNESS

    # map touch sensors to color names
    touch_map = [
        (crickit.touch_1, "blue"),
        (crickit.touch_2, "green"),
        (crickit.touch_3, "red"),
    ]

    current_color = None

    print("Touch-to-LED Controller")
    print("-" * 30)
    print("  Touch 1 = Blue")
    print("  Touch 2 = Green")
    print("  Touch 3 = Red")
    print("  Touch 4 = Exit")
    print("-" * 30)

    try:
        while True:
            # check color touch sensors
            for sensor, color_name in touch_map:
                if sensor.value:
                    if current_color != color_name:
                        set_led(color_name)
                        current_color = color_name
                    time.sleep(DEBOUNCE_DELAY)
                    break

            # check exit touch sensor
            if crickit.touch_4.value:
                print("\nTouch 4 pressed — exiting.")
                break

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        cleanup()


if __name__ == "__main__":
    main()
