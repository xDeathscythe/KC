class sedista:


    import tkinter as tk
    import sqlite3

    connection = sqlite3.connect("sedista.db")
    cursor=connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS sedista (row integer, col integer,color string)")

    GRID_ROWS, GRID_COLS = 15, 73
    seats = {(row, col): 0 for row in range(GRID_ROWS) for col in range(GRID_COLS)}
    SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
    root = tk.Tk()
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    root.attributes("-fullscreen", True)
    root.resizable(False, False)
    root.title("Selektor Sedišta")
    root.configure(bg="black")
    grid = []

    for row in range(GRID_ROWS):
        row_labels = []
        for col in range(GRID_COLS):
            bg_color = "black"
            if row == 0 and ((col >= 0+3 and col <= 19+3) or (col >= 22+2+3 and col <= 42+2+3) or (col >= 47+4+3 and col <= 64+2+3)):
                bg_color = "lightblue"
            elif row == 1 and ((col >= 0+3 and col <= 14+3) or (col >= 23+2+3 and col <= 41+2+3) or (col >= 45+4+3 and col <= 56+4+3) or (col >= 59+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 2 and ((col >= 1+3 and col <= 14+3) or (col >= 21+2+3 and col <= 43+2+3) or (col >= 45+4+3 and col <= 56+4+3) or (col >= 59+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 3 and ((col >= 1+3 and col <= 14+3) or (col >= 22+2+3 and col <= 43+2+3) or (col >= 45+4+3 and col <= 56+4+3) or (col >= 59+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 4 and ((col >= 1+3 and col <= 13+3) or (col >= 22+2+3 and col <= 42+2+3) or (col >= 45+4+3 and col <= 56+4+3) or (col >= 59+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 5 and ((col >= 1+3 and col <= 13+3) or (col >= 21+2+3 and col <= 42+2+3) or (col >= 50+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 6 and ((col >= 1+3 and col <= 12+3) or (col >= 23+2+3 and col <= 41+2+3) or (col >= 53+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 7 and ((col >= 1+3 and col <= 12+3) or (col >= 24+2+3 and col <= 40+2+3) or (col >= 53+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 8 and ((col >= 1+3 and col <= 11+3) or (col >= 25+2+3 and col <= 39+2+3) or (col >= 54+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 9 and ((col >= 1+3 and col <= 10+3) or (col >= 26+2+3 and col <= 39+2+3) or (col >= 54+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 10 and ((col >= 1+3 and col <= 9+3) or (col >= 26+2+3 and col <= 38+2+3) or (col >= 55+4+3 and col <= 66+4+3)):
                bg_color = "lightblue"
            elif row == 11 and (col >= 55+4+3 and col <= 66+4+3):
                bg_color = "lightblue"
            elif row == 12 and (col >= 56+4+3 and col <= 66+4+3):
                bg_color = "lightblue"
            elif row == 13 and (col >= 57+4+3 and col <= 66+4+3):
                bg_color = "lightblue"
            elif row == 14 and (col >= 58+4+3 and col <= 66+4+3):
                bg_color = "lightblue"
            else: 
                bg_color = "black"
            label = tk.Label(root, text=(), borderwidth=1, relief="solid", width=3, height=2, bg=bg_color)
            label.grid(row=row, column=col)
            row_labels.append(label)
        grid.append(row_labels)
    def on_click(event, seat_id, seat_label):
        current_color = seat_label.cget("background")
        if current_color == "":
            return
        if current_color == "lightblue":
            seat_label.configure(bg="red")  # change to yellow for reserved seats
            seats[seat_id] = 2
        elif current_color == "red":
            seat_label.configure(bg="yellow")  # change to red for occupied seats
            seats[seat_id] = 1
        elif current_color == "yellow":
            seat_label.configure(bg="lightblue")  # change to red for occupied seats
            seats[seat_id] = 0
        list()
        
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            seat_id = (row, col)
            seat_label = grid[row][col]
            seat_label.bind("<Button-1>", lambda event, seat_id=seat_id, seat_label=seat_label: on_click(event, seat_id, seat_label))

    # Get the data from the database
    cursor.execute("SELECT row, col, color FROM sedista")
    labels_data = cursor.fetchall()
    for row_data in labels_data:
        row = row_data[0]
        col = row_data[1]
        color = row_data[2]
        grid[row][col].configure(bg=color)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            seat_id = (row, col)
            seat_label = grid[row][col]
            seat_label.bind("<Button-1>", lambda event, seat_id=seat_id, seat_label=seat_label: on_click(event, seat_id, seat_label))
    def list():
        labels_list = []
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                bg_color = grid[row][col].cget("background")
                if bg_color == "black":
                    labels_list.append((row, col, "black"))
                elif bg_color == "lightblue":
                    labels_list.append((row, col, "lightblue"))
                elif bg_color == "red":
                    labels_list.append((row, col, "red"))
                elif bg_color == "yellow":
                    labels_list.append((row, col, "yellow"))
        cursor.executemany("INSERT INTO sedista VALUES (?,?,?)", labels_list) 

        
    list()




    root.mainloop()

    connection.commit()
    connection.close()
