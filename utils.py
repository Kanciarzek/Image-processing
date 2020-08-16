from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

from colorthief import ColorThief
from urllib import request
from urllib.error import HTTPError
from PIL import Image
from tqdm import tqdm


def download_images(link_list: List[str], img_dir: str = 'img') -> None:
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    for link in link_list:
        try:
            request.urlretrieve(link, f'{img_dir}/{link.split("/")[-1]}')
        except HTTPError:
            print(f'Image at {link} not downloaded')


def n_of_images(img_dir: str = 'img') -> int:
    return len(os.listdir(img_dir))


def get_image_data(img_path: str) -> Tuple[str, float, tuple, int, int]:
    filename: str = img_path.split('/')[-1]
    size: float = os.path.getsize(img_path) / 1024
    color_thief: ColorThief = ColorThief(img_path)
    pil_image: Image = color_thief.image
    dominant_color: tuple = color_thief.get_color(quality=10)
    width, height = pil_image.size
    return filename, size, dominant_color, width, height


def get_all_images_data(paths: List[str]) -> List[tuple]:
    return [get_image_data(f'img/{image_name}') for image_name in tqdm(paths)]


def plot_hist(dataframe: pd.DataFrame, column_name: str, min_bin=None, max_bin=None, number_of_bins: int = 20) -> None:
    if min_bin is None:
        min_bin = min(dataframe[column_name])
    if max_bin is None:
        max_bin = max(dataframe[column_name])
    plt.hist(dataframe[column_name], range=(min_bin, max_bin), bins=number_of_bins)
    plt.xlabel(column_name)
    plt.ylabel('Number of images')


def plot_popular_colors(dataframe: pd.DataFrame, coordinate_x_name: str, coordinate_y_name: str,
                        color_name: str) -> None:
    plt.scatter(dataframe[coordinate_x_name], dataframe[coordinate_y_name],
                c=color_tuples_to_array(dataframe, color_name))


def color_tuples_to_array(dataframe: pd.DataFrame, color_name: str) -> np.ndarray:
    return np.array([[*x] for x in dataframe[color_name]]) / 255


def plot_time(dataframe: pd.DataFrame, date_column: str, bins: int) -> None:
    plt.hist(dataframe[date_column], bins=bins)
    plt.xticks([min(dataframe[date_column]), max(dataframe[date_column])])
