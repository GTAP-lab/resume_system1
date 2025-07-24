import os
from werkzeug.utils import secure_filename
from ai_engine.resume_parser import extract_resume_data

def handle_resume_upload(request):
    if 'resume' not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files['resume']
    filename = secure_filename(file.filename)
    filepath = os.path.join('uploads', filename)
    file.save(filepath)

    parsed_data = extract_resume_data(filepath)
    return {"parsed": parsed_data}
