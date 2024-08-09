import tkinter as tk
from tkinter import messagebox
import requests

class GameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Tic-Tac-Toe Game", font=("Arial", 24))
        self.label.pack(pady=20)

        self.leaderboard_button = tk.Button(self.window, text="View Leaderboard", command=self.view_leaderboard)
        self.leaderboard_button.pack(pady=10)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack(pady=10)

    def view_leaderboard(self):
        leaderboard_window = tk.Toplevel(self.window)
        leaderboard_window.title("Leaderboard")

        leaderboard_data = requests.get("http://localhost:5000/leaderboard").json()
        for index, entry in enumerate(leaderboard_data):
            tk.Label(leaderboard_window, text=f"{index+1}. {entry['username']} - {entry['wins']} wins").pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GameGUI()
    game.run()
