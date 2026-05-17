# Titanic Survival Prediction

This is a beginner-friendly machine learning project that predicts whether a Titanic passenger survived or not based on passenger information.

## Project Overview

The goal of this project is to build a machine learning model using the Titanic dataset.

The model predicts survival using features such as:

- Passenger class
- Sex
- Age
- Family size
- Ticket fare
- Embarked port

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- Streamlit
- Jupyter Notebook

## Dataset

The dataset used in this project is the Titanic dataset from Kaggle.

Target column:

- `Survived`
  - `0` = Not survived
  - `1` = Survived

## Project Structure

```text
ml-titanic-survival-prediction/
├── data/
├── notebooks/
├── app.py
├── model.pkl
├── README.md
├── requirements.txt
└── .gitignore
```

## Machine Learning Workflow

1. Loaded the Titanic dataset
2. Explored the data
3. Checked missing values
4. Cleaned and preprocessed the dataset
5. Converted categorical variables into numerical values
6. Split the data into training and test sets
7. Trained a Random Forest Classifier
8. Evaluated the model using accuracy, confusion matrix, and classification report
9. Built a Streamlit web app for predictions

## Model

The machine learning model used in this project:

- Random Forest Classifier

## How to Run This Project

Clone the repository:

```bash
git clone https://github.com/asildavutoglu/ml-titanic-survival-prediction.git
cd ml-titanic-survival-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Example App Inputs

The Streamlit app takes the following passenger information:

- Passenger class
- Sex
- Age
- Number of siblings/spouses aboard
- Number of parents/children aboard
- Ticket fare
- Embarked port

Then it predicts whether the passenger is likely to survive.

## Results

The model achieved around 80% accuracy on the test set.

## Future Improvements

- Try different machine learning models
- Add hyperparameter tuning
- Add more feature engineering
- Deploy the Streamlit app online
- Add screenshots to the README