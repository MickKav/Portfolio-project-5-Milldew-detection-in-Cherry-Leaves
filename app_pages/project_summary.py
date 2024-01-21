# app_pages/project_summary.py
import streamlit as st

def show_project_summary():
    st.title("Project Summary")

    # Placeholder content
    st.write("Welcome to the Cherry Leaves Mildew Detection Project!")
    st.write("This dashboard aims to help you analyze and understand the dataset.")

    # Count images in each class
    dataset_path = '/workspace/Portfolio-project-5-Milldew-detection-in-Cherry-Leaves/notebooks/inputs/cherry_leaves_dataset/cheery-leaves'
    class_counts = count_images_in_subfolders(dataset_path)

    st.header("Dataset Summary:")
    st.write("The dataset contains images of cherry leaves, categorized into different classes.")
    
    for class_name, count in class_counts.items():
        st.write(f" - Number of {class_name} images: {count}")

    st.header("Dataset Summary:")
    st.write("The dataset contains images of cherry leaves, categorized into 'health' and 'mildew' classes.")
    st.write(f" - Number of health images: {len(health_images)}")
    st.write(f" - Number of mildew images: {len(mildew_images)}")
    # Add any additional dataset summary information

    st.header("Client Requirements:")
    st.write("Our client has specific requirements for identifying mildew in cherry leaves:")
    st.write(" - Requirement 1: Specify the desired outcome or goal.")
    st.write(" - Requirement 2: Provide any additional client expectations or specifications.")
    # Add any other relevant client requirements

    st.write("By exploring the different sections of this dashboard, you can gain insights from the analysis and visualize the findings related to cherry leaf health.")