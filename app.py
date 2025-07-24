from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)

# Register routes
from routes.resume_routes import resume_bp
app.register_blueprint(resume_bp)

if __name__ == '__main__':
    app.run(debug=True)
