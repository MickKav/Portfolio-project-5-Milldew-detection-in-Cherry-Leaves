import streamlit as st
from model_training import train_model, evaluate_model
from data_preprocessing import load_dataset, preprocess_data
from app_pages import home, project_summary, data_exploration, model_performance, image_analysis, live_prediction, findings_page

def main():
    st.title("Cherry Leaves Mildew Detection App")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = {
        "Home": home.show_home,
        "Project Summary": project_summary.show_project_summary,
        "Data Exploration": data_exploration.show_data_exploration,
        "Model Performance": model_performance.show_model_performance,
        "Image Analysis": image_analysis.show_image_analysis,
        "Live Prediction": live_prediction.show_live_prediction,
        "Findings Page": findings_page.show_findings_page,
    }

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["Home", "Project Summary", "Data Exploration", 
                                "Model Performance", "Image Analysis", "Live Prediction", "Findings Page"])

    # Display the selected page
    if page == "Home":
        home.show_home()
    elif page == "Project Summary":
        project_summary.show_project_summary()
    elif page == "Data Exploration":
        data_exploration.show_data_exploration()
    elif page == "Model Performance":
        model_performance.show_model_performance()
    elif page == "Image Analysis":
        image_analysis.show_image_analysis()
    elif page == "Live Prediction":
        live_prediction.show_live_prediction()
    elif page == "Findings Page":
        findings_page.show_findings_page()

if __name__ == "__main__":
    main()