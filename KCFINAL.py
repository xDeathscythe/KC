import tkinter as tk
import sqlite3

class Seat:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

class SeatingProgram:
    
    import tkinter as tk
    import sqlite3
        
    

    def __init__(self, event_name):
        self.event_name = event_name
        self.GRID_ROWS = 15
        self.GRID_COLS = 73
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.seats = {(row, col): 0 for row in range(self.GRID_ROWS) for col in range(self.GRID_COLS)}
        self.grid = []
        self.connection = sqlite3.connect("sedista.db")
        self.cursor = self.connection.cursor()
        self.table = self.cursor.execute("CREATE TABLE IF NOT EXISTS sedista (row integer, col integer,color string)")
        self.root = tk.Tk()
        self.root.geometry(f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}")
        self.root.attributes("-fullscreen", True)
        self.root.resizable(False, False)
        self.root.title("Selektor Sedišta")
        self.root.configure(bg="black")
        
    def setup_grid(self):
        for row in range(self.GRID_ROWS):
            row_labels = []
            for col in range(self.GRID_COLS):
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
                label = tk.Label(self.root, text=(), borderwidth=1, relief="solid", width=3, height=2, bg=bg_color)
                label.grid(row=row, column=col)
                row_labels.append(label)
            self.grid.append(row_labels)
            
    def on_click(self, event, seat_id, seat_label):
        current_color = seat_label.cget("background")
        if current_color == "":
            return
        if current_color == "lightblue":
            seat_label.configure(bg="red")  # change to yellow for reserved seats
            self.seats[seat_id] = 2
        elif current_color == "red":
            seat_label.configure(bg="yellow")  # change to red for occupied seats
            self.seats[seat_id] = 1
        elif current_color == "yellow":
            seat_label.configure(bg="lightblue")  # change to red for occupied seats
            self.seats[seat_id] = 0
        self.list()

    def bind_click_events(self):
        for row in range(self.GRID_ROWS):
            for col in range(self.GRID_COLS):
                seat_id = (row, col)
                seat_label = self.grid[row][col]
                seat_label.bind("<Button-1>", lambda event, seat_id=seat_id, seat_label=seat_label: self.on_click(event, seat_id, seat_label))

    def populate_from_db(self):
        self.cursor.execute("SELECT row, col, color FROM sedista")
        labels_data = self.cursor.fetchall()
        for row_data in labels_data:
            row = row_data[0]
            col = row_data[1]
            color = row_data[2]
            self.grid[row][col].configure(bg=color)

    def list(self):
        labels_list = []
        for row in range(self.GRID_ROWS):
            for col in range(self.GRID_COLS):
                bg_color = self.grid[row][col].cget("background")
                if bg_color == "black":
                    labels_list.append((row, col, "black"))
                elif bg_color == "lightblue":
                    labels_list.append((row, col, "lightblue"))
                elif bg_color == "red":
                    labels_list.append((row, col, "red"))
                elif bg_color == "yellow":
                    labels_list.append((row, col, "yellow"))
        self.cursor.executemany("INSERT INTO sedista VALUES (?,?,?)", labels_list) 
        
    def run(self, event_name):
        self.setup_grid()
        self.bind_click_events()
        self.populate_from_db()
        self.root.mainloop()
        self.connection.commit()
        self.connection.close()
        self.event_name = event_name

def main():
    event_name="My Event"
    seating_program = SeatingProgram(event_name)
    seating_program.run(event_name)

if __name__ == "__main__":
    main()