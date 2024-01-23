![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Cherry Leaves Mildew Detection

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into [CodeAnywhere](https://app.codeanywhere.com/) with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. In the terminal type `pip3 install jupyter`

1. In the terminal type `jupyter notebook --NotebookApp.token='' --NotebookApp.password=''` to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to Account Settings in the menu under your avatar.
2. Scroll down to the API Key and click Reveal
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with Regenerate API Key.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

As a Data Analyst from Code Institute Consulting, you are requested by Farmy & Foods to provide actionable insights and data-driven recommendations to a assist the client due to the manual process of thousands of cherry trees located in multiple farms across the country. This is not scalable due to time spent in the manual process inspection. 

The client has requested we create an ML system that is capable of detecting instantly, using a tree leaf image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops.


## Hypothesis and how to validate?

* **Hypothesis 1**: Powdery mildew-affected cherry leaves have distinct visual patterns, especially in the affected areas.
  - *Validation*: Conduct an image analysis study to identify and quantify the visual patterns associated with powdery mildew. Compare the visual features of healthy and affected leaves.

* **Hypothesis 2**: Machine learning models can effectively classify cherry leaves as healthy or powdery mildew-affected based on visual features.
  - *Validation*: Train and evaluate machine learning models using the dataset to predict the health status of cherry leaves. Use metrics such as accuracy, precision, and recall for validation.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* **Business Requirement 1**: Conducting a study to visually differentiate healthy and affected cherry leaves.
  - *Rationale*: Utilize data visualizations to showcase the identified visual patterns associated with powdery mildew. This could include heatmaps, image overlays, or side-by-side comparisons.

* **Business Requirement 2**: Predicting if a cherry leaf is healthy or contains powdery mildew.
  - *Rationale*: Implement machine learning tasks to build classifiers capable of making predictions based on the identified visual features. Visualize model predictions and showcase model performance metrics.

## ML Business Case

* **Project Name**: Portfolio-project-5-Milldew-detection-in-Cherry-Leaves
* **Objective**: Develop an ML model to predict if a cherry leaf is healthy or affected by powdery mildew.
* **Ideal Outcome**: Provide a fast and accurate diagnostic tool for detecting powdery mildew in cherry leaves.
* **Success Metrics**: Achieve an accuracy of 80% or above on the test set.
* **Model Output**: Binary classification indicating whether the cherry leaf is healthy or affected, along with associated probabilities.
* **Heuristics**: The current manual inspection process is time-consuming and not scalable. The ML model aims to provide quick and reliable detection, enabling efficient treatment of affected trees.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Project Summary
* General Information
  - Powdery mildew is a fungal disease of the foliage, stems and occasionally flowers and fruit where a superficial fungal growth covers the surface of the plant.
  - Our goal is to create an ML model to help identify this mildew on cherry leaves so the adequate precautions can be taken by the client.
* Project Dataset
  - The available dataset contains over 4 thousand images in both healthy and powdery mildew folders which have kindly been provided by the client and other business partners.
* Link to Additional Information
  - References and external links related to powdery mildew and cherry [link here](https://www.rhs.org.uk/disease/powdery-mildews).
* Business Requirements
  * 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
  * 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Visualizations
* Here we will answer business requirement 1
  - Checkbox 1 - Difference between average and variability image
  - Checkbox 2 - Visualize the differences between healthy and affected cherry leaves.
  - Checkbox 3 - Image Montage

* Display identified visual patterns associated with powdery mildew.

### Page 3: ML Model Performance
* Showcase the trained ML model's accuracy, precision, and recall.
* Display confusion matrix and other relevant metrics.
* Provide insights into the model's predictive capabilities.

### Page 4: Live Prediction
* User Interface with an image uploader widget for live prediction.
* Display the uploaded image and the model's prediction.
* Include probability scores and a concise result statement.

### Page 5: Project Hypothesis and Validation
* Section to detail each hypothesis, the methodology used for validation, and the outcomes.
* Highlight the importance of hypotheses in guiding the project.

### Page 6: Unfixed Bugs
* There were no unfixed bugs at point of deployment

# Deployment
### Heroku

* The App live link is: [Click Here for app link](https://mildew-detection-project-5-e5da9f4e8a7b.herokuapp.com/)
* Set the runtime.txt  to Python 3.8.17 and a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
In this project, the following libraries were used for data analysis and machine learning tasks:

- **pandas==1.1.2:** Used for data manipulation, cleaning, and exploratory data analysis.
- **numpy>=1.19.2:** Utilized for numerical operations and array manipulations, particularly in preprocessing data for machine learning models.
- **matplotlib==3.3.1:** Employed for creating visualizations such as plots and charts to better understand the dataset and model performance.
- **plotly==4.12.0:** Used for interactive visualizations, enhancing the presentation of data insights in the project.
- **seaborn==0.11.0:** Utilized for statistical data visualization, complementing Matplotlib to create aesthetically pleasing and informative visualizations.
- **tensorflow-cpu==2.6.0:** Implemented for building and training machine learning models, particularly neural networks using the TensorFlow framework.
- **streamlit==0.85.0:** Utilized for creating interactive and user-friendly web applications, enabling the deployment of machine learning models.
- **keras==2.6.0:** Employed for building and training deep learning models, providing a high-level neural networks API.

## Credits
* I'd like to mention taking reference from the Walkthrough project 1 malaria detection project, from where i got a quantity of code for the notebooks, and got extra help from slack and stack overflow.
* The images used for the gallery page were taken from kaggle.

## Acknowledgements (optional)
* Thanks to Niel McEwen for guidance with the project.