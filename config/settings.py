import os

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")

# Model Configuration
MODEL_NAME = "llama-3.1-8b-instant"
TEMPERATURE = 0

# Data Configuration
DEFAULT_SHEET_NAME = 'Data'
DEFAULT_HEADER_ROW = 1

# Path Configuration
DATA_FILE_PATH = './data/Sample Data for the Model.xlsx'