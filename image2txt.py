import sys
import cv2
import pytesseract

# Path to Tesseract executable (update this with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding or other preprocessing if needed
    # For example: ret, thresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(gray_image)

    return extracted_text

if __name__ == "__main__":
    try:
        image_path = f"{sys.argv[1]}"  # Update with the path to your image
        extracted_text = extract_text_from_image(image_path)

        if sys.argv[3] == "1":
            with open(f'{sys.argv[2]}.txt', mode="w") as output_file:
                output_file.write(extracted_text)

        print("Extracted Text:")
        print(extracted_text)
    except:
        print('Usage: python image2txt.py "filename.[jpg´|png|...]" output_filename 0|1 (1=write to file)')


