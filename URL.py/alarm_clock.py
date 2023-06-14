import datetime
import time
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Get the alarm time entered by the user
    alarm_time = entry.get()

    # Loop until the current time matches the alarm time
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)

    # Display the alarm message
    messagebox.showinfo("Alarm", "Wake up!")

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label and an entry widget for the alarm time
label = tk.Label(window, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Start the main event loop
window.mainloop()
