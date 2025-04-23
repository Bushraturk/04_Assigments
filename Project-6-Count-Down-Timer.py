#Project 6 : Count Down Timer


     

import time
import os  # To clear the screen

def countdown_timer(seconds):
    while seconds > 0:
        mins, sec = divmod(seconds, 60)  # Convert seconds to MM:SS format
        time_format = '{:02d}:{:02d}'.format(mins, sec)

        os.system("cls" if os.name == "nt" else "clear")  # Clear screen for Windows/Mac/Linux
        print(time_format)  # Print time clearly

        time.sleep(1)  # Delay 1 second
        seconds -= 1  # Reduce time

    # When timer reaches 0
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen before showing final message
    print("00:00 \nTime's up! ⏰")
