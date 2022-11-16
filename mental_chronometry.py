import tkinter as tk
import time
import random

main = tk.Tk()
canvas = tk.Canvas(main, width=800, height=600)
main.geometry("800x600")
starting_rectangle = canvas.create_rectangle(0,0,800,600,fill='white',tags='starting_rectangle')
samples = []

def wait(event):
    time.sleep(random.randint(2,5))
    canvas.delete(starting_rectangle)
    global start_t, rectangle
    rectangle = canvas.create_rectangle(0,0,800,600, fill='green2', tags='rectangle')
    start_t = time.time()

def clicked(event):
    end_t = time.time()
    print(f'reaction time: {end_t-start_t:.3f} s')
    samples.append(end_t-start_t)
    canvas.delete(rectangle)
    global starting_rectangle
    starting_rectangle = canvas.create_rectangle(0,0,800,600,fill='white',tags='starting_rectangle')
    if len(samples) == 5:
        print(f'Your average reaction {sum(samples)/5:.3f} s')
        main.destroy()


canvas.tag_bind('starting_rectangle', '<Button-1>', wait)
canvas.tag_bind('rectangle', '<Button-1>', clicked)

canvas.pack()

main.mainloop()