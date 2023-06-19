import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s;')

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/utils/__init__.py',
    'src/components/__init__.py',
    'src/pipelines/__init__.py',    
    'src/entity/__init__.py',    
    'src/constants/__init__.py',    
    'src/config/__init__.py',
    'src/config/configuration/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'setup.py',
    'requirements.txt',
    'research/trials.ipynb',
    'templates/index.html'
]

for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created Directory : {filedir}")
    if not os.path.exists(filepath):
        with open(filepath,"w") as f:
            logging.info(f"Created File : {filepath}")
    else:
        logging.info(f"File : {filename} alredy exists")