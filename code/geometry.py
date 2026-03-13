from __future__ import annotations

Coord = tuple[int, int]
Shape = frozenset[Coord]


def normalize(shape: Shape) -> Shape:
    """Normaliserer brikker. Plasserer i (0, 0) med riktig orientering.
    """
    min_r = min(r for r, _ in shape)
    min_c = min(c for _, c in shape)

    return frozenset(
        (r - min_r, c - min_c)
        for r, c in shape
    )

def rotate(shape: Shape) -> Shape:
    """Roterer brikke 90 grader med klokka."""
    rotated = frozenset((c, -r) for r, c in shape)
    return normalize(rotated)


def reflect(shape: Shape) -> Shape:
    """Speiler brikke om vertikal akse."""
    reflected = frozenset(
        (r, -c)
        for r, c in shape
    )

    return normalize(reflected)

def all_orientations(shape: Shape) -> set[Shape]:
    """Gir mengden av alle mulige orienteringer til en brikke."""
    orientations: set[Shape] = set()

    current = normalize(shape)
    for _ in range(4):
        orientations.add(current)
        current = rotate(current)

    current = reflect(shape)
    for _ in range(4):
        orientations.add(current)
        current = rotate(current)

    return orientations

def translate(shape: Shape, dr: int, dc: int) -> Shape:
    """Funksjon som flytter brikker."""
    return frozenset(
        (r + dr, c + dc)
        for r, c in shape
    )
    

    