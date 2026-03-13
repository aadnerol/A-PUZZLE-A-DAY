import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from board import LAYOUT
from pieces import Shape


def print_solution(solution: dict[str, Shape]) -> None:
    grid = {}

    for name, shape in solution.items():
        for cell in shape:
            grid[cell] = name

    for r, row in enumerate(LAYOUT):
        line = ""
        for c, cell in enumerate(row):
            if cell is None:
                line += "   "
            else:
                line += f"{grid.get((r,c),'.'):>2} "
        print(line)

def plot_solution(solution):
    rows = len(LAYOUT)
    cols = max(len(row) for row in LAYOUT)

    grid = {}
    for name, shape in solution.items():
        for cell in shape:
            grid[cell] = name

    cmap = plt.get_cmap("tab20")
    piece_colors = {
        name: cmap(i % 20)
        for i, name in enumerate(sorted(solution.keys()))
    }

    fig, ax = plt.subplots(figsize=(8, 8))

    # draw piece cells
    for name, shape in solution.items():
        color = piece_colors[name]

        for r, c in shape:
            y = rows - 1 - r

            rect = Rectangle(
                (c, y),
                1,
                1,
                facecolor=color,
                edgecolor="black",
                linewidth=2
            )
            ax.add_patch(rect)

    # draw remaining calendar cells (month/day)
    for r, row in enumerate(LAYOUT):
        for c, cell in enumerate(row):
            if cell is None:
                continue

            if (r, c) in grid:
                continue

            y = rows - 1 - r

            rect = Rectangle(
                (c, y),
                1,
                1,
                facecolor="white",
                edgecolor="black",
                linewidth=1
            )
            ax.add_patch(rect)

            ax.text(
                c + 0.5,
                y + 0.5,
                str(cell),
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold"
            )

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.show()
