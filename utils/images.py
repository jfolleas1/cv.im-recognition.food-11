import glob
import shutil
import os
import random

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

from config import TRIAN_DATA_FOLDER



def visualise_some_images(path_to_data):

    imgs_paths = []
    labels = []

    for r, d, f, in os.walk(path_to_data):
        for file in f:
            if file.endswith(".jpg"):
                imgs_paths.append(os.path.join(r, file))
                labels.append(os.path.basename(r))

    fig = plt.figure(figsize=(16, 16))

    for i in range(16):
        chosen_index = random.randint(0, len(imgs_paths) - 1)
        chosen_img = imgs_paths[chosen_index]
        chosen_label = labels[chosen_index]

        ax = fig.add_subplot(4, 4, i+1)
        ax.title.set_text(chosen_label)
        ax.imshow(Image.open(chosen_img))
    plt.show()

def get_images_sizes(path_to_data):

    widths = []
    heights = []

    for r, _, f in os.walk(path_to_data):
        for file in f:
            if file.endswith(".jpg"):

                img = Image.open(os.path.join(r, file))
                widths.append(img.size[0])
                heights.append(img.size[1])
                img.close()

    mean_width = np.mean(widths)
    mean_heights = np.mean(heights)
    median_width = np.median(widths)
    median_heights = np.median(heights)

    return mean_width, mean_heights, median_width, median_heights
                


if __name__ == '__main__':

    cwd = os.getcwd()
    cwd_prt = "/".join(cwd.split("/")[:-1])

    path_to_train_data = cwd_prt + TRIAN_DATA_FOLDER
    
    visualise_some_images(path_to_train_data)