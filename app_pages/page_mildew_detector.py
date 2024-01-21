import streamlit as st
from src.data_preprocessing import count_images_in_subfolders

def mildew_detection_body():
    st.title("Mildew Detection")

    st.write("This is the Mildew Detection page.")
    
    # Verify Dataset Path
    # Assign dataset paths
    train_path = '/workspace/Portfolio-project-5-Milldew-detection-in-Cherry-Leaves/notebooks/inputs/cherry_leaves_dataset/cherry-leaves/train'
    validation_path = '/workspace/Portfolio-project-5-Milldew-detection-in-Cherry-Leaves/notebooks/inputs/cherry_leaves_dataset/cherry-leaves/validation'
    test_path = '/workspace/Portfolio-project-5-Milldew-detection-in-Cherry-Leaves/notebooks/inputs/cherry_leaves_dataset/cherry-leaves/test'

    # Count images in each class
    class_counts = count_images_in_subfolders(train_path)

    st.header("Dataset Summary:")
    st.write("The dataset contains images of cherry leaves, categorized into different classes.")

    for class_name, count in class_counts.items():
        st.write(f" - Number of {class_name} images: {count}")

    # Add more content as needed
