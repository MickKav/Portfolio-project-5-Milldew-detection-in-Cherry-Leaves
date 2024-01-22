import streamlit as st
import os
import itertools
import random
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

def leaves_visualizer():
    st.title("Cherry Leaves Visualizer")

    st.write("Visualize your cherry leaves dataset here.")
    st.info(
        f"* The primary objective is to detect mildew in cherry leaves, addressing the need for early disease detection in plants."
    )

    version = 'v3'

    if st.checkbox("Difference between average and variability image"):
    
        avg_mildew_path = os.path.join("notebooks", "outputs", version, "avg_var_powdery_mildew.png")
        avg_healthy_path = os.path.join("notebooks", "outputs", version, "avg_var_healthy.png")

        if os.path.exists(avg_mildew_path):
           avg_mildew = plt.imread(avg_mildew_path)
           st.image(avg_mildew, caption='Average Powdery Mildew Image')
        else:
           st.warning("The image file does not exist.")

        if os.path.exists(avg_healthy_path):
           avg_healthy = plt.imread(avg_healthy_path)
           st.image(avg_healthy, caption='Average Healthy Image')
        else:
           st.warning("The Healthy image file does not exist.")

        st.write("---")

        st.warning(
            f"* The average and variability images may not show patterns where we could intuitively differentiate one from another."
            f" However, a small difference in the color pigment of the average images is observed for both labels."
        )

        st.image(avg_mildew, caption='Mildew Leaf - Average and Variability')
        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average mildew and average healthy leaves"):
        avg_diff_path = os.path.join("notebooks", "outputs", version, "avg_diff.png")

        if os.path.exists(avg_diff_path):
           diff_between_avgs = plt.imread(avg_diff_path)
           st.image(diff_between_avgs, caption='Difference between average images')
        else:
           st.warning("The average difference image file does not exist.")

        st.warning(
            f"* This study didn't show patterns where we could intuitively differentiate one from another."
        )
        st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        my_data_dir = 'notebooks/inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(os.path.join(my_data_dir, 'train'))
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=os.path.join(my_data_dir, 'train'),
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:

        images_list = os.listdir(os.path.join(dir_path, label_to_display))
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()
    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")

    st.write("Visualize your cherry leaves dataset here.")