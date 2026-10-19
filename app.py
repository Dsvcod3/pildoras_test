import streamlit as st



st.title("My Streamlit App")

modo = st.radio("Select mode:", ["Mode 1", "Mode 2", "Mode 3", "Mode 4", "Mode 5"])
valor = st.number_input("Enter a value:", min_value=0, max_value=100, value=50)


if modo == "Mode 1":
    st.write(f"You selected Mode 1 with value: {valor}")
    # Add more functionality for Mode 1 here
elif modo == "Mode 2":
    st.write(f"You selected Mode 2 with value: {valor}")
    # Add more functionality for Mode 2 here    
elif modo == "Mode 3":
    st.write(f"You selected Mode 3 with value: {valor}")
    # Add more functionality for Mode 3 here
elif modo == "Mode 4":
    st.write(f"You selected Mode 4 with value: {valor}")
    # Add more functionality for Mode 4 here
elif modo == "Mode 5":
    st.write(f"You selected Mode 5 with value: {valor}")
    # Add more functionality for Mode 5 here    
else:
    st.write("Please select a mode.")   
    
    
    

    
