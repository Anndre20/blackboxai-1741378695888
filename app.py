from flask import Flask, render_template, request, send_file, jsonify
import os
from sorting import sort_files
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    # Get initial list of files
    sorted_files, metadata = sort_files(app.config['UPLOAD_FOLDER'])
    initial_files = []
    for file_path, meta in zip(sorted_files, metadata):
        initial_files.append({
            'name': os.path.basename(file_path),
            'expiration_date': meta.get('expiration_date'),
            'serial_number': meta.get('serial_number')
        })
    return render_template('index.html', initial_files=initial_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files[]')
    for file in files:
        if file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # Sort the uploaded files
    sorted_files, metadata = sort_files(app.config['UPLOAD_FOLDER'])
    
    # Create response with file info and metadata
    file_info = []
    for file_path, meta in zip(sorted_files, metadata):
        file_info.append({
            'name': os.path.basename(file_path),
            'expiration_date': meta.get('expiration_date'),
            'serial_number': meta.get('serial_number')
        })
    
    return jsonify({'files': file_info})

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(
        os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)),
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True, port=8000)
