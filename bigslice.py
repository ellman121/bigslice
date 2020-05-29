import sys
import pydub
from metadata import DATA

segment = pydub.AudioSegment.from_mp3(sys.argv[1])

for cur, nxt in zip(DATA[:-1], DATA[1:]):
    segment[cur[2]*1000:nxt[2]*1000-1].export(
        f'{cur[0]}_{cur[1]}.mp3',
        format="mp3",
        tags={"title": cur[0], "artist": cur[1]}
    )

fin = DATA[-1]
segment[fin[2]*1000:].export(
        f'{fin[0]}_{fin[1]}.mp3',
        format="mp3",
        tags={"title": fin[0], "artist": fin[1]}
    )
