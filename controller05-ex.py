"""
Touch-to-LED Controller

This is how this script works:
    pressing 1 -> turns LED to blue.
    pressing 2 -> turns LED to green.
    pressing 3 -> turns LED to red.
    pressing 4 -> exits the script.

The user is prompted in the terminal for each input.
Each selection changes the LED and confirms the change
before prompting again.
"""

# import required libraries
from adafruit_crickit import crickit


# define hyper parameters
RGB = dict(red=0xFF0000, green=0x00FF00, blue=0x0000FF, off=0x000000)
BRIGHTNESS = 0.01

# map user input to color names
COLOR_MAP = {
    "1": "blue",
    "2": "green",
    "3": "red",
}


def main():
    # initialize LED brightness
    crickit.onboard_pixel.brightness = BRIGHTNESS

    print("=" * 35)
    print("  Touch-to-LED Controller")
    print("=" * 35)
    print("  1 = Blue")
    print("  2 = Green")
    print("  3 = Red")
    print("  4 = Exit")
    print("=" * 35)

    try:
        while True:
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice in COLOR_MAP:
                color_name = COLOR_MAP[choice]
                crickit.onboard_pixel.fill(RGB[color_name])
                print(f"  -> LED changed to {color_name}")

            elif choice == "4":
                print("  -> Exiting...")
                break

            else:
                print("  -> Invalid input. Please enter 1, 2, 3, or 4.")

    except KeyboardInterrupt:
        print("\n  -> Interrupted by user.")

    finally:
        # turn off LED on exit
        crickit.onboard_pixel.fill(RGB["off"])
        print("  -> LED turned off. Goodbye!")


if __name__ == "__main__":
    main()
