# File Sorting Module

import os
import logging
import re
from datetime import datetime

logger = logging.getLogger('flask-api-service')

def extract_file_metadata(file_path):
    """
    Extract metadata from the given file.
    Returns a dictionary with expiration date and serial number if applicable.
    """
    metadata = {}
    try:
        # Example logic for extracting expiration date and serial number
        # This is a placeholder and should be replaced with actual extraction logic
        if file_path.endswith('.pdf'):
            # Simulate extraction logic for PDF files
            metadata['expiration_date'] = datetime.now().strftime("%Y-%m-%d")  # Placeholder
            metadata['serial_number'] = "123456789"  # Placeholder
        elif file_path.endswith('.txt'):
            # Simulate extraction logic for text files
            metadata['expiration_date'] = None
            metadata['serial_number'] = None
        
        logger.info(f"Extracted metadata from {file_path}: {metadata}")
    except Exception as e:
        logger.error(f"Error extracting metadata from {file_path}: {e}")
        return None  # Return None if extraction fails

    return metadata

def sort_files(directory='files'):
    """
    Sort files in the specified directory based on metadata and content.
    Returns a list of sorted file paths along with their metadata.
    """
    sorted_files = []
    file_metadata = []  # List to hold metadata for each file
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.pdf') or filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                sorted_files.append(file_path)
                metadata = extract_file_metadata(file_path)  # Extract metadata
                if metadata:  # Check if metadata extraction was successful
                    file_metadata.append(metadata)  # Store metadata
        
        # Sort files (example: by name)
        sorted_files.sort()
        logger.info(f"Files sorted successfully: {sorted_files}")
    except Exception as e:
        logger.error(f"Error sorting files: {e}")
    
    return sorted_files, file_metadata  # Return both sorted files and their metadata
