import streamlit as st
from model_training import train_model, evaluate_model
from data_preprocessing import load_dataset, preprocess_data
from app_pages import home, project_summary, data_exploration, model_performance, image_analysis, live_prediction, findings_page

def show_home():
    home.show_home()

def show_project_summary():
    project_summary.show_project_summary()

def show_data_exploration():
    data_exploration.show_data_exploration()

def show_model_performance():
    model_performance.show_model_performance()

def show_image_analysis():
    image_analysis.show_image_analysis()

def show_live_prediction():
    live_prediction.show_live_prediction()

def show_findings_page():
    findings_page.show_findings_page()

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

    selected_page = st.sidebar.selectbox("Select a Section", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()