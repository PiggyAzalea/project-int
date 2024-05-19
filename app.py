import os
from flask import Flask, render_template, request, redirect, url_for, flash
from pptx import Presentation
import fitz  # PyMuPDF
from docx import Document

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def get_documents():
    documents = []
    uploads_dir = os.path.join(app.root_path, 'templates', 'uploads')
    for root, dirs, files in os.walk(uploads_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('.pdf') or file_path.endswith('.docx') or file_path.endswith('.pptx'):
                # Extract category from the folder name containing the file
                category = os.path.basename(os.path.dirname(file_path))
                documents.append({
                    'category': category,
                    'file_name': file_name,
                    'file_path': file_path
                })
    return documents

@app.route('/')
def index():
    documents = get_documents()
    return render_template('index.html', documents=documents)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = []
    for document in get_documents():
        if document['file_path'].endswith('.pdf'):
            text = extract_text_from_pdf(document['file_path'])
        elif document['file_path'].endswith('.docx'):
            text = extract_text_from_docx(document['file_path'])
        else:
            continue
        if search_in_text(text, query):
            results.append(document)
    return render_template('search_results.html', results=results, query=query)

def extract_text_from_pdf(file_path):
    text = ""
    document = fitz.open(file_path)
    for page in document:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    text = ""
    document = Document(file_path)
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def search_in_text(text, query):
    return query.lower() in text.lower()
@app.route('/open/<path:file_path>', methods=['GET'])
def open_file(file_path):
    # Here, you can implement the logic to open the file
    # For example, you can use the file_path to read the file content
    # and return it to the user or perform any other actions you need.
    # Make sure to handle any potential errors appropriately.

    # For now, let's just return a simple message indicating that the file is opened.
    return f"The file at path {file_path} is opened."

if __name__ == '__main__':
    app.run(debug=True)
