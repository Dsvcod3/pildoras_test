import streamlit as st



st.title("My Streamlit App")

modo = st.radio("Select mode:", ["Mode 1", "Mode 2", "Mode 3", "Mode 4", "Mode 5"])
valor = st.number_input("Enter a value:", min_value=0, max_value=100, value=50)




match modo:
    case "Mode 1":
        st.write(f"You selected Mode 1 with value: {valor}")
    case "Mode 2":
        st.write(f"You selected Mode 2 with value: {valor}")    
            
    case "Mode 3":
        st.write(f"You selected Mode 3 with value: {valor}")
    case "Mode 4":
        st.write(f"You selected Mode 4 with value: {valor}")
    case "Mode 5":
        st.write(f"You selected Mode 5 with value: {valor}")
    case _:
        st.write("Invalid mode selected.")    
        
        
    
    
    

    
