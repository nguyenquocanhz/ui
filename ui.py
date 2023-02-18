import tkinter as tk

class GameMenu:
    def __init__(self, master):
        self.master = master
        master.title("Game Menu")

        # Tạo danh sách các game
        self.game_list = ["Tic Tac Toe", "Hangman", "Minesweeper", "Snake"]

        # Tạo Label để hiển thị danh sách các game
        self.label = tk.Label(master, text="Select a game to play:")
        self.label.pack()

        # Tạo ListBox để hiển thị danh sách các game
        self.gameListBox = tk.Listbox(master)
        for game in self.game_list:
            self.gameListBox.insert(tk.END, game)
        self.gameListBox.pack()

        # Tạo Button để bắt đầu chơi game
        self.playButton = tk.Button(master, text="Play", command=self.start_game)
        self.playButton.pack()

    def start_game(self):
        # Lấy tên game được chọn
        selected_game = self.gameListBox.get(self.gameListBox.curselection())

        # Chuyển sang giao diện game tương ứng
        if selected_game == "Tic Tac Toe":
            # Chuyển sang giao diện Tic Tac Toe
            pass
        elif selected_game == "Hangman":
            # Chuyển sang giao diện Hangman
            pass
        elif selected_game == "Minesweeper":
            # Chuyển sang giao diện Minesweeper
            pass
        elif selected_game == "Snake":
            # Chuyển sang giao diện Snake
            pass

root = tk.Tk()
my_game_menu = GameMenu(root)
root.mainloop()
