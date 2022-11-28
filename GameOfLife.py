import numpy as np
import tkinter as tk


class GameOfLife():
    """Implentation of the Conway's Game of Life
    """
    
    
    def __init__(self, epochs:int, n_cells:int=20, windows_size:int=600) -> None:
        """Initialize the game
        :param int n_cells: The number of cells in a width/height, default 20
        :param int windows_size: The width & height windows size (in pixel), default 600
        :param int epochs: The number of epoch to do, default 10
        """
        
        self.crt_epoch = 0
        self.epochs = epochs
        self.all_dead = False
        self.windows_width = windows_size
        self.windows_heigth = windows_size
        self.colors = {0: "white", 1: "black"}
        
        self.init_window()
        self.info = tk.StringVar()
        self.info.set('WELCOME')
        self.init_board(n_cells, n_cells)
        self.init_menu()
        self.show_board()
        

    def init_window(self) -> None:
        """Initialize the main windows
        """

        self.root = tk.Tk('GameOfLife')
        self.root.title('GameOfLife')
        
        x = int((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2)
        y = int((self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2)

        self.root.geometry(f"{self.windows_heigth}x{self.windows_width}+{x}+{y}")
        self.root.resizable(width=False, height=False)


    def init_board(self, height:int, width:int) -> None:
        """Create the board view and logic
        
        Parameters:
        ------------
        :param int height: The number of cells we can put in the height of the board
        :param int width: The number of cells we can put in the width of the board
        """
        
        # compute the canva and the cell size

        self.cell_width = self.windows_width // width
        board_canva_w = width * self.cell_width

        free_space = 60
        self.cell_height = (self.windows_heigth - free_space) // height
        board_canva_h = height * self.cell_height

        self.board = np.zeros((height, width), dtype=int)

        self.board_canva = tk.Canvas(width=board_canva_w, height=board_canva_h)
        self.board_canva.place(x=0, y=free_space)


    def init_menu(self):
        """Create the basic button in the menu of the game
        """
        self.board_canva.bind("<Button-1>", self.event_hdlr)
        launch_btn = tk.Button(self.root, text='GO', width=4, 
                               height=2, command=self.launch_simulation)
        launch_btn.place(x=10, y=10)

        reset_btn = tk.Button(self.root, text='RESET', width=8, 
                              height=2, command=self.reset)
        reset_btn.place(x=self.windows_width - 80, y=10)

        text_info = tk.Label(self.root, textvariable=self.info, height=2, width=50)
        text_info.place(x=self.windows_width // 2 - 190, y=10)
        

    def event_hdlr(self, evt:tk.Event) -> None:
        """Raised on mouse click and create a cell where
        the mouse is

        :param tk.Event evt: The mouse event
        """

        x = int(evt.x / self.cell_width)
        y = int(evt.y / self.cell_height)
    
        self.board[x, y] = 0 if self.board[x, y] else 1
        x1 = x * self.cell_width
        y1 = y * self.cell_height
        x2 = (x + 1) * self.cell_width
        y2 = (y + 1) * self.cell_height
        self.board_canva.create_rectangle(x1, y1, x2, y2, fill=self.colors[self.board[x, y]])


    def show_board(self) -> None:
        """Display the different cells on the board
        """
        self.board_canva.delete('all')
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                x1 = i * self.cell_width
                y1 = j * self.cell_height
                x2 = (i + 1) * self.cell_width
                y2 = (j + 1) * self.cell_height
                self.board_canva.create_rectangle(x1, y1, x2, y2, fill=self.colors[self.board[i, j]])

    
    def reset(self) -> None:
        """Reset the game
        """
        self.board_canva.delete('all')
        self.board = np.zeros(self.board.shape, dtype=int)
        self.crt_epoch = 0
        self.all_dead = False
        self.show_board()


    def launch_simulation(self) -> None:
        """Launch the simulation for a given number of epochs
        """
        if self.crt_epoch < self.epochs and not self.all_dead:
            self.info.set(f"Epoch n°{self.crt_epoch+1}/{self.epochs}")
            self.next_epoch()
            self.show_board()
            self.crt_epoch += 1
            self.root.after(100, self.launch_simulation)
        else:
            info = "Simulation finished!"
            if self.all_dead:
                info = f"All cells are dead\n{info}"
                self.info.set(' 💡 All cells are dead')
            self.info.set(info)
            self.reset()
        

    def next_epoch(self) -> None:
        """Apply the different rules inorder to
        make the cells evolve to the next epoch
        """

        all_dead = True
        next_epoch_board = np.zeros(self.board.shape, dtype=int)
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                next_epoch_board[i, j] = self.get_new_state(i, j)
                if self.board[i, j]:
                    all_dead = False
        self.all_dead = all_dead
        self.board = next_epoch_board


    def get_neighbors(self, i:int, j:int) -> int:
        """Apply the rule n°1 to the cell at the given position

        :param int i: the x index of the cell
        :param int j: the y index of the cell
        :return int: The number of neighbors
        """
        
        x_start = i - 1 if i > 0 else i
        x_end = i + 2 if i < self.board.shape[0] - 1 else i + 1

        y_start = j - 1 if j > 0 else j
        y_end = j + 2 if j < self.board.shape[1] - 1 else j + 1

        neighbors = self.board[x_start:x_end, y_start:y_end]
        n_neighbords = np.sum(neighbors) - self.board[i, j]
            
        return n_neighbords


    def get_new_state(self, i:int, j:int) -> int:
        """Return the new state of a cell given its numer
        of current neighbors

        :param int i: the x index of the cell
        :param int j: the y index of the cell
        :return int: 1 if the cell is alive 0 either
        """
        n_neighbors = self.get_neighbors(i, j)

        if n_neighbors < 2 or n_neighbors > 3:
            state = 0
        elif n_neighbors == 3:
            state = 1
        else:
            state = self.board[i, j]
        return state



        


if __name__ == "__main__":
    game = GameOfLife(epochs=100, n_cells=30, windows_size=700)
    game.root.mainloop()
