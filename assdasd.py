import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

GRID_ROWS, GRID_COLS = 15, 73
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
GREEN_SEATS = [(0, (3, 19), (22, 42), (47, 64)), (1, (3, 14), (23, 41), (45, 56), (59, 66)), (2, (1, 14), (21, 43), (45, 56), (59, 66)), (3, (1, 14), (22, 43), (45, 56), (59, 66)), (4, (1, 13), (22, 42), (45, 56), (59, 66)), (5, (1, 13), (21, 42), (50, 66)), (6, (1, 12), (23, 41), (53, 66)), (7, (1, 12), (24, 40), (53, 66)), (8, (1, 11), (25, 39), (54, 66)), (9, (1, 10), (26, 39), (54, 66)), (10, (1, 9), (26, 38), (55, 66)), (11, None, None, None, None, None, None, None, None, None, None, None, None, None, (55, 66)), (12, None, None, None, None, None, None, None, None, None, None, None, None, None, (56, 66)), (13, None, None, None, None, None, None, None, None, None, None, None, None, (57, 66)), (14, None, None, None, None, None, None, None, None, None, None, None, (58, 66))]
COLOR_MAP = {"": "black", "orange": "lightblue", "lightblue": "red", "red": "orange"}

def on_click(event):
    seat_label = event.widget
    current_color = seat_label.cget("background")
    if current_color in COLOR_MAP:
        new_color = COLOR_MAP[current_color]
        seat_label.configure(bg=new_color)
        row, col = seat_label.grid_info()["row"], seat_label.grid_info()["column"]
        seats[(row, col)] = ["lightblue", "orange", "red", 0][list(COLOR_MAP.values()).index(new_color)]

root = tk.Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.attributes("-fullscreen", True)
root.resizable(False, False)
root.title("Selektor Sedišta")
root.configure(bg="black")

grid = [[tk.Label(root, text=(row, col), borderwidth=1, relief="solid", width=3, height=2, bg=COLOR_MAP.get("".join(["orange" if row == g[0] and any([r and col >= r[0] + 3 and col <= r[1] + 3 for r in g[1:]]) else "" for g in GREEN_SEATS]), "black")) for col in range(GRID_COLS)] for row in range(GRID_ROWS)]
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        seat_label = grid[row][col]
        seat_label.bind("<Button-1>", on_click)
        seat_label.grid(row=row, column=col)
seats = {}
count = 1
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        seat_color = COLOR_MAP.get("".join(["orange" if row == g[0] and any([r and col >= r[0] + 3 and col <= r[1] + 3 for r in g[1:]]) else "" for g in GREEN_SEATS]), "black")
        if seat_color == "lightblue":
            seats[(row, col)] = count
            count += 1
        else:
            seats[(row, col)] = 0
        seat_label = tk.Label(root, text=seats[(row, col)], borderwidth=1, relief="solid", width=3, height=2, bg=seat_color)
        seat_label.bind("<Button-1>", on_click)
        seat_label.grid(row=row, column=col)

seats_list = []
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        seat_label = grid[row][col]
        color = seat_label.cget("background")
        if color == "black":
            seat_value = 0
        elif color == "lightblue":
            seat_value = 1
        elif color == "red":
            seat_value = 2
        elif color == "orange":
            seat_value = 3
        seats_list.append((row, col, seat_value))
          
root.mainloop()