import os
import cv2
import numpy as np
from pathlib import Path
from typing import Tuple
import matplotlib.pyplot as plt


def load_image(fname: str, cv2_read_param: int = 0, path_extra="") -> Tuple[str, np.ndarray]:
    """
    Loads an image from the data folder using cv2.imread
    :param fname: the name of the image file (format must be specified)
    :param path_extra: extra path entry to be added to the data/ default path
    :param cv2_read_param: the parameter for cv2.imread
        As a reference:
        cv2.IMREAD_COLOR (1): Loads a color image. Any transparency of image will be neglected
        cv2.IMREAD_GRAYSCALE (0): Loads image in grayscale mode
        cv2.IMREAD_UNCHANGED (-1): Loads image as such including alpha channel
    :return: the image read from the file and its name
    """
    if len(path_extra) > 0:
        filepath = Path.cwd()/'data'/path_extra/fname
    else:
        filepath = Path.cwd()/'data'/fname
    print("Filepath:"+str(filepath))
    assert (filepath.exists() is True), "Wrong path: "+str(filepath)

    img_name = str(os.path.splitext(fname)[0])
    # img_basename = str(Path.cwd() / os.path.splitext(filename)[0])
    img = cv2.imread(str(filepath), cv2_read_param)
    assert (img is not None), "There was an issue loading the image"

    if cv2_read_param != 0:
        # invert channels from BGR to RGB
        img[:, :, :] = img[:, :, ::-1]
    return img_name, img


def save_image(filename, img):
    """
    Save an image in the current directory
    :param filename: the name of the destination file
    :param img: the image that has to be saved
    """
    filepath = Path.cwd()/'out'/filename
    print(filepath)
    img[:, :, :] = img[:, :, ::-1]
    # assert (filepath.exists() is True), "Wrong path"
    cv2.imwrite(str(filepath), img)


def display_image(img, cmap, title):
    """
    Display an image using matplotlib.imshow()
    :param img: original image
    :param cmap: the colormap passed to the matplotlib.imshow() function
    :param title: the title of the plot
    """
    if cmap is None:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.show()
