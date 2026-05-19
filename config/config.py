import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Chemins
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = os.path.join(BASE_DIR, 'data')
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
GRADES_FILE = os.path.join(DATA_DIR, 'grades.json')

# Configuration
ADMIN_ID = os.getenv('ADMIN_ID', '0')
BOT_NAME = "🎓 Academic CodeRun Bot"
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN not found in .env file!")
