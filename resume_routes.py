from flask import Blueprint, request, jsonify
from controllers.resume_controller import handle_resume_upload

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/upload-resume', methods=['POST'])
def upload_resume():
    return handle_resume_upload(request)
