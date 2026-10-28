# Note Player

Parses a melody from a plain-text file into `Note` objects and plays it through your speakers with [`musicalbeeps`](https://pypi.org/project/musicalbeeps/).

Built as a university Python course assignment.

## Tech stack

Python 3, `musicalbeeps` (which uses `numpy` and `simpleaudio`).

## What's interesting

- **`Note` class:**
  - Validates its arguments: duration, pitch `A`–`G` or `R` for a rest, octave 1–7, and accidental.
  - Converts itself to the note format `musicalbeeps` expects.
- **`Melody` parser:**
  - Reads the title, author and note lines.
  - Expands **repeated sections**: notes flagged `true` mark where a section starts and ends, and the section is played twice.
- **Transformations:**
  - `change_tempo(factor)` scales every duration.
  - `upper_octave()` and `lower_octave()` shift the whole melody, refusing if any note would leave octaves 1–7.
  - `get_total_duration()` sums the note lengths.

## Melody file format

```
Hot Cross Buns          <- title
Traditional             <- author
0.5 B 4 NATURAL true    <- duration pitch octave accidental repeat-flag
0.5 A 4 NATURAL false
...
```

## Running it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python play.py                    # plays hotcrossbuns.txt
python play.py my_song.txt        # or any file in the format above
```

Example: parsing without playing.

```python
>>> from Melody import Melody
>>> m = Melody('hotcrossbuns.txt')
>>> m.title, m.author, len(m.notes), m.get_total_duration()
('Hot Cross Buns', 'Traditional', 17, 8.0)
```

## Known issues

- Rests always last 0.5 s, whatever duration is written in the file.
- Some docstring examples refer to melody files that aren't included (`tetris.txt`, `twinkle.txt`).
