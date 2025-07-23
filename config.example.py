"""
Configuration template file.
Copy this file to config.py and update the values as needed.
"""


class Config:
    """Configuration class with class attributes for all settings."""
    
    # Database configuration
    DATABASE_URL = "your_database_url_here"
    DATABASE_NAME = "your_database_name"
    DATABASE_USER = "your_username"
    DATABASE_PASSWORD = "your_password"
    
    # API configuration
    API_KEY = "your_api_key_here"
    API_BASE_URL = "https://api.example.com"
    API_TIMEOUT = 30
    
    # Application settings
    DEBUG = False
    LOG_LEVEL = "INFO"
    MAX_WORKERS = 4
    
    # File paths
    DATA_DIR = "data/"
    OUTPUT_DIR = "results/"
    TEMP_DIR = "temp/"
    
    # Other settings
    DEFAULT_ENCODING = "utf-8"
    MAX_RETRY_ATTEMPTS = 3
    CACHE_ENABLED = True