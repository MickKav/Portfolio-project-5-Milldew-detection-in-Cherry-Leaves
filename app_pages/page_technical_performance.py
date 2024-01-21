import streamlit as st
import pandas as pd
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

    # Model History - Training Accuracy and Losses
    st.header("Model History")
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"notebooks/outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"notebooks/outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    # Generalized Performance on Test Set - Evaluation Metrics
    st.header("Generalized Performance on Test Set")
    evaluation_data = {
        'Metric': ['Loss', 'Accuracy'],
        'Value': [0.0355, 0.9976]
    }

    evaluation_df = pd.DataFrame(evaluation_data).set_index('Metric')
    st.dataframe(evaluation_df)

    # Conclusion and recommendations
    st.header("Conclusion and Recommendations")
    st.write("Summarize the findings and make any recommendations for improvement if applicable.")
