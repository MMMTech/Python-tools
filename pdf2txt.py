import fitz  # PyMuPDF
import os, sys

def extract_text_from_pdf(pdf_path, output_folder):
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

if __name__ == "__main__":
    pdf_file_path = f"{sys.argv[1]}"       # Replace with your PDF file path
    output_folder_path = "pdf2txt"     # Replace with your desired output folder
    
    extract_text_from_pdf(pdf_file_path, output_folder_path)
    print("Text extraction complete.")
