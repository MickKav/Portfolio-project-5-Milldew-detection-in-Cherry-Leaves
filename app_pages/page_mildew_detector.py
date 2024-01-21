import streamlit as st
from data_preprocessing import count_images_in_subfolders

def mildew_detection_body():
    st.title("Mildew Detection")

    st.write("This is the Mildew Detection page.")
    
    # Verify Dataset Path
    # Assign dataset paths
    train_path = '/path/to/your/train/data'
    validation_path = '/path/to/your/validation/data'
    test_path = '/path/to/your/test/data'

    # Count images in each class
    class_counts = count_images_in_subfolders(train_path)

    st.header("Dataset Summary:")
    st.write("The dataset contains images of cherry leaves, categorized into different classes.")

    for class_name, count in class_counts.items():
        st.write(f" - Number of {class_name} images: {count}")

    # Add more content as needed
