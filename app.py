import PyPDF2
import pyttsx3

def convert_pdf_to_audiobook(pdf_path, start_page=0, end_page=None):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            total_pages = len(reader.pages)

            # Adjust page range if not specified
            start_page = max(0, start_page)
            end_page = end_page if end_page is not None else total_pages
            end_page = min(end_page, total_pages)

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Speed of speech
            engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

            # Extract text and read it aloud
            for page_num in range(start_page, end_page):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text.strip():  # Read only if the page has text
                    print(f"Reading Page {page_num + 1}...")
                    engine.say(text)
            engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ").strip()
    start_page = int(input("Enter the start page (0-indexed, default is 0): ") or 0)
    end_page = input("Enter the end page (default is the last page): ")
    end_page = int(end_page) if end_page else None

    convert_pdf_to_audiobook(pdf_path, start_page, end_page)
