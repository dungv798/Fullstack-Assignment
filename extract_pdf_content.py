import fitz  # PyMuPDF
import os

def extract_text_images_pdf(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)
    text_file_path = os.path.join(output_dir, "pdf_extracted_text.txt")
    images_dir = os.path.join(output_dir, "pdf_images")
    os.makedirs(images_dir, exist_ok=True)

    def format_text_for_eval(text):
        return text.replace("'", "\\'")

    with open(text_file_path, "w", encoding="utf-8") as text_file:
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]

            text_file.write(f"Page {page_num + 1}:\n\n")
            for block in blocks:
                if "lines" in block:
                    paragraph_text = ""
                    font = None
                    size = None
                    color = None
                    bold = False
                    italic = False
                    for line in block["lines"]:
                        for span in line["spans"]:
                            if font is None:
                                font = span["font"]
                            if size is None:
                                size = span["size"]
                            if color is None:
                                color = span["color"]
                            if span["flags"] & 2:
                                bold = True
                            if span["flags"] & 1:
                                italic = True
                            paragraph_text += span["text"] + " "
                    if paragraph_text.strip():
                        formatted_text = format_text_for_eval(paragraph_text.strip())
                        text_file.write(
                            f"{{'Text': '{formatted_text}', 'Font': '{font}', 'Size': {size}, 'Bold': {bold}, 'Italic': {italic}, 'Color': {color}}}\n\n"
                        )

            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = os.path.join(images_dir, f"page{page_num + 1}_img{img_index + 1}.{image_ext}")
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)

# Example usage
if __name__ == "__main__":
    pdf_path = "input_files/pdf_mock_file.pdf"
    output_dir = "output_files"
    extract_text_images_pdf(pdf_path, output_dir)
