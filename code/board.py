from __future__ import annotations
from typing import Final

Coord = tuple[int, int]

# Board Layout 
BASE_BOARD: Final[set[Coord]] = {
    # Months
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    # Days
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
    (6, 0), (6, 1), (6, 2),
}

MONTH_CELLS: Final[dict[str, Coord]] = {
    "jan": (0, 0), 
    "feb": (0, 1), 
    "mar": (0, 2), 
    "apr": (0, 3), 
    "may": (0, 4), 
    "jun": (0, 5),
    "jul": (1, 0), 
    "aug": (1, 1), 
    "sep": (1, 2), 
    "oct": (1, 3), 
    "nov": (1, 4), 
    "dec": (1, 5),
}

DAY_CELLS: Final[dict[int, Coord]] = {
    1: (2, 0), 2: (2, 1), 3: (2, 2), 4: (2, 3), 5: (2, 4), 6: (2, 5), 7: (2, 6),
    8: (3, 0), 9: (3, 1), 10: (3, 2), 11: (3, 3), 12: (3, 4), 13: (3, 5), 14: (3, 6),
    15: (4, 0), 16: (4, 1), 17: (4, 2), 18: (4, 3), 19: (4, 4), 20: (4, 5), 21: (4, 6),
    22: (5, 0), 23: (5, 1), 24: (5, 2), 25: (5, 3), 26: (5, 4), 27: (5, 5), 28: (5, 6),
    29: (6, 0), 30: (6, 1), 31: (6, 2),
}

def normalize_month(month: str | int) -> str:
    month_numbers = {
        1: "jan",
        2: "feb",
        3: "mar",
        4: "apr",
        5: "may",
        6: "jun",
        7: "jul",
        8: "aug",
        9: "sep",
        10: "oct",
        11: "nov",
        12: "dec",
    }

    month_aliases = {
        "jan": "jan",
        "january": "jan",
        "januar": "jan",

        "feb": "feb",
        "february": "feb",
        "februar": "feb",

        "mar": "mar",
        "march": "mar",
        "mars": "mar",

        "apr": "apr",
        "april": "apr",

        "may": "may",
        "mai": "may",

        "jun": "jun",
        "june": "jun",
        "juni": "jun",

        "jul": "jul",
        "july": "jul",
        "juli": "jul",

        "aug": "aug",
        "august": "aug",

        "sep": "sep",
        "sept": "sep",
        "september": "sep",

        "oct": "oct",
        "okt": "oct",
        "october": "oct",
        "oktober": "oct",

        "nov": "nov",
        "november": "nov",

        "dec": "dec",
        "des": "dec",
        "december": "dec",
        "desember": "dec",
    }

    if isinstance(month, int):
        if month not in month_numbers:
            raise ValueError(f"Invalid month number: {month}")
        return month_numbers[month]

    value = month.strip().lower()

    if value.isdigit():
        month_num = int(value)
        if month_num not in month_numbers:
            raise ValueError(f"Invalid month number: {month}")
        return month_numbers[month_num]

    if value not in month_aliases:
        raise ValueError(f"Unknown month: {month!r}")

    return month_aliases[value]


def get_month_cell(month: str|int) -> Coord:
    key = normalize_month(month)
    return MONTH_CELLS[key]

def get_day_cell(day: int | str) -> Coord:
    if isinstance(day, str):
        day = day.strip()

        if not day.isdigit():
            raise ValueError(f"Invalid day: {day}")

        day = int(day)

    if day not in DAY_CELLS:
        raise ValueError(f"Day not on board: {day}")

    return DAY_CELLS[day]

def build_target_board(month: str|int, day: int|str) -> set[Coord]:
    month_cell = get_month_cell(month)
    day_cell = get_day_cell(day)
    return BASE_BOARD - {month_cell, day_cell}

LAYOUT = [
    ["Jan","Feb","Mar","Apr","May","Jun", None],
    ["Jul","Aug","Sep","Oct","Nov","Dec", None],
    ["1","2","3","4","5","6","7"],
    ["8","9","10","11","12","13","14"],
    ["15","16","17","18","19","20","21"],
    ["22","23","24","25","26","27","28"],
    ["29","30","31", None, None, None, None],
]