import datetime
import time
import winsound
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get()

    try:
        # Parse the alarm time entered by the user
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        current_time = datetime.datetime.now()
        alarm_time = current_time.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

        # Calculate the time difference between the current time and the alarm time
        time_diff = alarm_time - current_time

        if time_diff.total_seconds() < 0:
            # If the alarm time has already passed, show an error message
            messagebox.showerror("Invalid Time", "Please enter a future time.")
        else:
            # Wait for the specified time duration before playing the alarm sound
            time.sleep(time_diff.total_seconds())

            # Play the alarm sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

            # Show a message box when the alarm goes off
            messagebox.showinfo("Alarm", "Wake up!")

    except ValueError:
        # If the user enters an invalid time format, show an error message
        messagebox.showerror("Invalid Time", "Please enter time in HH:MM format.")

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label and an entry field for entering the alarm time
label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Start the main event loop
window.mainloop()