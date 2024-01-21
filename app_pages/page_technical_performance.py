import streamlit as st
import matplotlib.pyplot as plt
from src.machine_learning.evaluate_clf import load_test_evaluation

def technical_performance_body():
    st.title("Technical Performance")

    st.write("This page focuses on evaluating the technical performance of the Cherry Leaves Mildew Detection model.")

    version = 'v1'

    # Labels Distribution on Train, Validation, and Test Sets
    st.header("Train, Validation, and Test Set: Labels Frequencies")
    labels_distribution = plt.imread(f"notebooks/outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    # Example: Display confusion matrix, ROC curve, or other relevant visualizations
    st.header("Visualizations")
    st.write("Include visualizations that showcase the model's performance.")

    # Additional details, insights, or analysis related to technical performance
    st.header("Analysis and Insights")
    st.write("Provide any additional insights or analysis related to the technical performance of the model.")

    # Conclusion and recommendations
    st.header("Conclusion and Recommendations")
    st.write("Summarize the findings and make any recommendations for improvement if applicable.")
