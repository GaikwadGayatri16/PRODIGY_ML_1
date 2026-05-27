import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# UI Title
st.title("🏠 House Price Prediction App")

st.write("Enter house details below:")

# Input fields (same order as training)
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedroom", min_value=0)
bathrooms = st.number_input("Bathroom", min_value=0)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₹ {int(prediction[0])}")