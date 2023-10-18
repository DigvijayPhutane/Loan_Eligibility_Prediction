# Loan_Eligibility_Prediction
Loan Eligibility Prediction project using SVM with Machine Learning Python for making loan approval predictions.

# Loan Eligibility Prediction Web Application

**Author**: Digvijay Phutane

## Overview

This web application predicts loan eligibility using a Support Vector Machine (SVM) classifier. It includes an exploratory data analysis (EDA) phase, data preprocessing, model training, and a user-friendly web interface for making loan approval predictions.

## Project Structure

- `app.py`: The Flask application that serves as the web interface for loan eligibility prediction.
- `loan_approval_model.sav`: A pre-trained SVM classifier model saved using the Pickle library.
- `templates/`: Directory containing HTML templates for the web interface.
- `data/`: Directory containing the dataset used for model training and EDA.
- `notebooks/`: Jupyter notebooks used for EDA and model training.
- `README.md`: This file.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed. You can check the installed version with the following command:

python --version

### Installation

1. Clone this repository

2 Install the libraries mentioned in the code

Usage
Run the Flask application:
python app.py

Access the web interface by opening a web browser and navigating to http://localhost:5000.

Fill out the form with the required information (e.g., gender, marital status, education, income, etc.) and click "Predict Loan Approval."

The web interface will display the loan approval prediction, either "Congratulations! Your loan is approved" or "Sorry, your loan is not approved."

Model Selection
We used a Support Vector Machine (SVM) classifier to predict loan eligibility. This model was selected based on its higher accuracy compared to other algorithms like K-Nearest Neighbors (KNN). The SVM model has been trained on a pre-processed dataset and saved for later use in the Flask application.

Data
The dataset used for this project includes various features such as gender, marital status, education, income, credit history, and property area. The data was preprocessed to handle categorical features and make it suitable for machine learning.

loan_train.csv
