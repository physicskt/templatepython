"""
Logger setup module for the entire application.
Provides a standardized logger with file name and line number information.
"""

import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name=None, log_file='.app.log', level=logging.INFO):
    """
    Set up a logger with standardized format including file name and line number.
    
    Args:
        name (str): Logger name. If None, returns root logger.
        log_file (str): Log file path. Defaults to '.app.log'.
        level (int): Logging level. Defaults to INFO.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logger
    logger = logging.getLogger(name)
    
    # Avoid adding multiple handlers if logger already exists
    if logger.handlers:
        return logger
        
    logger.setLevel(level)
    
    # Create formatter with file name and line number
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger


def get_logger(name=None):
    """
    Get a logger instance. Creates one if it doesn't exist.
    
    Args:
        name (str): Logger name. If None, returns root logger.
    
    Returns:
        logging.Logger: Logger instance.
    """
    return setup_logger(name)


# Create default logger for immediate use
default_logger = setup_logger()