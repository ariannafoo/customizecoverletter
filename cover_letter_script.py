# Used to open and manipulate word documents
from docx import Document
from docx.shared import Pt

document = Document("Arianna_Foo_Cover_Letter.docx")
all_paragraphs = document.paragraphs

# Defining styles for paragraphs
style = document.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)



def is_empty(data):
    """
    Return true if data structure is empty, otherwise false.

    Can also check with len method.
    """
    return not data

def get_non_empty_input(user_prompt):
    """
    Check if user input is non-empty and return result.

    >>> company_name = get_non_empty_input("Enter company name: ")
    >>> Enter company name: 
    
    >>> Enter company name: 
    Airbnb
    >>> print(company_name)
    Airbnb
    """
    user_input = ""

    while is_empty(user_input):
        print(user_prompt)
        user_input = input()
    return user_input

date = get_non_empty_input("Enter date (dd/mm/yyyy): ")
company_name = get_non_empty_input("Enter company name: ")
city = get_non_empty_input("Enter city: ")
position_name = get_non_empty_input("Enter position name: ")

# Create dictionary based on user input - will replace placeholders in doc
replacements = {
    '{DATE}': date,
    '{COMPANY}': company_name,
    '{CITY}': city,
    '{POSITION}': position_name
}

# Loop through dictionary and paragraphs to replace placeholders
for key, value in replacements.items():
    for paragraph in all_paragraphs:
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, value)
            paragraph.style = style

for paragraph in all_paragraphs:
    print(paragraph.text)

document.save(f"{company_name}_Arianna_Foo_Resume.docx")





""" TODO
- option to save as pdf
- save job to excel sheet

def replace_placeholders(docx_path, replacements, output_path):

    Replace placeholders in the Word document with corresponding values from replacements.
"""