import streamlit as st
import joblib

# Load the saved model
try:
    model = joblib.load('pol.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'regression_model.pkl' exists in the current directory.")

# Streamlit app content
st.title('Real Estate Price Prediction App')

# Add input elements
region = st.selectbox('Region', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144])  # Assuming categorical region feature
property_age = st.number_input('Property Age (years)', min_value=0)
area_type = st.selectbox('Area Type', [0, 1, 2, 3])  # Assuming categorical area type feature
area_sqft = st.number_input('Area Square Feet', min_value=0)
rate_sqft = st.number_input('Rate Per Square Foot', min_value=0.0)
floor_no = st.number_input('Floor Number', min_value=0)
bedroom = st.number_input('Number of Bedrooms', min_value=0)

# Predict on button click
if st.button('Predict Price'):
    # Prepare the feature vector
    features = [[region, property_age, area_type, area_sqft, rate_sqft, floor_no, bedroom]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Display the prediction
    st.success(f'Predicted House Price (in Lakh):  { prediction:.2f}')
