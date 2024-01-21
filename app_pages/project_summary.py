# app_pages/project_summary.py
import streamlit as st
from data_preprocessing import count_images_in_subfolders

def show_project_summary():
    st.title("Project Summary")

    # Placeholder content
    st.write("Welcome to the Cherry Leaves Mildew Detection Project!")
    st.write("This dashboard aims to help you analyze and understand the dataset.")

    # Verify Dataset Paths
    st.header("Dataset Paths:")
    st.write(f"- Training Set: {train_path}")
    st.write(f"- Validation Set: {validation_path}")
    st.write(f"- Test Set: {test_path}")

    # Count images in each class for specific paths
    class_counts_train = count_images_in_subfolders(train_path)
    class_counts_validation = count_images_in_subfolders(validation_path)
    class_counts_test = count_images_in_subfolders(test_path)

    st.header("Dataset Summary:")
    st.write("The dataset contains images of cherry leaves, categorized into different classes.")

    # Display counts for each class in training set
    st.subheader("Training Set:")
    for class_name, count in class_counts_train.items():
        st.write(f" - Number of {class_name} images: {count}")

    # Display counts for each class in validation set
    st.subheader("Validation Set:")
    for class_name, count in class_counts_validation.items():
        st.write(f" - Number of {class_name} images: {count}")

    # Display counts for each class in test set
    st.subheader("Test Set:")
    for class_name, count in class_counts_test.items():
        st.write(f" - Number of {class_name} images: {count}")

    # Add any additional dataset summary information

    st.header("Client Requirements:")
    st.write("Our client has specific requirements for identifying mildew in cherry leaves:")
    st.write(" - Requirement 1: Specify the desired outcome or goal.")
    st.write(" - Requirement 2: Provide any additional client expectations or specifications.")
    # Add any other relevant client requirements

    st.write("By exploring the different sections of this dashboard, you can gain insights from the analysis and visualize the findings related to cherry leaf health.")
