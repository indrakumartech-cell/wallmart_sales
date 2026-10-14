import streamlit as st
import pickle
import pandas as pd

# Saved model load karte hain
with open('walmart_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🛒 Walmart Weekly Sales Prediction App")
st.write("Aap apne store ki details daal kar weekly sales predict kar sakte hain.")

# User inputs ke liye fields banate hain
store = st.number_input("Store Number (1-45)", min_value=1, max_value=45, value=20)
holiday_flag = st.selectbox("Holiday Flag (0 = Normal, 1 = Holiday)", [0, 1])
temp = st.number_input("Temperature", value=70.0)
fuel_price = st.number_input("Fuel Price", value=3.5)
cpi = st.number_input("CPI", value=211.0)
unemployment = st.number_input("Unemployment Rate", value=8.1)
year = st.number_input("Year", value=2011)
month = st.number_input("Month", min_value=1, max_value=12, value=5)
day = st.number_input("Day", min_value=1, max_value=31, value=15)

# Predict button
if st.button("Predict Sales"):
    input_data = pd.DataFrame([[store, holiday_flag, temp, fuel_price, cpi, unemployment, year, month, day]], 
                              columns=['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Year', 'Month', 'Day'])
    
    prediction = model.predict(input_data)
    st.success(f"Predicted Weekly Sales: ₹{prediction[0]:,.2f}")