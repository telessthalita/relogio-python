from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

root = Tk()
root.title("Relógio")
root.configure(background="purple")

time_label = Label(root, font=("Arial", 80), bg="purple", fg="white")
time_label.pack(pady=50)

update_time()

root.mainloop()