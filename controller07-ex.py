"""
Touch-to-Drive Controller

This is how this script works:
    pressing 1 -> turns LED to red and drives the robot
                  at full power (0.9) for 0.3 seconds.
    pressing 3 -> exits the script.

The user is prompted in the terminal for each input.
Each selection changes the LED, drives the motors,
and confirms the action before prompting again.
"""

# import required libraries
import time
from adafruit_crickit import crickit as ck

# define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF, off=0x000000)
BRIGHTNESS = 0.01
DELAY = 0.3        # motor drive duration in seconds
THROTTLE = 0.9     # full power (never use 1.0)


def drive_motors(duration):
    """Drive both motors at full power for the given duration, then stop."""
    ck.dc_motor_1.throttle = THROTTLE
    ck.dc_motor_2.throttle = THROTTLE
    time.sleep(duration)
    ck.dc_motor_1.throttle = 0
    ck.dc_motor_2.throttle = 0


def main():
    # initialize LED brightness
    ck.onboard_pixel.brightness = BRIGHTNESS

    print("=" * 40)
    print("  Touch-to-Drive Controller")
    print("=" * 40)
    print("  1 = Change (LED Red + Drive)")
    print("  3 = Exit")
    print("=" * 40)

    try:
        while True:
            choice = input("\nEnter your choice (1 or 3): ").strip()

            if choice == "1":
                # turn LED red
                ck.onboard_pixel.fill(RGB["red"])
                print("  -> LED changed to red")
                # drive the robot
                print(f"  -> Driving motors at {THROTTLE} for {DELAY}s...")
                drive_motors(DELAY)
                print("  -> Motors stopped")

            elif choice == "3":
                print("  -> Exiting...")
                break

            else:
                print("  -> Invalid input. Please enter 1 or 3.")

    except KeyboardInterrupt:
        print("\n  -> Interrupted by user.")

    finally:
        # turn off LED and motors on exit
        ck.onboard_pixel.fill(RGB["off"])
        ck.dc_motor_1.throttle = 0
        ck.dc_motor_2.throttle = 0
        print("  -> LED and motors off. Goodbye!")


if __name__ == "__main__":
    main()
