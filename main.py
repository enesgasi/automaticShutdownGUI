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
canvas1.create_text(200, 35, text="For example: 23:41", fill="black")
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


    if (seconds < 0 ):
      seconds = 0
    try:
      os.system(f'shutdown /s /t {seconds}')
      cancel = input(f"System shutting down in {seconds} seconds.\nEnter 'Cancel' to abort, or press Enter to exit.")
    except:
      input("Unexpected error:", sys.exc_info()[0], "\nPress Enter to exit.")
    if(cancel=="Cancel"):
      os.system('shutdown /a')
      input("System shutdown cancelled.\nPress Enter to exit.")

        
button1 = tk.Button(text='Set shutdown', command=shutdown_timer)
canvas1.create_window(200, 180, window=button1)

root.mainloop()