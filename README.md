# Fullstack Assignment

A Python-based project for extracting and processing text and images from PDF, DOCX, and PPTX files.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Project Description

This project provides scripts to:

1. Extract text and images from PDF and DOCX files.
2.  For each paragraph in the PDF/DOCX, extract the following details:
   - Text content
   - Font type
   - Font size
   - Styling elements (such as italics, bold, etc.)
   - Text color
3. Convert the text of each extracted paragraph to uppercase and compile all the uppercase paragraphs into new PDF and DOCX files.
4. Translate text from PPTX files to English and append the translation to the slides.

## Features

- Extract and save text and images from PDF and DOCX files.
- Convert text to uppercase and compile it into new PDF and DOCX files.
- Translate text in PPTX files to English and append the translation to the slides.
- Easy deployment using Docker.

## Installation

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/dungv798/Fullstack-Assignment.git
   cd project-name

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt

4. (Optional) Build the Docker image:
   ```sh
   docker build -t fullstackassignment .


## Usage
# Running the Script Manually

1. Ensure you have activated the virtual environment if you are using one.

2. Run the script:
   
    ```sh
   python main_script.py
  
  
# Running with Docker 
1. Run the Docker container:
   ```sh
   docker run -d --name my_fullstack_assignment -p 4000:80 fullstackassignment
   
2. To access the output files, copy them from the container to your local machine:
   ```sh
   docker cp my_fullstack_assignment:/app/output_files ./output_files
   
3. To stop and remove the container:
   ```sh
   docker stop my_fullstack_assignment
   docker rm my_fullstack_assignment