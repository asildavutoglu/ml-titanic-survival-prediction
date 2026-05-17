import pickle 
import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

st.title("🚢 Titanic Survival Prediction")
st.write("Bu uygulama, yolcu bilgilerine göre Titanic'te hayatta kalma ihtimalini tahmin eder.")


with open("model.pkl", "rb") as file:
    model = pickle.load(file)


st.header("Yolcu Bilgileri")

pclass = st.selectbox(
    "Bilet Sınıfı",
    options=[1, 2, 3],
    help="1 = Birinci sınıf, 2 = İkinci sınıf, 3 = Üçüncü sınıf"
)

sex = st.selectbox(
    "Cinsiyet",
    options=["male", "female"]
)

age = st.slider(
    "Yaş",
    min_value=0,
    max_value=100,
    value=25
)

sibsp = st.number_input(
    "Gemideki kardeş/eş sayısı",
    min_value=0,
    max_value=10,
    value=0
)

parch = st.number_input(
    "Gemideki ebeveyn/çocuk sayısı",
    min_value=0,
    max_value=10,
    value=0
)

fare = st.number_input(
    "Bilet ücreti",
    min_value=0.0,
    max_value=600.0,
    value=50.0
)

embarked = st.selectbox(
    "Gemiye binilen liman",
    options=["C", "Q", "S"],
    help="C = Cherbourg, Q = Queenstown, S = Southampton"
)


sex_encoded = 0 if sex == "male" else 1

embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0


input_data = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex_encoded],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Embarked_Q": [embarked_Q],
    "Embarked_S": [embarked_S]
})


st.subheader("Modele Gönderilen Veri")
st.dataframe(input_data)


if st.button("Tahmin Et"):
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    survival_probability = prediction_proba[1] * 100

    if prediction == 1:
        st.success(f"Bu yolcunun hayatta kalma ihtimali yüksek. Olasılık: %{survival_probability:.2f}")
    else:
        st.error(f"Bu yolcunun hayatta kalma ihtimali düşük. Olasılık: %{survival_probability:.2f}")