import datetime
import time
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    alarm_time = entry.get()

    messagebox.showinfo("Popup", "Alarm Set!")

    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)

    messagebox.showinfo("Alarm", "Wake up!")


window = tk.Tk()
window.title("Alarm Clock")

label = tk.Label(window, text="Enter alarm time (HH:MM:SS):")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

window.mainloop()
