import os
from extract_pdf_content import extract_text_images_pdf
from compile_uppercase_to_docx import compile_uppercase_to_docx
from compile_uppercase_to_pdf import compile_uppercase_to_pdf
from translate_pptx import translate_pptx
from extract_docx_content import extract_text_images_docx

print("Starting the script...")

if __name__ == "__main__":
    print("Inside main...")
    pdf_path = "input_files/pdf_mock_file.pdf"
    docx_path = "input_files/docx_mock_file.docx"
    output_dir = "output_files"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    print("Created output directory...")

    # Extract text and images from PDF
    extract_text_images_pdf(pdf_path, output_dir)
    print("Extracted text and images from PDF...")

    pdf_text_file_path = os.path.join(output_dir, "pdf_extracted_text.txt")
    uppercase_pdf_path = os.path.join(output_dir, "uppercase_pdf_output.pdf")
    uppercase_docx_path = os.path.join(output_dir, "uppercase_docx_output.docx")

    # Compile uppercase text into new PDF
    compile_uppercase_to_pdf(pdf_text_file_path, uppercase_pdf_path)
    print("Compiled uppercase text to PDF...")

    # Compile uppercase text into new DOCX
    compile_uppercase_to_docx(pdf_text_file_path, uppercase_docx_path)
    print("Compiled uppercase text to DOCX...")

    input_file = 'input_files/Networking.pptx'
    output_pptx_file = 'output_files/Translated_Networking.pptx'
    output_image_directory = 'output_files/pptx_images'

    # Translate PPTX
    translate_pptx(input_file, output_pptx_file)
    print("Translated PPTX...")

    # Extract text and images from DOCX
    extract_text_images_docx(docx_path, output_dir)
    print("Extracted text and images from DOCX...")
