import tkinter as tk
import os
import sys
from datetime import datetime

root = tk.Tk()

root.title("Automatic Shutdown")
img = tk.PhotoImage(file='assets/icon.png')
root.iconphoto(False, img)

canvas1 = tk.Canvas(root, width=400, height=300, background='#B9D3E9')
canvas1.create_text(200, 20, text="Please enter the time you want the pc to be shut down.", fill="black")
canvas1.create_text(200, 35, text="example format: 23:41", fill="black")
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def shutdown_timer():  
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current time is ",current_time)
    current_time = current_time.split(":")

    shutdown_time = entry1.get()
    shutdown_time = shutdown_time.split(":")

    current_time = now.strftime("%H:%M")
    current_time = current_time.split(":")

    seconds=((int(shutdown_time[0])-int(current_time[0]))*60*60)+(int(shutdown_time[0])-int(current_time[0])*60)

    print(seconds)  
    os.system(f"shutdown -s -f -t {seconds}")


def cancel_shutdown():
  os.system('shutdown /a')


        
button1 = tk.Button(text='Set shutdown', command=shutdown_timer)
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text='Cancel Shutdown', command=cancel_shutdown)
canvas1.create_window(200, 210, window=button2)

root.mainloop()