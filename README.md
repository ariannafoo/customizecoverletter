# CoverLetterApp

A Python and **PyQt5** desktop application that automates the generation of personalized cover letters by populating a Word template with user input, converting the result to PDF, and rendering a live preview within the application.

The project focuses on improving the efficiency of cover letter creation while showcasing clean architecture, document processing, and desktop GUI development.


## ✨ Features

- 📝 Generate personalized cover letters from user input
- 📄 Automatically create:
  - `.docx` cover letters
  - `.pdf` versions
- 🖼️ Live preview of the generated PDF as an image
- 🖥️ Desktop GUI built with PyQt5
- 📂 Clean separation of views, models, and utilities
- ⚙️ Uses LibreOffice + Poppler for document conversion


## 🏗️ Project Architecture

The project follows a modular, MVC-style structure:

```text
CoverLetterApp/
├── main.py
├── app/
│   ├── views/        # PyQt UI pages
│   ├── models/       # Business logic (cover letter & preview generation)
│   ├── utils/        # Helper utilities
│   └── services/     # (optional) workflow logic
├── assets/           # Templates & static assets
├── output/           # Generated files (ignored by Git)
└── venv/
```


## 🧰 Tech Stack
- Python 3
- PyQt5
- python-docx
- pdf2image
- LibreOffice (CLI)
- Poppler
- Git & GitHub

## 📸 Demo
Demo video coming soon.

## 💡 Why This Project

This project demonstrates:
- GUI development with Python
- File processing and automation
- Clean project architecture
- Real-world problem solving
- Attention to user experience

## 📁 Future Improvements

- Editable preview before final export
- Resume attachment support
- Multiple templates
- Cross-platform packaging (PyInstaller)

## 👩‍💻 Author
Arianna Foo <br>
GitHub: https://github.com/ariannafoo <br>
LinkedIn: https://www.linkedin.com/arianna-foo