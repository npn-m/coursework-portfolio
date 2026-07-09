import streamlit as st
import os

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt&display=swap');
h1, h2, h3, p, div, a {
    font-family: 'Prompt', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:40px; font-weight:bold;'>ยินดีต้อนรับสู่ Refined Radiance ที่คุณจะค้นพบ..</p>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    st.image(os.path.join(os.getcwd(),"picture", "0.png"))
    st.markdown("<p style='text-align:center; font-size:18px;'>ความงามที่ไม่ซ้ำใครด้วยสีสันและสไตล์ที่สมบูรณ์แบบสำหรับคุณ เปล่งประกายด้วยความมั่นใจในทุกวัน พร้อมแต่งตัวให้เข้ากับโทนสีที่ช่วยเสริมเสน่ห์และสะท้อนตัวตนของคุณอย่างแท้จริง.</p>", unsafe_allow_html=True)
    st.image(os.path.join(os.getcwd(),"picture", "1.png"))
    st.markdown("<p style='text-align:center; font-size:18px;'>Find your Personal Color&Style ค้นหาสีและสไตล์ที่ใช่สำหรับคุณ เพิ่มความมั่นใจให้ลุคปังทุกวัน! ไปเริ่มกันเลย!!</p>", unsafe_allow_html=True)
    st.image(os.path.join(os.getcwd(),"picture", "2.png"))
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
                width: 200px;
            }
            </style>
            """,
            unsafe_allow_html=True
    )
    col1,col2,col3=st.columns([1,1,1])
    with col2:
        if st.button("START !"):
                st.switch_page("pages/home.py")
                st.rerun()
    