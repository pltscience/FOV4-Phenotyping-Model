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

results(input_pth, save, label, outpath)

    """
    Returns the % stain of each sample from the output of the AI model
    input_pth: path to the folder containing the 0-2 scale result images of the model
    save = Boolean value. If True, the function will take the outputs of both stes of images and save them to an excel file
    label: String used to label the excel file
    outpath = path to save the excel file to
    """


