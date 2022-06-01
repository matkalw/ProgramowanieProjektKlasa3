import tkinter
import customtkinter
import math
import time

t = 0               #time [s]
v0 = 36             #initial velocity [m/s]
g = 9.81            #gravity of earth [m/s^2]
h = 0.0             #height [m]
alpha = 30          #angle [°]
buttonStart = 0

root = customtkinter.CTk()
root.state('zoomed')

window_width = root.winfo_width()
window_height = root.winfo_height()

canvas = tkinter.Canvas(root, width = window_width, height = window_height-500)
canvas.grid(column=0, row=2, columnspan=4)
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()
ground = canvas.create_rectangle(0, canvas_height - 100, canvas_width, canvas_height, fill = "green", width = 0)

entry_alpha     = customtkinter.CTkEntry(root, placeholder_text="0-90°")
entry_height    = customtkinter.CTkEntry(root, placeholder_text=">0")
entry_v0        = customtkinter.CTkEntry(root, placeholder_text=">0")

entry_alpha     .grid(column = 0, row = 1, pady = 30)
entry_height    .grid(column = 1, row = 1, pady = 30)
entry_v0        .grid(column = 2, row = 1, pady = 30)
root.update()

def get_values():
    global ball, alpha, h, v0
    if entry_alpha.get() != "":
        get_values.alpha   = float(entry_alpha.get())
    if entry_height.get() != "":
        get_values.h       = float(entry_height.get())
    if entry_v0.get() != "":
        get_values.v0      = float(entry_v0.get())
    if "ball" in locals() or "ball" in globals():
        canvas.delete(ball)
    ball = canvas.create_oval(0, canvas_height - 100 - (h*100), 100, canvas_height - 100 - (h*100 + 100), fill = "yellow", width = 2)

get_values()

label_alpha     = customtkinter.CTkLabel(root, text="Kat:")
label_height    = customtkinter.CTkLabel(root, text="Wysokosc:")
label_v0        = customtkinter.CTkLabel(root, text="Predkosc poczatkowa:")
button_get      = customtkinter.CTkButton(root, text="Get Values", hover = "enable", command = get_values)

label_alpha     .grid(column = 0, row = 0, pady = 30)
label_height    .grid(column = 1, row = 0, pady = 30)
label_v0        .grid(column = 2, row = 0, pady = 30)
button_get      .grid(column = 3, row = 0, pady = 30)
root.update()

x_position = v0 * t * math.cos(math.radians(alpha))
y_position = v0 * t * math.sin(math.radians(alpha)) - (g * t ** 2) / 2

def start():
    global buttonStart
    buttonStart = 1

button_get      = customtkinter.CTkButton(root, text="Start", hover = "enable", command =  start)
button_get      .grid(column = 3, row = 1)

while True:
    if buttonStart == 1:
        horizontal_velocity = v0 * math.cos(math.radians(alpha))
        vertical_velocity = g * t - v0 * math.sin(math.radians(alpha))
        canvas.move(ball, horizontal_velocity, vertical_velocity)
        time.sleep(0.05)
        t += 0.1
    canvas.update()
    if canvas.coords(ball)[3] > canvas_height - 100:
        buttonStart = 0