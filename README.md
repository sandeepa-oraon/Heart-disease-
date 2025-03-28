
# Heart Disease Prediction System
### Link : https://hrt-disease-predictpy-as.streamlit.app/#heart-disease-prediction-using-ml
## Overview

This project is a Heart Disease Prediction System built using Machine Learning and deployed with Streamlit. The model predicts the likelihood of heart disease based on various health parameters entered by the user.

## Features

- User-friendly interface using Streamlit

- Predicts heart disease risk based on user input

- Uses a gradient boosting model

- Interactive UI with real-time results

- Dataset

The model is trained on the Heart Disease Dataset of Machine Learning Repository. It contains health-related parameters such as:

- Age

- Serum cholesterol level

- Chest pain type

- Maximum heart rate achieved

- ST depression induced by exercise

- Number of major vessels colored by fluoroscopy

- Exercise-induced angina

## Technologies Used

- Python
- Scikit-Learn/sklearn (Machine Learning model)
- Matplotlib (visualization)
- Streamlit (Web application framework)
- Pandas & NumPy (Data processing)
- GitHub & Streamlit Cloud (Deployment)

## Installation

- Clone the repository:

git clone https://github.com/sandeepa-oraon/Heart-disease-.git

- Navigate to the project directory:

cd Heart-disease-

- Install dependencies:

pip install -r requirements.txt

- Run the application:

streamlit run HDpredict.py


## Project Structure

├── HDModel.sav          # Trained Machine Learning model

├── HDpredict.py         # Streamlit application script

├── heart.csv            # Dataset used for training

├── requirements.txt     # Dependencies

├── main3Copy.ipynb          # Jupyter Notebook for training & testing

└── README.md            # Project Documentation


