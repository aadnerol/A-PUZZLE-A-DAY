from __future__ import annotations

Coord = tuple[int, int]
Shape = frozenset[Coord]

PIECES: dict[str, Shape] = {
    "A": frozenset({
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 2),
    }),
    "B": frozenset({
        (0, 0), (0, 1),
        (1, 1),
        (2, 1), (2, 2),
    }),
    "C": frozenset({
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1),
    }),
    "D": frozenset({
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
    }),
    "E": frozenset({
        (0, 0), (0, 1), (0, 2),
        (1, 0), 
        (2, 0),
    }),
    "F": frozenset({
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0),
    }),
    "G": frozenset({
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 1),
    }),
    "H": frozenset({
        (0, 0), (0, 1),
        (1, 1), (1, 2), (1, 3),
    }),
}

def get_piece(name: str) -> Shape:
    return PIECES[name]

def all_pieces() -> dict[str, Shape]:
    return PIECES.copy()
