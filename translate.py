from googletrans import Translator
import sys

def translate_text(input_file, output_file, target_language):
    # Read the content from the input text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Create a Translator object
    translator = Translator()

    # Translate the text to the target language
    translated = translator.translate(text, dest=target_language)

    # Write the translated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated.text)

    print(f"Translation complete. Translated text saved to {output_file}")

if __name__ == "__main__":
    input_file = f"{sys.argv[1]}.txt"        # Path to your input text file
    output_file = f"{sys.argv[2]}.txt"      # Desired name for the output translated text file
    target_language = f"{sys.argv[3]}"          # Target language code (e.g., "fr" for French)

    translate_text(input_file, output_file, target_language)
