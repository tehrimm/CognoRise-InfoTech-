from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime

def quit(*args):
    root.destroy()

# Function to stop (pause) the countdown
def stop_countdown():
    global running, remaining_time
    running = False
    remaining_time = endTime - datetime.datetime.now()  # Calculate remaining time
    txt.set(txt.get())  # Display the current time

# Function to calculate the remaining time and update the label
def cant_wait():
    if not running:
        return  # Stop updating if countdown is paused

    timeLeft = endTime - datetime.datetime.now()
    seconds_left = int(timeLeft.total_seconds())

    if seconds_left >= 0:
        time_str = str(datetime.timedelta(seconds=seconds_left))
        txt.set(time_str)
        root.after(1000 - datetime.datetime.now().microsecond // 1000, cant_wait)
    else:
        txt.set("00:00:00")
        minutes_entry.delete(0, END)  # Clear minutes entry when done
        seconds_entry.delete(0, END)  # Clear seconds entry when done

# Function to start or resume the countdown with the user-defined time
def start_countdown():
    global endTime, running
    running = True
    try:
        if not endTime:
            # If no existing endTime, start a new countdown
            user_minutes = int(minutes_entry.get())
            user_seconds = int(seconds_entry.get())
            total_seconds = user_minutes * 60 + user_seconds
            endTime = datetime.datetime.now() + datetime.timedelta(seconds=total_seconds)
        else:
            # Resume from where it was paused
            endTime = datetime.datetime.now() + remaining_time
        cant_wait()
    except ValueError:
        txt.set("Invalid time!")

# main window
root = Tk()
root.title("Countdown Timer")
root.configure(background='black')
root.geometry("400x300")  # Set a fixed window size

# Font settings
fnt = font.Font(family="Helvetica", size=50, weight='bold')

# StringVar to update the label with the remaining time
txt = StringVar()
txt.set("00:00:00")

# Create the label to display the countdown time
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.4, anchor=CENTER)

# Entry fields for minutes and seconds
minutes_label = ttk.Label(root, text="Minutes:", font=("Helvetica", 15), foreground="white", background="black")
minutes_label.place(relx=0.25, rely=0.7, anchor=CENTER)
minutes_entry = ttk.Entry(root, font=("Helvetica", 15), width=3)
minutes_entry.place(relx=0.4, rely=0.7, anchor=CENTER)

seconds_label = ttk.Label(root, text="Seconds:", font=("Helvetica", 15), foreground="white", background="black")
seconds_label.place(relx=0.6, rely=0.7, anchor=CENTER)
seconds_entry = ttk.Entry(root, font=("Helvetica", 15), width=3)
seconds_entry.place(relx=0.75, rely=0.7, anchor=CENTER)

# Start button to begin or resume the countdown
start_button = ttk.Button(root, text="Start", command=start_countdown)
start_button.place(relx=0.35, rely=0.85, anchor=CENTER)

# Stop button to pause the countdown
stop_button = ttk.Button(root, text="Stop", command=stop_countdown)
stop_button.place(relx=0.65, rely=0.85, anchor=CENTER)

# Initialize variables
endTime = None
remaining_time = datetime.timedelta(seconds=0)
running = False

root.bind("x", quit)

# Run the main loop
root.mainloop()
