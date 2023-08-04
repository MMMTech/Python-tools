# Import the necessary libraries
from gtts import gTTS
import os
import sys

# Define a function to convert text to speech and save as an MP3 file
def text_to_speech(input_file, output_file):
    # Read the content from the input text file
    with open(input_file, 'r') as file:
        text = file.read()

    # Create a gTTS object and generate the speech from the text
    tts = gTTS(text)

    # Save the generated speech as an MP3 file
    tts.save(output_file)

    # Print a message indicating successful conversion and saving
    print(f"Text converted and saved as {output_file}")

# Entry point of the script
if __name__ == "__main__":
    # Change these paths to match your input text file and desired output MP3 file
    input_file = f"{sys.argv[1]}.txt"       # Path to your input text file
    output_file = f"{sys.argv[2]}.mp3"     # Desired name for the output MP3 file

    # Call the text_to_speech function with the specified input and output files
    text_to_speech(input_file, output_file)
