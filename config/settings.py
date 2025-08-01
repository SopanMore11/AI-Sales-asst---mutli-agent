import os

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Model Configuration
MODEL_NAME = "gemma2-9b-it"
TEMPERATURE = 0

# Data Configuration
DEFAULT_SHEET_NAME = 'Data'
DEFAULT_HEADER_ROW = 1

# Path Configuration
DATA_FILE_PATH = './data/Sample Data for the Model.xlsx'