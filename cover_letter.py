# Used to open and manipulate word documents
from docx import Document
from datetime import date
from docx.shared import Pt, RGBColor
from io import BytesIO
from preview import Preview
from helper import isNotEmpty
import os
import subprocess

class CoverLetter():

    def __init__(self, company, city, position, suffix, document_path, destination):

        # User inputs
        self.date = date.today().strftime("%B %d, %Y")
        self.company = company
        self.city = city
        self.position = position
        self.suffix = suffix
        self.document = Document(document_path)
        self.destinaton = destination
        self.file_path = ""
       
        # Define style
        self.defineDocumentStyles()

        # Create dictionary based on user input - will replace placeholders in doc
        self.replacements = {
            '{DATE}': self.date,
            '{COMPANY}': self.company,
            '{CITY}': self.city,
            '{POSITION}': self.position,
            '{S}': self.suffix
        }

    def defineDocumentStyles(self):
        """
        Define the document styles for the cover letter.
        """
        self.reg_style = self.document.styles['CL_Normal']
        font_1 = self.reg_style.font
        font_1.name = 'Calibri'
        font_1.size = Pt(11)
    
    def generate_cover_letter(self):
        """
        Return file path and destination and save docx to destination.
        """
        # Create word document
        self.create_cover_letter_docx()

        # Create pdf document
        if(isNotEmpty(self.file_path) or not isNotEmpty(self.destinaton)):
            self.convert_docx_to_pdf(self.file_path, self.destinaton)

    def create_cover_letter_docx(self):
        """
        Replace fields and save new docx to destination.
        """
        all_paragraphs = self.document.paragraphs

        for key, value in self.replacements.items():
            for paragraph in all_paragraphs:
                if key in paragraph.text:
                        paragraph.text = paragraph.text.replace(key, value)
                        paragraph.style = self.reg_style

        # save as .docx
        self.file_path = os.path.join(self.destinaton, f"{self.company}_Arianna_Foo_Cover_Letter.docx")
        self.document.save(self.file_path)
  
    
    def convert_docx_to_pdf(self, docx_path, output_pdf_path):
        # Call LibreOffice to convert the document
        subprocess.run(['/Applications/LibreOffice.app/Contents/MacOS/soffice', '--headless', '--convert-to', 'pdf', docx_path, '--outdir', output_pdf_path])

        # generate preview
        pdf_file_path = f"{output_pdf_path}/{self.company}_Arianna_Foo_Cover_Letter.pdf"    
        
        if os.path.exists(pdf_file_path):
            print("---PATH EXISTS---")
            new_preview = Preview(pdf_file_path, self.company)
            new_preview.generate_preview()
        else:
            print(f"Error: PDF file not found at {pdf_file_path}")