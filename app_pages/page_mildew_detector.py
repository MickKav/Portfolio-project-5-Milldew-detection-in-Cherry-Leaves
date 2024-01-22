import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from src.data_management import load_pkl_file, download_dataframe_as_csv

from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


# Function for Mildew Detection Page
def mildew_detection_body():
    st.info(
        "As a user, you can upload cherry leaf images for live prediction and view the results in a user-friendly interface."
    )

    st.write(
        "You can upload cherry leaf images to check for mildew presence. For live predictions, feel free to upload your images."
    )

    st.write("---")

    # File uploader for images
    images_buffer = st.file_uploader(
        'Upload cherry leaf images for live prediction. You may select more than one.',
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    if images_buffer is not None:
        df_report = pd.DataFrame([])

        # Process each uploaded image
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            # Model prediction
            version = 'v3'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            
            # Display predictions and probabilities
            plot_predictions_probabilities(pred_proba, pred_class)

            # Store results in a dataframe
            df_report = df_report.append({"Name": image.name, 'Result': pred_class},
                                         ignore_index=True)

        # Display analysis report
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
