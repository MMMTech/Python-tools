from gtts import gTTS
import fitz  # PyMuPDF
import os

class PDFTool:

    def __init__(self, file_path, output_folder):
        self.file_path = file_path
        self.output_folder = output_folder

    def extract_text_from_pdf(self, pdf_path, output_folder):
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        
        # Iterate through each page in the PDF
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            
            # Extract text from the page
            text = page.get_text("text")
            
            # Save text to a text file
            text_filename = os.path.join(output_folder, f"page_{page_num + 1}_text.txt")
            with open(text_filename, "w", encoding="utf-8") as text_file:
                text_file.write(text)
        
        # Close the PDF document
        pdf_document.close()


    # Define a function to convert text to speech and save as an MP3 file
    def _text_to_speech(self, input_file, output_file):
        # Read the content from the input text file
        with open(input_file, 'r') as file:
            text = file.read()

        # Create a gTTS object and generate the speech from the text
        tts = gTTS(text)

        # Save the generated speech as an MP3 file
        tts.save(output_file)

        # Print a message indicating successful conversion and saving
        print(f"Text converted and saved as {output_file}")


    def loopfiles_and_make_pdf_to_mp3(self, folder_path):
        # Check if the specified folder path exists
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            return

        # Check if the specified path is a valid folder
        if not os.path.isdir(folder_path):
            print(f"'{folder_path}' is not a valid folder path.")
            return

        # Walk through the folder and its subfolders
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                #print(f"Found file: {file_path}")

                #Create a filename without exxtension
                filepath_without_extension = file_path.split(".")
                filename_without_extention = filepath_without_extension[1].split("/")
                #print(filename_without_extention[2])

                self._text_to_speech(file_path, f"./{self.output_folder}/{filename_without_extention[2]}" + ".mp3")
                #print(f"./{self.output_folder}/{filename_without_extention[2]}" + ".mp3")

    

        
if __name__ == "__main__":

    pdf = PDFTool("Secrets-Of-Speed-Seduction.pdf", "pdf2text")
    pdf.extract_text_from_pdf(pdf.file_path, pdf.output_folder)
    
    pdf.loopfiles_and_make_pdf_to_mp3("./pdf2text/")
    print("Text extraction complete.")