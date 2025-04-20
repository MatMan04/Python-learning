import os
import pyzipper   # pip install pyzipper
from pathlib import Path
import getpass  # For secure password input

def create_secure_zip(folder_path, output_zip, password):
    """
    Creates a truly encrypted ZIP with AES-256
    """
    with pyzipper.AESZipFile(
        output_zip,
        'w',
        encryption=pyzipper.WZ_AES_256,  # Strongest encryption
        compress_type=pyzipper.ZIP_DEFLATED
    ) as zipf:
        zipf.setpassword(password.encode('utf-8'))
        
        for file in Path(folder_path).rglob('*'):
            if file.is_file():
                zipf.write(file, file.relative_to(folder_path))

# Usage (password entered securely):
password = getpass.getpass("Enter ZIP password: ")
create_secure_zip(r"D:\Scraping_to_MatMan", "SecureData.zip", password)