from pynput.mouse import Button, Controller
import tkinter as tk
from tkinter import messagebox
import keyboard
import time
import sys

root  = tk.Tk()
root.title("AutoClicker")
root.geometry("350x250")
root.iconbitmap("icon.ico")

clickedTimes = tk.StringVar()
countDown = tk.StringVar()
untilStart = tk.StringVar()

mouse = Controller()
amount = 0
clicks = 0
clearText = ""

def presser():
    countDown.set(str(clearText))
    untilStart.set(str(clearText))
    root.update()
    clicked = 0
    sleepTimeInput = 0
    amount = e.get()
    sleepTimeInput = e1.get()
    try:
        clicks = int(amount)
        sleepTime = float(sleepTimeInput)
        for i in range(clicks):
            if keyboard.is_pressed('q'):  
                print('Stopping autoclicker')
                sys.exit(1)
        
            time.sleep(sleepTime)
            mouse.press(Button.left)
            mouse.release(Button.left)
            clicked += 1
            clickedTimes.set(str(clicked))
            root.update()

    except ValueError:
        messagebox.showerror("Error", "You need to type a number")

"Until autoclicker starts"

def countdown():
    count = 6
    while count > 1:
        time.sleep(1)
        count -= 1
        countDown.set(str(count))
        root.update()
    presser()




label = tk.Label(root, text="How many times do you want to click?")
label.config(font=('Arial', 10))
label.pack()


e = tk.Entry(root) 
e.pack()
e.get()


fast = tk.Label(root, text="How fast do you want it to click (in seconds)?")
fast.config(font=('Arial', 10))
fast.pack()


e1 = tk.Entry(root) 
e1.pack()
e1.get()


run_btn = tk.Button(root, text="Run", command=countdown)
run_btn.pack()


label3 = tk.Label(root, text="Clicked:")
label3.pack()


label2 = tk.Label(root, textvariable=clickedTimes)
label2.config(font=('Arial', 30))
label2.pack()



label4 = tk.Label(root, textvariable=countDown)
label4.config(font=('Arial', 30))
label4.pack()

root.mainloop()

