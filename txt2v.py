from text_to_speech import save
import playsoundsimple as p
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-t", "--text", dest="text", help="Input string")
parser.add_argument("-l", "--lang", dest="lang", help="Language of the input string")
parser.add_argument("-o", "--outputfile", dest="output", help="Output file")
parser.add_argument("-p", "--play", dest="playsound", help="Flag to play the produced mp3 file.")

options = parser.parse_args()


save(options.text, options.lang, file=f"{options.output}.mp3")

if options.playsound:
    sound = p.Sound(f"{options.output}.mp3")
    sound.play(1)
    sound.wait()

    

