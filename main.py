import tkinter as tk
import datetime

root = tk.Tk()
root.geometry("300x200")  # set the size of the window
root.title("My Window")  # set the title of the window

clock_label = tk.Label(root, font=('LCD-Mono', 290, 'bold'),fg="white", bg='black')
clock_label.pack(fill='both', expand=True)

def update_clock():
    now = datetime.datetime.now()
    clock_label.config(text=now.strftime("%H:%M:%S"))
    root.after(1000, update_clock)  # call update_clock() after 1000ms (1 second)

update_clock()  # start the clock update loop
root.mainloop()  # start the event loop
