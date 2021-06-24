import glob
import shutil
import os
import random

import numpy as np
import matplotlib.pyplot as plt


from pathlib import Path
from PIL import Image

from config import FOOD_CLASSES, TRIAN_DATA_FOLDER, EVAL_DATA_FOLDER,\
    VAL_DATA_FOLDER


def split_data_into_class_folders(path_to_data, class_id):

    imgs_paths = glob.glob(os.path.join(path_to_data, "*.jpg"))
    path_to_save = os.path.join(path_to_data, FOOD_CLASSES[class_id])

    Path(path_to_save).mkdir(parents=True, exist_ok=True)

    for path in imgs_paths:
        basename = os.path.basename(path)
        if basename.startswith(str(class_id) + "_"):
            shutil.move(path, os.path.join(path_to_save, basename))

if __name__ == '__main__':

    cwd = os.getcwd()
    cwd_prt = "/".join(cwd.split("/")[:-1])

    path_to_train_data = cwd_prt + TRIAN_DATA_FOLDER
    path_to_val_data = cwd_prt + VAL_DATA_FOLDER
    path_to_eval_data = cwd_prt + EVAL_DATA_FOLDER
    
    for data_dir_path in [path_to_train_data, path_to_val_data,
                          path_to_eval_data]:
        for class_id in range(11):
            split_data_into_class_folders(data_dir_path, class_id)