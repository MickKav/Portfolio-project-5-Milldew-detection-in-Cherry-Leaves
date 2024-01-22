import streamlit as st
import matplotlib.pyplot as plt

# Function to show hypothesis validation page
def hypothesis_validation():

    st.title("Hypothesis Validation")

    st.header("Hypotheses:")
    
    # Hypothesis 1
    st.subheader("Hypothesis 1:")
    st.info("We suspect that mildewed cherry leaves exhibit distinct visual patterns that differentiate them from healthy leaves.")

    # Validation for Hypothesis 1
    st.subheader("Validation:")
    st.write("To validate this hypothesis, we will analyze the growth characteristics of mildewed leaves.")
    st.error("Symptoms to look for include curled leaves, smaller and pale leaves, distorted growth, and the presence of a whitish fungus.")

    with st.beta_expander("View Mildewed Leaves Examples"):
        # You can add multiple images here to showcase examples of mildewed leaves
        mildewed_leaf_image_1 = "notebooks/inputs/cherry_leaves_dataset/cherry-leaves/train/powdery_mildew/0ceb54ca-c9c1-48fb-9b8c-eb8afaefc378___FREC_Pwd.M 4698_flipLR.JPG"
        mildewed_leaf_image_2 = "notebooks/inputs/cherry_leaves_dataset/cherry-leaves/train/powdery_mildew/0c22dfef-7413-4f46-b949-903d238678a3___FREC_Pwd.M 5094_flipLR.JPG"
        mildewed_leaf_image_3 = "notebooks/inputs/cherry_leaves_dataset/cherry-leaves/train/powdery_mildew/00e0a4ab-ecbd-4560-a71c-b19d86bb087c___FREC_Pwd.M 4917_flipLR.JPG"

        st.image([mildewed_leaf_image_1, mildewed_leaf_image_2, mildewed_leaf_image_3], caption=["Mildewed Leaf 1", "Mildewed Leaf 2", "Mildewed Leaf 3"])

    st.warning("Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.")
