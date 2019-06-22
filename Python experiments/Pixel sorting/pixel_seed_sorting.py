from typing import Tuple, List

from image_utils import load_image
from image_utils import display_image, save_image
import cv2


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs((a[0]-b[0])+(a[1]-b[1]))


def neighbors_coordinates(seed_coordinates: Tuple, ksize: int, height: int, width: int,
                          allow_diagonals: bool = True, include_seed=True) -> List[Tuple[int, int]]:
    """
    Return the list of the coordinates of the neighbors, given the coordinates of the center, in a 2D matrix
    :param seed_coordinates: the coordinates of the central element
    :param ksize: the size of the squared kernel
    :param height: the number of rows
    :param width: the number of columns
    :param allow_diagonals: if True computes the neighbors in all 8 directions,
    if False computes only N-S-E-W
    :param include_seed: decide whether the seed (central element) must be returned
    :return: the list of tuples of coordinates around the given element
    """
    pad = ksize//2
    left_border = max(0, seed_coordinates[0]-pad)
    right_border = min(width, seed_coordinates[0]+pad+1)
    top_border = max(0, seed_coordinates[1]-pad)
    bottom_border = min(height, seed_coordinates[1]+pad+1)

    if allow_diagonals:
        neighbors = [(i, j) for i in range(left_border, right_border)
                     for j in range(top_border, bottom_border)]
    else:
        pivot_row = set([(i, seed_coordinates[1]) for i in range(left_border, right_border)])
        pivot_col = set([(seed_coordinates[0], j) for j in range(top_border, bottom_border)])
        neighbors = list(pivot_row.union(pivot_col))
    if not include_seed:
        neighbors.remove(seed_coordinates)
    return neighbors


def edges_coordinates(edg):
    coordinates = []
    for x in range(edg.shape[0]):
        for y in range(edg.shape[1]):
            if edg[x, y] == 255:
                coordinates.append((x, y))
    return coordinates


def enhance_borders(img, edg, marker_size=3):
    edges = edges_coordinates(edg)
    enhanced = img.copy()
    for e in edges:
        neighbors = neighbors_coordinates(seed_coordinates=e, ksize=marker_size,
                                          width=enhanced.shape[0], height=enhanced.shape[1])
        for n in neighbors:
            enhanced[n[0], n[1], :] = 255
    return enhanced


def pixel_propagation_along_edges(img, edg, direction: str):
    result = img.copy()
    edges = edges_coordinates(edg)

    for e in edges:
        if direction == "UP":
            reference_pixel = img[e[0], e[1], :]
            result[:e[0], e[1], :] = reference_pixel
        elif direction == "DOWN":
            reference_pixel = img[e[0], e[1], :]
            result[e[0]:, e[1], :] = reference_pixel
        elif direction == "LEFT":
            reference_pixel = img[e[0], e[1], :]
            result[e[0], :e[1], :] = reference_pixel
        elif direction == "RIGHT":
            reference_pixel = img[e[0], e[1], :]
            result[e[0], e[1]:, :] = reference_pixel
    return result


def pixel_sorting_along_edges(img, edg, direction: str):
    result = img.copy()
    edges = edges_coordinates(edg)
    print("Here")

    for e in edges:
        if direction == "UP":
            pixel_list = img[:e[0], e[1], :]
            sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
            result[:e[0], e[1], :] = sorted_pixels[::-1]
        elif direction == "DOWN":
            pixel_list = img[e[0]:, e[1], :]
            sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
            result[e[0]:, e[1], :] = sorted_pixels[::-1]
        elif direction == "LEFT":
            # TODO "Fix value error exception"
            pixel_list = img[e[0], :e[1], :]
            sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
            result[e[0], :e[1], :] = sorted_pixels[::-1]
        elif direction == "RIGHT":
            pixel_list = img[e[0], e[1]:, :]
            sorted_pixels = sorted(pixel_list, key=lambda x:x[2])
            result[e[0], e[1]:, :] = sorted_pixels[::-1]
    return result


if __name__ == '__main__':
    for i in range(2, 3):
        fname = str(i)+".jpg"
        file_name, image = load_image(fname, cv2_read_param=1)
        display_image(image, title="Original image", cmap=None)

        edgemap = cv2.Canny(image, 100, 500)
        # enhanced_borders = enhance_borders(image, edgemap, marker_size=2)
        # display_image(enhanced_borders, title="Canny", cmap=None)
        # result_img = pixel_propagation_along_edges(image, edgemap, "RIGHT")
        result_img = pixel_sorting_along_edges(image, edgemap, "DOWN")
        # result_img = pixel_sorting_along_edges(result_img, edgemap, "RIGHT")
        display_image(result_img, title="", cmap=None)
        #save_image(file_name+"_sorting_narrow_down"+".png", result_img)
