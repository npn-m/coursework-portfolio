import streamlit as st
import os
from streamlit_card import card
import base64

with open("C:\\Users\\ASUS\\Desktop\\python pj\\picture\\4.png", "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
img1 = "data:image/png;base64," + encoded.decode("utf-8")

with open("C:\\Users\\ASUS\\Desktop\\python pj\\picture\\5.png", "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
img2 = "data:image/png;base64," + encoded.decode("utf-8")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt&display=swap');
h1, h2, h3, p, div, a {
    font-family: 'Prompt', sans-serif;
}
</style>
""", unsafe_allow_html=True)

class Main:
    st.markdown("<h1 style='text-align:center;'>LET'S FIND WHAT IS SUITED YOU MOST !</h1>", unsafe_allow_html=True)
    st.divider()
    st.image(os.path.join(os.getcwd(), "picture", "PERSONAL COLOR.png"))
    part1, part2, part3 = st.columns([1, 0.05, 1])
    with part1:
        st.write("")
        st.markdown("""<div style='text-align:center; font-weight:600;'><span style='font-size:23px;'>อยากรู้ว่าโทนสีไหนที่ทำให้คุณเด่น ?</span>
                    <span style='font-size:18px;'>มาทำ Personal Color Test แล้วค้นหาสไตล์ที่ใช่กันเถอะ !</span></div>""", unsafe_allow_html=True)
        st.write("")
        pers_test = card(
            title="PERSONAL TEST",
            text="",
            image=img1,
            styles={
                "card": {
                    "margin": "auto",
                    "width": "300px",
                    "height": "300px"
                },
                "filter": {
                    "background-color": "rgba(0, 0, 0, 0)"
                }
            }
        )

        if pers_test:
            st.switch_page("pages/start_personal.py")
            st.rerun()

    with part2:
        st.write("")
        st.write("")
        st.markdown(
            """
            <style>
            .divider {
                height: 55vh;
                border-left: 2px solid gray;
                margin: 0 auto;
            }
            </style>
            <div class="divider"></div>
            """,
            unsafe_allow_html=True,
        )

    with part3:
        st.write("")
        st.markdown("""<div style='text-align:center; font-weight:600;'><span style='font-size:23px;'>อยากรู้สไตล์ที่ปังที่สุดสำหรับคุณ ?</span>
                    <span style='font-size:18px;'>มาทำ Style Test แล้วหาลุคที่ใช่กันเลย !</span></div>""", unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        style_test = card(
            title="STYLE TEST",
            text="",
            image=img2,
            styles={
                "card": {
                    "margin": "auto",
                    "width": "300px",
                    "height": "300px"
                },
                "filter": {
                    "background-color": "rgba(0, 0, 0, 0)"
                }
            }
        )

        if style_test:
            st.switch_page("pages/start_style.py")
            st.rerun()

    st.write("")
    st.write("")