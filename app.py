import streamlit as st



st.title("My Streamlit App")
celsius = st.number_input("Enter temperature in Celsius:")
fahrenheit = (celsius * 9/5) + 32
st.write(f"{celsius}°C is equal to {fahrenheit}°F")