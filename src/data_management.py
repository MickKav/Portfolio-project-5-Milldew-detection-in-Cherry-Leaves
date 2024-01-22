import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib

def download_dataframe_as_csv(df):
    """
    Download DataFrame as CSV with timestamped filename
    """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report_{datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href

def load_pkl_file(file_path):
    """
    Load a pickled file
    """
    return joblib.load(filename=file_path)

def count_images_in_subfolders(directory):
    image_counts = {}

    for subfolder in os.listdir(directory):
        subfolder_path = os.path.join(directory, subfolder)
        if os.path.isdir(subfolder_path):
            images = [file for file in os.listdir(subfolder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
            image_counts[subfolder] = len(images)

    return image_counts