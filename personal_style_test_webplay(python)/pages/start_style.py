import streamlit as st
import os

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt&display=swap');
h1, h2, h3, p, div, a {
    font-family: 'Prompt', sans-serif;
}
</style>
""", unsafe_allow_html=True)

class Main:
    st.markdown("<h1 style='text-align:center;'>Let's find your STYLE !</h1>",unsafe_allow_html=True)
    st.image(os.path.join(os.getcwd(), "picture", "7.png"))
    st.markdown("<h2 style='text-align:center;'>Are You READY ?</h2>",unsafe_allow_html=True)
    
    st.markdown(
            """
            <style>
            .center-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .stButton button {
                width: 200px; /* ปรับขนาดปุ่ม */
            }
            </style>
            """,
            unsafe_allow_html=True
    )

    col4, col5, col6 = st.columns([2,2,2])

    with col5:
        if st.button("Find your Style"):
            st.switch_page('pages/style_test.py')
            st.rerun()
            
        if st.button("Back to Home"):
            st.switch_page('pages/home.py')
            st.rerun()