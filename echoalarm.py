# -----------------------------------------------------------
# Project Name: EchoAlarm
# Description: A simple countdown timer with user input, alarm sound and desktop notification
# Author: Emre Murat Adlı
# -----------------------------------------------------------

import time  # Used for countdown and delays
from playsound import playsound  # Used to play a sound file
from plyer import notification  # Used to send a desktop notification

# --- SETTINGS ---
ALARM_SOUND_PATH = "alarm.mp3"  # Path to the alarm sound file
NOTIFICATION_TITLE = "Time's up!"  # Title of the desktop notification
NOTIFICATION_MESSAGE = "The countdown has finished."  # Message of the desktop notification


def get_user_input():
    """
    Function to get countdown time from user.
    Ensures that the input is a valid positive integer.
    """
    while True:
        try:
            seconds = int(input("Enter countdown time in seconds: "))
            if seconds > 0:
                return seconds
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")


def countdown(seconds):
    """
    Function to perform countdown from the given number of seconds.
    Displays the remaining time every second.
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert total seconds to minutes and seconds
        timer_format = '{:02d}:{:02d}'.format(mins, secs)  # Format as MM:SS
        print(timer_format, end='\n')  # Print on a new line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease time by 1 second


def play_alarm(sound_path):
    """
    Function to play an alarm sound.
    Takes the path of the sound file as input.
    """
    try:
        playsound(sound_path)
    except Exception as e:
        print("Error playing sound:", e)


def send_notification(title, message):
    """
    Function to send a desktop notification.
    Takes the title and message as input.
    """
    try:
        notification.notify(
            title = title,
            message = message,
            timeout = 5 # Notification disappears after 5 seconds
        )
    except Exception as e:
        print("Error sending notification:", e)


def main():
    """
    Main function to coordinate user input, countdown, playing sound, and sending notification.
    """
    print("Welcome to EchoAlarm!") # Friendly greeting
    seconds = get_user_input() # Get countdown time from user

    print(f"Countdown started for {seconds} seconds...")
    countdown(seconds)

    print("Time is up!")

    #Play alarm sound
    play_alarm(ALARM_SOUND_PATH)

    #Send desktop notification
    send_notification(NOTIFICATION_TITLE, NOTIFICATION_MESSAGE)


# --- ENTRY POINT ---
if __name__ == "__main__":
    main()
