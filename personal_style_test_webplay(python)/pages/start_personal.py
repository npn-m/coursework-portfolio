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
    st.markdown("<h1 style='text-align:center;'>Let's find your SEASON !</h1>",unsafe_allow_html=True)
    st.image(os.path.join(os.getcwd(),"picture", "6.png"))
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
                width: 220px;
            }
            </style>
            """,
            unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2,2,2])

    with col2:
        if st.button("Find Your Personal Color"):
            st.switch_page('pages/personal_test.py')
            st.rerun

        if st.button("Back to Home"):
            st.switch_page('pages/home.py')
            st.rerun()