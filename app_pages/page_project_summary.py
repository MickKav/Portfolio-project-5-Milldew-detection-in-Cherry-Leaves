import streamlit as st

# Function to show project summary
def show_project_summary():
    st.title("Project Summary")

    # Introduction
    st.info('''
            **Welcome to the Cherry Leaves Mildew Detection Project!**
            \n*This dashboard aims to help you analyze and understand the dataset.*
            ''')

    # Dataset Description
    st.header("Dataset Overview")
    st.write("The dataset contains images of cherry leaves.")

    # Business Understanding
    st.header("Business Understanding")
    st.info('''
            The primary objective is to detect mildew in cherry leaves.
            \nThis addresses the need for early detection of plant diseases, enabling timely intervention.
            ''')

    # Data Analysis and Visualization
    st.header("Data Analysis and Visualization")
    st.write("We have performed exploratory data analysis (EDA) and visualized key aspects of the dataset.")

    # Specific Insights from EDA
    st.success('''
                **Insights from EDA:**
                \n- The distribution of mildew and non-mildew samples in the dataset.
                \n- Correlation analysis between various features in the dataset.
                \n- Visualizations showing the average and variability of leaf characteristics.
                \n- Identification of any class imbalance in the dataset.
                ''')

    # Business Case for Mildew Detection
    st.header("Business Case for Mildew Detection")
    st.subheader("Aim:")
    st.info("Detect mildew in cherry leaves.")

    st.subheader("Learning Method:")
    st.error("Utilize machine learning techniques.")

    st.subheader("Ideal Outcome:")
    st.success("Accurate detection of mildew.")

    st.subheader("Success/Failure Metrics:")
    st.warning("Define the metrics used to evaluate model performance.")

    st.subheader("Model Output and Relevance:")
    st.info("Describe the significance of the model output for end-users.")

    # Version Control
    st.header("Version Control")
    st.write("Git & GitHub have been used for version control throughout the development of this project.")

