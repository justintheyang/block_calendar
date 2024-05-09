import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, Normalize

class PuzzleGrid:
    def __init__(self, month, date):
        self.grid_size = 7
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.blocked_cells = [(6, 0), (6, 1), (0, 6), (1, 6), (5, 6), (6, 6)]
        self.month_dict = {
            "January": (0, 0), "February": (1, 0), "March": (2, 0), "April": (3, 0),
            "May": (4, 0), "June": (5, 0), "July": (0, 1), "August": (1, 1),
            "September": (2, 1), "October": (3, 1), "November": (4, 1), "December": (5, 1)
        }
        self.date_dict = {str(i): ((i-1) % 7, 2 + (i-1) // 7) for i in range(1, 32)}

        # Initialize grid
        for x, y in self.blocked_cells:
            self.grid[y, x] = -1  # Mark blocked cells
        if month in self.month_dict:
            mx, my = self.month_dict[month]
            self.grid[my, mx] = -1
        if date in self.date_dict:
            dx, dy = self.date_dict[date]
            self.grid[dy, dx] = -1

    def is_free(self, x, y):
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size and self.grid[y, x] == 0
    
    def place_piece(self, piece, piece_id, x, y):
        """Place a piece with an identifier piece_id for color coding."""
        if all(self.is_free(x + dx, y + dy) for dx, dy in piece.cells):
            for dx, dy in piece.cells:
                self.grid[y + dy, x + dx] = piece_id  # Use piece_id instead of 1
            return True
        return False

    def remove_piece(self, piece, x, y):
        for dx, dy in piece.cells:
            if 0 <= x + dx < self.grid_size and 0 <= y + dy < self.grid_size:
                self.grid[y + dy, x + dx] = 0  # Reset the cell to free

    def visualize_grid(self):
        """Use a colormap to represent different pieces."""
        fig, ax = plt.subplots(figsize=(7, 7))
        base_cmap = plt.cm.get_cmap('tab20', 20)
        colors = base_cmap(np.arange(20))
        colors[0] = np.array([0.5, 0.5, 0.5, 1])  # Set grey for the blocked cells (-1 index)
        custom_cmap = ListedColormap(colors)
        norm = Normalize(vmin=-1, vmax=19)
        ax.imshow(self.grid, cmap=custom_cmap, norm=norm)

        # Draw grid lines
        ax.set_xticks(np.arange(self.grid_size) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.grid_size) - 0.5, minor=True)
        ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
        ax.tick_params(which='minor', size=0)

        # Set limits and aspect
        ax.set_xlim(-0.5, self.grid_size - 0.5)
        ax.set_ylim(-0.5, self.grid_size - 0.5)
        ax.set_aspect('equal')
        ax.invert_yaxis()  # Invert the y-axis to match the coordinate system
        plt.show()

class PuzzleSolver:
    def __init__(self, grid, pieces):
        self.grid = grid
        self.pieces = pieces
        self.solutions = []
    
    def solve(self):
        # This method will implement the backtracking algorithm to find solutions
        pass  # Algorithm X logic will go here
    
    def find_valid_placements(self, piece):
        # Check all positions on the grid for valid placements of the piece
        valid_placements = []
        for y in range(self.grid.grid_size):
            for x in range(self.grid.grid_size):
                if self.can_place(piece, x, y):
                    valid_placements.append((x, y))
        return valid_placements
    
    def can_place(self, piece, x, y):
        # Check if piece can be placed at (x, y)
        return all(self.grid.is_free(x + dx, y + dy) for dx, dy in piece.cells)

