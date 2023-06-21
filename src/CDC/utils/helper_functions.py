import os
from pathlib import Path

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import Any
from CDC import logger
import json


@ensure_annotations
def read_yaml(filename: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.
    """
    try:
        with open(filename) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file {filename} uploaded successfully")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"yaml file {filename} not found")
        raise e
    except BoxValueError as e:
        logger.error(f"yaml file {filename} is empty")
        raise ValueError("file is empty")


@ensure_annotations
def save_json(path: Path, content: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(content, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns a ConfigBox object.
    """
    try:
        with open(path,"r") as f:
            content = json.load(f)
            logger.info(f"json file {path} loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"json file {path} not found")
        raise e
    except BoxValueError as e:
        logger.error(f"json file {path} is empty")
        raise ValueError("file is empty")

@ensure_annotations
def savebin(path: Path, content: Any) -> None:
    """
    Saves a binary file.
    """
    try:
        joblib.save(filename=path, value=content)
        logger.info(f"bin file {path} saved successfully")
    except FileNotFoundError as e:  
        logger.error(f"bin file {path} not found")
    
@ensure_annotations
def loadbin(path: Path) -> Any:
    """
    Loads a binary file.
    """
    try:
        content = joblib.load(path)
        logger.info(f"bin file {path} loaded successfully")
        return content
    except FileNotFoundError as e:
        logger.error(f"bin file {path} not found")
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in kilobytes.
    """
    try:
        size =  round(os.path.getsize(path)/1024)
        logger.info(f"size of {path} is {size} KB")
        return f"~ {size} KB"
    except FileNotFoundError as e:
        logger.error(f"file {path} not found")
        raise e
    

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")