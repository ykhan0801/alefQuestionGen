import streamlit as st
import base64
import textwrap
from AlefDifferent import questions

finalText = ""
svgText = []
selectedQ = st.selectbox(
        "Question:", ("Trapezoid", "Triangle", "Pyramid", "Length", "Median", "RA Triangle"),key=f"id{1}")
quantity = int(st.text_input("Quantity", value="0"))

if st.button("Run"):
    st.write('You selected:', selectedQ)
    finalText, svgText = questions(selectedQ, quantity)

st.text_area("Questions and Answers", finalText, key=f"id{2}", height=500)

def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def render_svg_example():
    i=0
    for i in range(quantity):
        st.code(textwrap.dedent(svgText[i]), 'svg')
        render_svg(svgText[i])
        i+=1


if __name__ == '__main__':
    render_svg_example()





