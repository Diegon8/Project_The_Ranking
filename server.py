import os
from dotenv import load_dotenv
load_dotenv()
from src.app import app
import students_controller

PORT = os.getenv('PORT')
app.run('0.0.0.0', PORT, debug=True)