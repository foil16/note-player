import sys
import musicalbeeps
from Melody import Melody

# Usage: python play.py [melody_file]
filename = sys.argv[1] if len(sys.argv) > 1 else 'hotcrossbuns.txt'
mel = Melody(filename)
print(mel.title, '-', mel.author)
mel.play(musicalbeeps.Player(volume=0.3))
