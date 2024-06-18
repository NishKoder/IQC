import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s:%(message)s:')

list_dirs = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "setup.py",
]

for filepath in list_dirs:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    logging.info(f"filedir: {filedir}")
    logging.info(f"filename: {filename}")

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory: {filedir}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        logging.info(f"created file: {filepath}")
        open(filepath, 'a').close()
    else:
        logging.info(f"file already exists: {filepath}")
