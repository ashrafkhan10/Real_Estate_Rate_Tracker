import streamlit as st
import joblib

# Load the saved model
try:
    model = joblib.load('pol.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'regression_model.pkl' exists in the current directory.")

# Dictionary to map region names to numerical values
region_mapping = {
    'Malad Mumbai': 0, 'Manpada Thane': 1, 'Dahisar Mumbai': 2, 'Central Mumbai': 3, 'Santacruz Mumbai': 4,
    'Vile Parle Mumbai': 5, 'Kalyan Thane': 6, 'Mira Road': 7, 'Andheri Mumbai': 8, 'Kalamboli Navi-Mumbai': 9,
    'Goregaon Mumbai': 10, 'Thane': 11, 'Ulwe Navi-Mumbai': 12, 'Palm Beach Navi-Mumbai': 13,
    'Koparkhairane Navi-Mumbai': 14, 'Dombivli Thane': 15, 'Vashi Navi-Mumbai': 16, 'South Mumbai': 17,
    'Charkop Mumbai': 18, 'Kasar Vadavali Thane': 19, 'Chakala Mumbai': 20, 'Seven Bunglow': 21,
    'Panvel Navi-Mumbai': 22, 'Kharghar Navi-Mumbai': 23, 'Mumbai Harbour': 24, 'Kandivali Mumbai': 25,
    'Jogeshwari Mumbai': 26, 'Hiranandani Thane': 27, 'Borivali Mumbai': 28, 'Majiwada Thane': 29,
    'Dadar Mumbai': 30, 'Badlapur Mumbai': 31, 'Verosva Mumbai': 32, 'Oshiwara Mumbai': 33,
    'Airoli Navi-Mumbai': 34, 'Gorai Mumbai': 35, 'Ghansoli Navi-Mumbai': 36, 'Marol Mumbai': 37,
    'Vasind Mumbai': 38, 'Taloja Navi-Mumbai': 39, 'Kopargaon Mumbai': 40, 'Matunga Mumbai': 41,
    'Balkum Thane': 42, 'Mitha Nagar Mumbai': 43, 'Mumbai Thane': 44, 'Kalher Thane': 45,
    'Khanda Colony Navi-Mumbai': 46, 'Vakola Mumbai': 47, 'Chipale Navi-Mumbai': 48, 'Naupada Thane': 49,
    'Wada Mumbai': 50, 'Jawahar Nagar': 51, 'Sakinaka Mumbai': 52, 'Ambernath Mumbai': 53,
    'Liberty Garden': 54, 'Shilphata Navi-Mumbai': 55, 'Nerul Navi-Mumbai': 56, 'Belapur Navi-Mumbai': 57,
    'Marve Road': 58, 'Shirdon Navi-Mumbai': 59, 'Titwala Mumbai': 60, 'Versova Mumbai': 61,
    'Neral Mumbai': 62, 'Thakurli Mumbai': 63, 'Kharegaon Mumbai': 64, 'Anjurdive Mumbai': 65,
    'Mahim Mumbai': 66, 'Seawoods Navi-Mumbai': 67, 'Dattanagar Mumbai': 68, 'Kamothe Navi-Mumbai': 69,
    'Walkeshwar Mumbai': 70, 'Khandeshwar Navi-Mumbai': 71, 'Ulhasnagar Mumbai': 72,
    'Adaigaon Navi-Mumbai': 73, 'Azad Nagar': 74, 'Palaspa Navi-Mumbai': 75, 'Shirgaon Mumbai': 76,
    'Bhagat Colony': 77, 'Ambika Nagar Mumbai': 78, 'Shastri Nagar': 79, 'Thakur Village': 80,
    'Shankar Pada': 81, 'Vichumbe Navi-Mumbai': 82, 'Khardipada Thane': 83, 'Roadpali Navi-Mumbai': 84,
    'Katemanivali Mumbai': 85, 'Rabale Navi-Mumbai': 86, 'Shahapur Mumbai': 87, 'Sai Nagar': 88,
    'Shivaji Nagar': 89, 'Teen-Hath-Naka Thane': 90, 'Sanpada Navi-Mumbai': 91, 'Village Navi-Mumbai': 92,
    'Kandarpada Mumbai': 93, 'Juhu Mumbai': 94, 'Kavesar Thane': 95, 'Bandhan Navi-Mumbai': 96,
    'Adharwadi Mumbai': 97, 'Sunder Nagar': 98, 'Dn Nagar': 99, 'Bhiwandi': 100, 'Evershine Nagar': 101,
    'Ranjanpada Navi-Mumbai': 102, 'Khandeshhwar Navi-Mumbai': 103, 'Sankalp Colony': 104,
    'Punjab Colony': 105, 'Nagar Navi-Mumbai': 106, 'Khadakpada Mumbai': 107, 'Karanjade Navi-Mumbai': 108,
    'Karade Khurd Navi-Mumbai': 109, 'Prakash Nagar': 110, 'Valivali Gaon Mumbai': 111,
    'Kulupwadi Mumbai': 112, 'Koyana Vele Navi-Mumbai': 113, 'Naupada Mumbai': 114, 'Kopri Thane': 115,
    'Sundervan Complex': 116, 'Yagna Nagar': 117, 'Palaspe Phata Navi-Mumbai': 118, 'Manjarli Mumbai': 119,
    'Vazira Mumbai': 120, 'Gauripada Mumbai': 121, 'Katrap Mumbai': 122, 'Koparkhairne Navi-Mumbai': 123,
    'Tilak Chowk Mumbai': 124, 'Chikuwadi Mumbai': 125, 'Wayle Nagar': 126, 'Mhatre Wadi': 127,
    'Manda Mumbai': 128, 'Dongripada Thane': 129, 'Asha Nagar': 130, 'Bunglows Mumbai': 131,
    'Patel Nagar': 132, 'Rasayani Navi-Mumbai': 133, 'Mahavir Nagar': 134, 'Point Charkop': 135,
    'Amboli Mumbai': 136, 'Natwar Nagar': 137, 'Rajan Pada': 138, 'Kapurbawadi Thane': 139,
    'Tower Dindoshi': 140, 'Nilje Gaon Mumbai': 141, 'Satya Nagar': 142, 'Manish Nagar': 143,
    'Jijamata Nagar Navi-Mumbai': 144
}

# Streamlit app content
st.title('Real Estate Rate Tracker App')

# Add input elements
region_options = list(region_mapping.keys())
region = st.selectbox('Region', region_options)  # Assuming categorical region feature
property_age = st.number_input('Property Age (years)', min_value=0)
area_type = st.selectbox('Area Type', ['Carpet area', 'Plot area', 'Built up area', 'Super built up area'])  # Assuming categorical area type feature
area_sqft = st.number_input('Area Square Feet', min_value=0)
rate_sqft = st.number_input('Rate Per Square Foot', min_value=0.0)
floor_no = st.number_input('Floor Number', min_value=0)
bedroom = st.number_input('Number of Bedrooms', min_value=0)

# Predict on button click
if st.button('Predict Price'):
    # Map selected region name to numerical value
    region_value = region_mapping[region]
    
    # Map selected area type to numerical value
    area_type_value = {
        'Carpet area': 1,
        'Plot area': 2,
        'Built up area': 0,
        'Super built up area': 3
    }[area_type]

    # Prepare the feature vector
    features = [[region_value, property_age, area_type_value, area_sqft, rate_sqft, floor_no, bedroom]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Display the prediction
    st.success(f'Predicted House Price (in Lakh): {prediction:.2f}')
