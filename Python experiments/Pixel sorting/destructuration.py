from typing import Tuple, List

import numpy as np
from image_utils import load_image
from image_utils import display_image, save_image
import cv2


def pixel_sorting(img, direction: str):
    result = img.copy()

    if direction == "UP":
        for p in range(img.shape[2]):
            pixel_list = img[p, :, :]
            sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
            result[:, :, :] = sorted_pixels[::-1]
    # elif direction == "DOWN":
    #     pixel_list = img[e[0]:, e[1], :]
    #     sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
    #     result[e[0]:, e[1], :] = sorted_pixels[::-1]
    # elif direction == "LEFT":
    #     # TODO "Fix value error exception"
    #     pixel_list = img[e[0], :e[1], :]
    #     sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
    #     result[e[0], :e[1], :] = sorted_pixels[::-1]
    # elif direction == "RIGHT":
    #     pixel_list = img[e[0], e[1]:, :]
    #     sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
    #     result[e[0], e[1]:, :] = sorted_pixels[::-1]
    return result


def split_squares_random_direction_sorting(img: np.ndarray, n_squares: int, marker_size: int):
    """
    Split the image in squares
    :param img: the original image
    :param n_squares: the number of squares
    :param marker_size: the width of the line in pixels
    """
    result_img = img.copy()
    square_size = img.shape[0]//n_squares
    for nx in range(n_squares-1):
        for ny in range(n_squares-1):
            current_cell_pixels = result_img[square_size*nx:square_size*(nx+1),
                                  square_size*ny:square_size*(ny+1), :]

            result_img[square_size*nx:square_size*(nx+1), square_size*ny:square_size*(ny+1), :] = \
                pixel_sorting(current_cell_pixels, direction="UP")

    for n in range(n_squares):
        result_img[square_size*n: square_size*n+5, :, :] = 255
        result_img[:, square_size*n: square_size*n+5, :] = 255
    display_image(result_img, title="rotation test", cmap=None)


def split_squares_average(img: np.ndarray, n_squares: int, marker_size: int):
    """
    Split the image in squares
    :param img: the original image
    :param n_squares: the number of squares
    :param marker_size: the width of the line in pixels
    """
    result_img = img.copy()
    square_size = img.shape[0]//n_squares
    for nx in range(n_squares-1):
        for ny in range(n_squares-1):
            current_cell = result_img[square_size*nx:square_size*(nx+1), square_size*ny:square_size*(ny+1), :]
            for ch in range(3):
                result_img[square_size*nx:square_size*(nx+1), square_size*ny:square_size*(ny+1), ch] = \
                    np.mean(current_cell[:, :, ch])

    for n in range(n_squares):
        result_img[square_size*n: square_size*n+5, :, :] = 255
        result_img[:, square_size*n: square_size*n+5, :] = 255
    display_image(result_img, title="test", cmap=None)


if __name__ == '__main__':
    fname = "flower_5.jpg"
    file_name, image = load_image(fname, cv2_read_param=1, path_extra="flowers")
    # display_image(image, title="Original image", cmap=None)

    split_squares_random_direction_sorting(image, n_squares=10, marker_size=1)

    # display_image(result_img, title="", cmap=None)
    # save_image(file_name+"_sorting_narrow_down"+".png", result_img)
