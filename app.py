import streamlit as st
import pickle as pc
import numpy as np

def fruad_prediction(input_data):
    loaded_model = pc.load(open('trained_model.sav','rb'))
    reshaped_array = np.array(input_data).reshape(1, -1)
    prediction = loaded_model.predict(reshaped_array)
    
    if (prediction[0] == 0):
        return 'The Transaction is Not Fraud'
    else:
        return 'The Transaction is Fraud'
    
def main():
    st.title("Fraud Detection App")
    st.markdown("---")

    st.sidebar.header("User Input")
    step = st.sidebar.number_input("Step", value=1)
    amount = st.sidebar.number_input("Amount", value=0.0)
    oldbalanceOrg = st.sidebar.number_input("Old Balance Origin", value=0.0)
    newbalanceOrig = st.sidebar.number_input("New Balance Origin", value=0.0)
    oldbalanceDest = st.sidebar.number_input("Old Balance Destination", value=0.0)
    newbalanceDest = st.sidebar.number_input("New Balance Destination", value=0.0)

    if st.button('Detect Fraud'):
        input_data = [
            int(step), float(amount), float(oldbalanceOrg),
            float(newbalanceOrig), float(oldbalanceDest), float(newbalanceDest)
        ]
        diagnosis = fruad_prediction(input_data)
        st.success(diagnosis)

    st.sidebar.markdown("---")
    st.sidebar.info(
        "This app is for demonstration purposes only. Always verify results "
        "from a professional source before making any financial decisions."
    )
    st.sidebar.markdown("---")
    st.sidebar.text("Your additional information here")

if __name__ == '__main__':
    main()