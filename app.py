import streamlit as st



st.title("My Streamlit App")

modo = st.radio("Select mode:", ["Mode 1", "Mode 2"])
valor = st.number_input("Enter a value:", min_value=0, max_value=100, value=50)


if modo == "Mode 1":
    st.write(f"You selected Mode 1 with value: {valor}")
    # Add more functionality for Mode 1 here
elif modo == "Mode 2":
    st.write(f"You selected Mode 2 with value: {valor}")
    # Add more functionality for Mode 2 here    
    
    