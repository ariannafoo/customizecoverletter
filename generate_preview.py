from pdf2image import convert_from_path
import os

# Path to the PDF file
pdf_file_path = 'documents/AriannaFoo_Resume.pdf'  # Replace with your PDF path

# Specify the output directory for previews
output_path = 'output_previews/'
os.makedirs(output_path, exist_ok=True)

# Convert PDF to images with high DPI for maximum quality
dpi = 600  # Adjust DPI for better quality
images = convert_from_path(pdf_file_path, dpi=dpi)

# Save the first page as JPEG with high quality
output_file_path = os.path.join(output_path, 'AriannaFoo_Resume_page1.jpg')
images[0].save(output_file_path, 'JPEG', quality=100)  # Save as JPEG with maximum quality

print(f'PDF preview created at: {output_file_path}')
