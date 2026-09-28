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


#This function is for after the model has run


SbS(original_path, mask_path, output_path)

    """
    This function takes the original image and concatinates it with the unbinarized output of the model so that you can easily compare the two side by side. Both folders should have their original naming, i.e. DATASET_001 for the original matching with DATASET_001_0000 for the AI image
    original_path: path to the folder containing the original images tested by the model
    mask_path: path to the folder containing the unbinarized output of the CV model
    output_path: path to the desired folder for the output side by side images
    """

