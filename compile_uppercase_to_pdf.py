from fpdf import FPDF

# Mapping of font names to FPDF core fonts
FONT_MAPPING = {
    'arial': 'Arial',
    'arial-boldmt': 'Arial',
    'times new roman': 'Times',
    'times new roman-boldmt': 'Times',
    'courier': 'Courier',
    'courier-boldmt': 'Courier',
    'helvetica': 'Helvetica',
    'helvetica-boldmt': 'Helvetica',
    # Add more font mappings if needed
}


def compile_uppercase_to_pdf(input_text_file, output_pdf_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    with open(input_text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("Page "):
            # Add a new page for each page number
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, line, ln=True, align='C')
        elif line.startswith("{'Text': "):
            try:
                text_attributes = eval(line)
                font_name = text_attributes["Font"].lower()
                mapped_font = FONT_MAPPING.get(font_name, 'Arial')  # Default to Arial if font not found
                style = ''
                if text_attributes["Bold"]:
                    style += 'B'
                if text_attributes["Italic"]:
                    style += 'I'
                size = text_attributes["Size"]
                pdf.set_font(mapped_font, style, size)
                color = text_attributes["Color"]
                pdf.set_text_color((color >> 16) & 255, (color >> 8) & 255, color & 255)
                pdf.multi_cell(0, 10, text_attributes["Text"].upper().encode('latin1', 'replace').decode('latin1'))
            except Exception as e:
                print(f"Error processing line: {line} - {e}")

    pdf.output(output_pdf_file)


# Example usage
if __name__ == "__main__":
    input_text_file = "output_files/pdf_extracted_text.txt"
    output_pdf_file = "output_files/uppercase_pdf_output.pdf"
    compile_uppercase_to_pdf(input_text_file, output_pdf_file)
