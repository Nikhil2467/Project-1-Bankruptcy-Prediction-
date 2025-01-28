
import streamlit as st
import pickle
import numpy as np

# Load the trained model
filename = 'Trained_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Function to make predictions using the loaded model
def predict(features):
    # Convert features to a numpy array and reshape for a single sample
    features = np.array(features).reshape(1, -1)
    prediction = loaded_model.predict(features)
    return prediction[0]

def main():
    st.title('Welcome To Our Prediction App:thumbsup:')
    html_temp = """
    <div style="background-color:skyblue;padding:10px">
    <h2 style="color:white;text-align:center;">Bankruptcy Prevention App </h2>
    </div>
    <h3 style="color:black;text-align:center;">Enter the details to predict bankruptcy:</h3>
    """
    
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    # Input fields for each feature
    industrial = st.number_input("Industrial", min_value=0.0, max_value=100.0)
    management_risk = st.number_input("Management Risk", min_value=0.0, max_value=100.0)
    financial_flexibility = st.number_input("Financial Flexibility", min_value=0.0, max_value=100.0)
    credibility = st.number_input("Credibility", min_value=0.0, max_value=100.0)
    competitiveness = st.number_input("Competitiveness", min_value=0.0, max_value=100.0)
    operating_risk = st.number_input("Operating Risk", min_value=0.0, max_value=100.0)
    
    # Collect the features into a list
    features = [industrial, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]

    if st.button("Predict"):
        prediction = predict(features)
        
        if prediction == 1:
            st.write("The company is predicted to go bankrupt.")
        else:
            st.write("The company is predicted not to go bankrupt.")

if __name__=='__main__':
    main()
