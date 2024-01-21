import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_project_summary import show_project_summary
from app_pages.page_visualizer import leaves_visualizer
from app_pages.page_mildew_detector import mildew_detection_body
from app_pages.page_hypothesis import hypothesis_validation

app = MultiPage(app_name="Cherry Leaves Mildew Detection")  # Modify the app name

app.add_page("Project Summary", show_project_summary)
app.add_page("Data Visualizer", leaves_visualizer)
app.add_page("Mildew Detection", mildew_detection_body)
app.add_page("Hypothesis Validation", hypothesis_validation)

app.run()