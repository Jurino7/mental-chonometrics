import tkinter as tk
import time
import random


main = tk.Tk()
canvas = tk.Canvas(main, width=800, height=600)
main.geometry("800x600")


samples = []

def createTarget():
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
    print(f'\nreaction time: {end_t-start_t:.4f} s')
    canvas.delete(circle)
    print('Button-1 pressed at x = % d, y = % d'%(event.x, event.y))
    samples.append(end_t-start_t)
    createTarget()
    if len(samples) == 10:
        print(f'\nYour average reaction time: {sum(samples)/10}')
        main.destroy()


createTarget()
canvas.tag_bind('circle','<Button-1>', pressed1)

canvas.pack()

main.mainloop()

