# Used to open and manipulate word documents
from docx import Document
from docx.shared import Pt

# document = Document("documents/Arianna_Foo_Cover_Letter.docx")
# all_paragraphs = document.paragraphs

class CoverLetter():

    def __init__(self, document_path, date, company, city, position):

        # User inputs
        self.document = Document(document_path)
        self.date = date
        self.company = company
        self.city = city
        self.position = position

        # Define style
        self.style = self.defineDocumentStyles()

        # Create dictionary based on user input - will replace placeholders in doc
        self.replacements = {
            '{DATE}': self.date,
            '{COMPANY}': self.company,
            '{CITY}': self.city,
            '{POSITION}': self.position
        }

    def defineDocumentStyles(self):
        """
        Define the document styles for the cover letter.
        """
        style = document.styles['Normal']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(11)

        return style
    
    # TODO: edit colour and font in one placeholder
    def replacePlaceholders(self):
        """
        Replace placeholders in the cover letter and save new cover letter.
        """
        all_paragraphs = self.document.paragraphs

        for key, value in self.replacements.items():
            for paragraph in all_paragraphs:
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, value)
                    paragraph.style = self.style

        for paragraph in all_paragraphs:
            print(paragraph.text)

        self.document.save(f"{self.company}_Arianna_Foo_Resume.docx")
    
    def exportAs(document_type):
        pass






""" TODO
- option to save as pdf
- choose where to save
- create new folder to save??
- save job to excel sheet

def replace_placeholders(docx_path, replacements, output_path):

    Replace placeholders in the Word document with corresponding values from replacements.
"""