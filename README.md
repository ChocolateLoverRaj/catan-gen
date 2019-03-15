# Catan Board Generator
Generator for a mathematically fair, randomized board setup for Settlers of Catan.

## Usage

Simply run the `catan_gen.py` Python script from terminal.  A REPL will prompt user for board parameters/presets.

`> python catan_gen.py`

### Key

```
H : hill
P : pasture
M : mountain
W : field
F : forest
D : desert
- : sea
```

Numbers are represented in hexadecimal.

### Example Output

Normal (4-player)
```
================
Max variety 0.20212765957446807
Max numbers 7.163628472222222
Max value 3.0
Max redundency 4
================
 - - - - - - -
- - F P W - -
 - W H F M - -
- M P W P F -
 - F H D H - -
- - M P W - -
 - - - - - - -
================
 - - - - - - -
- - 6 4 9 - -
 - 5 3 2 8 - -
- C A 4 B A -
 - 8 B - 9 - -
- - 3 5 6 - -
 - - - - - - -
================
Variety Score: 0.15079365079365079
Value Score: 2.6666666666666665
Numbers Score: 6.267361111111111
Redundency Score: 4
Normalized Score: 11.608169427191164
Num Adj Score: 0
Hex Adj Score: 0
Resource Score: 6.638888888888888
================
```

## Presets

There are currently 4 available presets from the Seafarers Expansion:
- Normal
- New Shores
- Four Islands
- Fog Islands
