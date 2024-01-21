import os
from PIL import Image
import numpy as np

"""
This is a simple module that provides functions to:

Load images from a specified folder.
Resize a list of images to a target size.
Preprocess a list of images (scaling pixel values between 0 and 1).
"""

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        if os.path.isfile(img_path) and img_path.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(img_path)
            images.append(img)
    return images

def resize_images(images, target_size):
    resized_images = [img.resize(target_size, Image.LANCZOS) for img in images]
    return resized_images

def preprocess_images(images, target_size):
    resized_images = resize_images(images, target_size)
    processed_images = [np.array(img) / 255.0 for img in resized_images]
    return processed_images

def count_images_in_subfolders(root_folder):
    subfolders = [f.path for f in os.scandir(root_folder) if f.is_dir()]
    image_counts = {os.path.basename(subfolder): len(os.listdir(subfolder)) for subfolder in subfolders}
    return image_counts
