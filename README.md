# A-Puzzle-A-Day Solver

Et lite Python-prosjekt som finner en løsning på kalenderpuslespillet **A-Puzzle-A-Day** fra DragonFjord.

Programmet tar inn en **måned og en dag**, og finner en måte å plassere de 8 brikkene slik at akkurat denne datoen blir synlig på brettet.

---

# Oversikt over repoet

Prosjekt-koden er delt opp i følgende filer, under mappen **code**:

## `board.py`

Beskriver kalenderbrettet.

Inneholder:

* `LAYOUT`
  2D-struktur som beskriver brettets form og hvor måneder/dager ligger.

* `BASE_BOARD`
  Alle gyldige koordinater på brettet.

* `MONTH_CELLS`
  Mapping fra måned → koordinat.

* `DAY_CELLS`
  Mapping fra dag → koordinat.

Funksjoner:

* `normalize_month(month)`
  Normaliserer månedsinput (norsk, engelsk, tall).

* `get_month_cell(month)`
  Returnerer koordinaten til måneden.

* `get_day_cell(day)`
  Returnerer koordinaten til dagen.

* `build_target_board(month, day)`
  Lager brettet som skal dekkes av brikkene.

---

## `pieces.py`

Definerer puslespillbrikkene.

Typer:

* `Coord`
* `Shape`

Variabler:

* `PIECES`
  Alle brikkene definert som relative koordinater.

Funksjoner:

* `get_piece(name)`
* `all_pieces()`

---

## `geometry.py`

Funksjoner for å transformere brikker.

Funksjoner:

* `normalize(shape)`
  Flytter en shape slik at minste rad/kolonne er `(0,0)`.

* `translate(shape, dr, dc)`
  Flytter en shape på brettet.

* `rotate(shape)`
  Roterer shape 90°.

* `reflect(shape)`
  Speiler shape.

* `all_orientations(shape)`
  Genererer alle unike rotasjoner og speilinger.

---

## `solver.py`

Selve løseren.

Funksjoner:

* `is_within_board(shape, board)`
  Sjekker om en shape ligger innenfor brettet.

* `generate_placements_for_piece(piece, board)`
  Genererer alle gyldige plasseringer for én brikke.

* `generate_all_placements(board)`
  Genererer plasseringer for alle brikker.

* `solve(board, placements)`
  Backtracking-algoritme som finner en løsning.

* `solve_date(month, day)`
  Hjelpefunksjon som løser en spesifikk dato.

---

## `visualize.py`

Funksjoner for å vise løsninger.

Funksjoner:

* `print_solution(solution)`
  Skriver løsningen som tekst.

* `plot_solution(solution)`
  Visualiserer løsningen med `matplotlib`.

---

# Notebook

Repoet inneholder også en **Jupyter Notebook** som samler hele prosjektet i én fil.

Notebooken:

* tar inn måned og dag
* finner en løsning
* viser resultatet grafisk
* Mulighet for å lagre løsningen

---

# Kort forklaring av algoritmen

1. Brettet genereres for en valgt dato.
2. Alle mulige plasseringer av hver brikke beregnes.
3. En **backtracking-algoritme** prøver å plassere brikkene én etter én.
4. Når alle brikker er plassert uten overlapp er en løsning funnet.

---
# Videre arbeid

1. Finne alle mulige løsninger for hver dato.
2. Utforske hvilke datoer som har flest løsninger.
3. Utforske om det finnes "umulige" datoer uten løsning. 
- Eksempel: 31. februar
4. Optimalisere med raskere løsningsalgoritmer.
5. Nettside/app som gir figur med løsning 

---
