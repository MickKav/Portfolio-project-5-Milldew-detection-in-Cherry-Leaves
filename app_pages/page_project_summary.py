# Import necessary libraries
import streamlit as st

# Function to show project summary
def show_project_summary():
    st.title("Project Summary")

    # Introduction
    st.write("Welcome to the Cherry Leaves Mildew Detection Project!")
    st.write("This dashboard aims to help you analyze and understand the dataset.")

    # Dataset Description
    st.header("Dataset Overview")
    st.write("The dataset contains images of cherry leaves.")

    # Business Understanding
    st.header("Business Understanding")
    st.write("The primary objective is to detect mildew in cherry leaves.")
    st.write("This addresses the need for early detection of plant diseases, enabling timely intervention.")

    # Data Analysis and Visualization
    st.header("Data Analysis and Visualization")
    st.write("We have performed exploratory data analysis (EDA) and visualized key aspects of the dataset.")

    # Specific Insights from EDA
    st.subheader("Insights from EDA:")
    st.write("- The distribution of mildew and non-mildew samples in the dataset.")
    st.write("- Correlation analysis between various features in the dataset.")
    st.write("- Visualizations showing the average and variability of leaf characteristics.")
    st.write("- Identification of any class imbalance in the dataset.")

    # Business Case for Mildew Detection
    st.header("Business Case for Mildew Detection")
    st.subheader("Aim:")
    st.write("Detect mildew in cherry leaves.")

    st.subheader("Learning Method:")
    st.write("Utilize machine learning techniques.")

    st.subheader("Ideal Outcome:")
    st.write("Accurate detection of mildew.")

    st.subheader("Success/Failure Metrics:")
    st.write("Define the metrics used to evaluate model performance.")

    st.subheader("Model Output and Relevance:")
    st.write("Describe the significance of the model output for end-users.")

    # Version Control
    st.header("Version Control")
    st.write("Git & GitHub have been used for version control throughout the development of this project.")

