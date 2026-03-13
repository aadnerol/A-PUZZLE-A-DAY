from board import Coord, build_target_board
from pieces import Shape, all_pieces
from geometry import all_orientations, translate

def is_within_board(shape: Shape, board: set[Coord]) -> bool:
    """Check if shape is within board."""
    return shape <= board

def generate_placements_for_piece(piece: Shape, board: set[Coord]) -> set[Shape]:
    """Returnerer alle mulige plasseringer til en brikke på et brett."""
    placements: set = set()
    for oriented in all_orientations(piece):
        for br, bc in board:
            moved = translate(oriented, br, bc)
            if is_within_board(moved, board):
                placements.add(moved)
    return placements


def generate_all_placements(board: set[Coord]) -> dict[str, set[Shape]]:
    "Returnerer alle lovlige plasseringer for alle brikker."
    return {
        name: generate_placements_for_piece(piece, board)
        for name, piece in all_pieces().items()
    }

def solve(
    board: set[Coord],
    placements: dict[str, set[Shape]],
    remaining: set[str] | None = None,
    solution: dict[str, Shape] | None = None,
) -> dict[str, Shape] | None:
    if remaining is None:
        remaining = set(placements.keys())

    if solution is None:
        solution = {}

    if not remaining:
        return solution.copy()

    piece_name = next(iter(remaining))

    for placement in placements[piece_name]:
        if placement <= board:
            solution[piece_name] = placement
            result = solve(
                board - placement,
                placements,
                remaining - {piece_name},
                solution,
            )
            if result is not None:
                return result
            del solution[piece_name]

    return None
