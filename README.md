Project Overview

The goal of this project is to analyze historical climate and disaster data, identify patterns, and forecast future risks. By leveraging machine learning, the project provides actionable insights to help governments, policymakers, and disaster management authorities make data-driven decisions for mitigation, resource allocation, and climate adaptation planning.

Features:

Data Collection: Historical climate and disaster data were collected from official sources in CSV format for multiple regions.

Data Loading: The dataset is loaded using pandas in a Streamlit app for interactive exploration.

Data Preprocessing: Key features like lag values, rolling averages, percent changes, and risk trends are calculated. Dates are converted to datetime format for time-series analysis.

Model Training: Machine learning regression or classification models are trained using scikit-learn to learn patterns in climate risks or disaster occurrences. The trained model is saved as a .pkl file using joblib.

Forecasting: The saved model predicts climate risks or disaster probabilities for the next 36 months (3 years) for each selected region.

Visualization: Results are visualized using matplotlib, seaborn, or plotly as cumulative risk trends and percentage changes.

Deployment: The full interactive app is deployed using Streamlit in a VS Code environment.

Dataset:The original dataset is then change to clean_data.csv in order to a clear and simple understanding dataset.

The dataset includes historical climate and disaster records, with information such as:

Entity

Code

Year

air_total

household

pm25

ozone

Example file: clean_data.csv

Technology Stack

Programming Language: Python 3.9.11

Development Environment: VS Code

Forecasting & Modeling: scikit-learn

Data Processing: pandas, numpy

Visualization: matplotlib, seaborn, plotly

Web App Interface: Streamlit

How It Works

Load and preprocess data – Calculate lag values, rolling averages, percent changes, and risk trends.

Train model – Fit a machine learning model to historical data to learn patterns in climate risks.

Forecast future risks – Use the trained model to predict risk probabilities for the next 36 months.

Visualize results – Display cumulative trends and percentage changes to inform decision-making.

Interactive deployment – Users can explore forecasts and insights through a Streamlit app.

Applications

Identifying high-risk regions for climate-related disasters

Planning resource allocation for disaster management

Guiding climate adaptation strategies and mitigation policies

Informing governments and policymakers for proactive planning
