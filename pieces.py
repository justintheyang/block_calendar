import matplotlib.pyplot as plt

class Piece:
    def __init__(self, cells):
        self.base_cells = cells  # Original shape
        self.cells = cells.copy()  # Active configuration of cells
        self.configurations = self.generate_configurations()
    

    def rotate(self):
        """Rotate the piece 90 degrees clockwise and reposition."""
        self.cells = [(dy, -dx) for dx, dy in self.cells]
        self.reposition()
        return self

    def reflect(self):
        """Reflect the piece horizontally and reposition."""
        self.cells = [(-dx, dy) for dx, dy in self.cells]
        self.reposition()
        return self

    def reposition(self):
        """Reposition the piece to ensure all coordinates are non-negative and normalized."""
        if not self.cells:
            return
        min_x = min(x for x, y in self.cells)
        min_y = min(y for x, y in self.cells)
        self.cells = [(x - min_x, y - min_y) for x, y in self.cells]

    def reset(self):
        """Reset to the original configuration."""
        self.cells = self.base_cells.copy()
        return self
    
    def generate_configurations(self):
        """Generate and return all unique configurations."""
        configs = set()
        self.reset()
        for _ in range(4):
            current = tuple(self.cells)
            configs.add(current)
            self.reflect()
            configs.add(tuple(self.cells))
            self.reflect()
            self.rotate()
        self.reset()
        return [list(config) for config in configs]
    
    def visualize_configurations(self):
        unique_configs = {tuple(config) for config in self.configurations}
        fig, axes = plt.subplots(1, len(unique_configs), figsize=(len(unique_configs)*3, 3))
        if len(unique_configs) == 1:
            axes = [axes]  # Make sure axes is iterable
        
        for ax, config in zip(axes, unique_configs):
            ax.set_aspect('equal')
            ax.set_xticks([])
            ax.set_yticks([])
            min_x = min(x for x, y in config)
            max_x = max(x for x, y in config)
            min_y = min(y for x, y in config)
            max_y = max(y for x, y in config)
            ax.set_xlim(min_x - 1, max_x + 1)
            ax.set_ylim(min_y - 1, max_y + 1)
            grid = set(config)
            for x, y in grid:
                ax.add_patch(plt.Rectangle((x-0.5, y-0.5), 1, 1, fill=True, color="blue"))
            ax.axis('off')
        plt.tight_layout()
        plt.show()

class PieceA(Piece):
    """Piece A: 2x2 square"""
    def __init__(self):
        super().__init__([
            (0, 0), (1, 0), 
            (0, 1), (1, 1)
                         ])

class PieceB(Piece):
    """Piece B: cross shape"""
    def __init__(self):
        super().__init__([
                    (1, 0), 
            (0, 1), (1, 1), (2, 1), 
                    (1, 2)
                        ])
        
class PieceC(Piece):
    """Piece C: C shape"""
    def __init__(self):
        super().__init__([
            (0, 0), (1, 0),
            (0, 1), 
            (0, 2), (1, 2)
                        ])

class PieceD(Piece):
    """Piece D: Long elbow shape"""
    def __init__(self):
        super().__init__([
                            (2, 0),
            (0, 1), (1, 1), (2, 1), 
            (0, 2),
                        ])

class PieceE(Piece):
    """Piece E: Short elbow shape"""
    def __init__(self):
        super().__init__([
                    (1, 0),
            (0, 1), (1, 1),
            (0, 2)
                        ])

class PieceF(Piece):
    """Piece F: tetris shape"""
    def __init__(self):
        super().__init__([
            (0, 0),
            (0, 1), (1, 1),
            (0, 2),
                        ])

class PieceG(Piece):
    """Piece G: Square + 1 shape"""
    def __init__(self):
        super().__init__([
            (0, 0), (1, 0),
            (0, 1), (1, 1), 
            (0, 2),
                        ])

class PieceH(Piece):
    """Piece H: L shape"""
    def __init__(self):
        super().__init__([
            (0, 0), (1, 0),
            (0, 1), 
            (0, 2),
                        ])

class PieceI(Piece):
    """Piece I: Long L shape"""
    def __init__(self):
        super().__init__([
            (0, 0), (1, 0),
            (0, 1), 
            (0, 2),
            (0, 3),
                        ])