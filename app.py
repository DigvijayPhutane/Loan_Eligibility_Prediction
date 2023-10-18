from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the SVM model
with open('loan_approval_model.sav', 'rb') as model_file:
    svm_classifier = pickle.load(model_file)

# Create a route to render the loan prediction form
@app.route('/')
def loan_form():
    return render_template('loan_form.html')

# Function to handle the mapping of 'Dependents' string to a numeric value
def map_dependents(dependents_str):
    if dependents_str == '0':
        return 0
    elif dependents_str == '1':
        return 1
    elif dependents_str == '2':
        return 2
    elif dependents_str == '3':
        return 3
    elif dependents_str == '3+':
        return 4

# Create a route to handle the form submission and display results
@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    # Get input data from the form
    gender = request.form['gender']
    married = request.form['married']
    dependents = map_dependents(request.form['dependents'])
    education = request.form['education']
    self_employed = request.form['self_employed']
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = request.form['credit_history']
    property_area = request.form['property_area']

    # Reverse the encoding for the prediction
    gender = 1 if gender == 'Male' else 0
    married = 1 if married == 'Yes' else 0
    self_employed = 1 if self_employed == 'Yes' else 0
    property_area = 0 if property_area == 'Rural' else (1 if property_area == 'Semiurban' else 2)
    education = 1 if education == 'Graduate' else 0
    credit_history = 1 if credit_history == 'Yes' else 0

    # Make a prediction using the SVM classifier
    features = np.array([gender, married, dependents, education, self_employed, applicant_income,
                         coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]).reshape(1, -1)
    prediction = svm_classifier.predict(features)

    # Map the prediction to 'Yes' or 'No' based on your encoding
    loan_status = 'Yes' if prediction[0] == 1 else 'No'

    # Render the result page
    return render_template('loan_result.html', loan_status=loan_status)

if __name__ == '__main__':
    app.run(debug=True)
