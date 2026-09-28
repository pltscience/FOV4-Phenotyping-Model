import CV_Functions
from generate_dataset_json import generate_dataset_json
import cv2
import numpy as np
import os
from PIL import Image, ImageChops
from typing import Tuple
from batchgenerators.utilities.file_and_folder_operations import save_json, join
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image



#This function is for before you run the model

#Prepare images for analysis
grabcut(input_path, output_path)

    """
    This function takes a collection of images and opens a window where you can click and drag a rectangle over the object you 
    want to section out to make a copy with a mask covering the background 
    input_path: path to a folder containing unprocessed images to be modified
    output_path: path to location you want to save the masked images to
    """

