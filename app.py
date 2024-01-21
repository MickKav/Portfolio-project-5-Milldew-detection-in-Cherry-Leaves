import streamlit as st

# Define key sections
sections = ["Home", "Project Summary", "Data Exploration", "Model Performance", "Image Analysis", "Live Prediction", "Findings Page"]

# Page layout
page = st.sidebar.selectbox("Select a Section", sections)

# Render different pages based on user selection
if page == "Home":
    st.title("Cherry Leaves Mildew Detection Project")
    st.write("Brief overview and project introduction.")

elif page == "Project Summary":
    st.title("Project Summary")
    st.write("Dataset summary and client requirements.")

elif page == "Data Exploration":
    st.title("Data Exploration")
    st.write("Visualizations and insights gained during data analysis.")

# Add similar sections for other pages...

elif page == "Image Analysis":
    st.title("Image Analysis")
    st.write("Visualizations related to image analysis.")

elif page == "Findings Page":
    st.title("Findings Page")
    st.write("Visualizations and insights related to differentiating healthy and affected cherry leaves.")

# Add more sections as needed...