"""
Configuration template file.
Copy this file to config.py and update the values as needed.
"""


class config:
    """Configuration class with static methods for all settings."""
    
    # Database configuration
    @staticmethod
    def DATABASE_URL():
        return "your_database_url_here"
    
    @staticmethod
    def DATABASE_NAME():
        return "your_database_name"
    
    @staticmethod
    def DATABASE_USER():
        return "your_username"
    
    @staticmethod
    def DATABASE_PASSWORD():
        return "your_password"
    
    # API configuration
    @staticmethod
    def API_KEY():
        return "your_api_key_here"
    
    @staticmethod
    def API_BASE_URL():
        return "https://api.example.com"
    
    @staticmethod
    def API_TIMEOUT():
        return 30
    
    # Application settings
    @staticmethod
    def DEBUG():
        return False
    
    @staticmethod
    def LOG_LEVEL():
        return "INFO"
    
    @staticmethod
    def MAX_WORKERS():
        return 4
    
    # File paths
    @staticmethod
    def DATA_DIR():
        return "data/"
    
    @staticmethod
    def OUTPUT_DIR():
        return "results/"
    
    @staticmethod
    def TEMP_DIR():
        return "temp/"
    
    # Other settings
    @staticmethod
    def DEFAULT_ENCODING():
        return "utf-8"
    
    @staticmethod
    def MAX_RETRY_ATTEMPTS():
        return 3
    
    @staticmethod
    def CACHE_ENABLED():
        return True