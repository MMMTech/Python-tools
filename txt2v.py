import sys
import os
from text_to_speech import save
import playsoundsimple as p

try:
    save(f"{sys.argv[1]}", f"{sys.argv[3]}", file=f"{sys.argv[2]}.mp3")

    if sys.argv[4] == "1":
        sound = p.Sound(f"{sys.argv[2]}.mp3")
        sound.play(1)
        sound.wait()

except:
    print("Usage: python txt2v.py 'text to be converted into mp3' 'outputfile' 'language ((IETF language tag - ex: en | da ...)' 0|1 (muted|speak) ")
    

