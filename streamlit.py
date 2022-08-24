import streamlit as st
from AlefDifferent import questions

finalText = ""
selectedQ = st.selectbox(
        "Question:", ("Trapezoid", "Triangle", "Pyramid", "Length", "Median", "RA Triangle"),key=f"id{1}")
quantity = int(st.text_input("Quantity", value="0"))

if st.button("Run"):
    st.write('You selected:', selectedQ)
    finalText = questions(selectedQ, quantity)

st.text_area("Questions and Answers", finalText, key=f"id{2}", height=500)





