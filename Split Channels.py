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


split_channels(input_pth, output_pth)

    """
    input_pth: Path to the folder containing the images sectioned with grabcut
    output_pth:Path to the desired folder for the split images. They will be used for both the imagesTr and imagesTs folders 
    of the model
    """


