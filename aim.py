import tkinter as tk
import time
import random


main = tk.Tk()
canvas = tk.Canvas(main, width=800, height=600)
main.geometry("800x600")

circle1 = canvas.create_oval(375, 275, 425, 325, fill='red', outline='red', tags='start')

samples = []
def create_circle():
    x = random.randint(0, 750)
    y = random.randint(0, 50)
    r = 50
    colors = ['red', 'yellow', 'blue', 'green', 'black', 'magenta']
    color = random.choice(colors)
    global circle, start_t
    circle = canvas.create_oval(x, y, x+r, y+r,fill=color, outline=color, tags='circle')
    start_t = time.time()    

def pressed1(event):
    end_t = time.time()
    canvas.delete(circle)
    print(f'\nreaction time: {end_t-start_t:.4f} s')
    samples.append(end_t-start_t)
    create_circle()
    

    if len(samples) == 10:
        print(f'\nYour average reaction time: {sum(samples)/10}')
        main.destroy()

def start(event):
    canvas.delete(circle1)
    create_circle()

canvas.tag_bind('start', '<Button-1>', start)
canvas.tag_bind('circle','<Button-1>', pressed1)

canvas.pack()

main.mainloop()

