import streamlit as st
import os
import pandas as pd
from streamlit_card import card
import base64

info = pd.read_excel("C:\\Users\\ASUS\\Desktop\\python pj\\pages\\info.xlsx", sheet_name=['Seasons','Jewelry'])
s = info['Seasons']
s = s.set_index('Seasons')
j = info['Jewelry']
jewel = j.set_index('Under_Tone')

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

class get_info:
    def __init__(self, ans):
        self.ans = ans

    def Feature(self):
        if ("Blonde/Light Color" in self.ans) and ("Blue/Light Brown" in self.ans):
            self.feature = 'Light'
        else:
            self.feature = 'Dark'
        return self.feature

    def Undertone(self):
        if ("Red Undertone" in self.ans) and ("Purple/Blue" in self.ans):
            self.un_tone = 'Cool Tone'
        elif ("Golden Undertone" in self.ans) and ("Green/Olive Green" in self.ans):
            self.un_tone = 'Warm Tone'
        else:
            self.un_tone = 'Neutral Tone'
        return self.un_tone

class personal(get_info):
    def __init__(self, ans):
        super().__init__(ans)
        self.feature = self.Feature()
        self.un_tone = self.Undertone()
        self.pers = ''

    def pers_t(self):
        if self.un_tone == 'Cool Tone':
            if self.feature == 'Light':
                self.pers = 'Summer'
            else:
                self.pers = 'Winter'
        elif self.un_tone == 'Warm Tone':
            if self.feature == 'Light':
                self.pers = 'Spring'
            else:
                self.pers = 'Autumn'
        else :
            if self.feature == 'Light':
                self.pers = 'All Seasons'
            else:
                self.pers = 'Autumn&Summer'
        return self.pers


st.markdown("<h1 style='text-align:center;'>Let's find your PERSONAL COLOR !</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")

questions = {
    "Find your FEATURE": [
        ("What is your hair color ?", ["Blonde/Light Color", "Black/Dark Color"]),
        ("What is your eye color ?", ["Blue/Light Brown", "Black/Dark Brown"]),
    ],
    "Find your UNDERTONE": [
        ("What is your skin like after the sun ?", ["Red Undertone", "Golden Undertone"]),
        ("What is the color of your blood vessel ?", ["Purple/Blue", "Green/Olive Green", "Blue/Green"]),
    ]
}

img = {
    "Find your FEATURE": [
        (os.path.join("picture", "8.png"), [
            (os.path.join("picture", "9.png"), "Blonde/Light Color"),
            (os.path.join("picture", "10.png"), "Black/Dark Color"),
        ]),
        (os.path.join("picture", "12.png"), [
            (os.path.join("picture", "13.png"), "Blue/Light Brown"),
            (os.path.join("picture", "14.png"), "Black/Dark Brown"),
        ]),
    ],
    "Find your UNDERTONE": [
        (os.path.join("picture", "16.png"), [
            (os.path.join("picture", "17.png"), "Red Undertone"),
            (os.path.join("picture", "18.png"), "Golden Undertone"),
        ]),
        (os.path.join("picture", "20.png"), [
            (os.path.join("picture", "21.png"), "Purple/Blue"),
            (os.path.join("picture", "23.png"), "Green/Olive Green"),
            (os.path.join("picture", "22.png"), "Blue/Green"),
        ]),
    ],
}



if "current_q_img" not in st.session_state:
    st.session_state.current_q_img = img["Find your FEATURE"][0][0]
if "current_op_img" not in st.session_state:
    st.session_state.current_op_img = img["Find your FEATURE"][0][1]

total_questions = sum(len(q_list) for q_list in questions.values())

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state or len(st.session_state.answers) != total_questions:
    st.session_state.answers = [""] * total_questions

if "show_results" not in st.session_state:
    st.session_state.show_results = False

progress = (st.session_state.question_index + 1) / total_questions

if st.session_state.question_index < 2:
    progress_texts = ["Find your FEATURE", "Find your UNDERTONE", "FINISH"]
    progress_styles = ["font-size: 28px;", "font-size: 18px;", "font-size: 18px;"]
elif st.session_state.question_index < 3:
    progress_texts = ["Find your FEATURE", "Find your UNDERTONE", "FINISH"]
    progress_styles = ["font-size: 18px;", "font-size: 28px;", "font-size: 18px;"]
elif st.session_state.question_index == 3:
    progress_texts = ["Find your FEATURE", "Find your UNDERTONE", "FINISH"]
    progress_styles = ["font-size: 18px;", "font-size: 18px;", "font-size: 28px;"]

st.markdown(f"""
    <style>
    .progress-container {{
        position: relative;
        width: 100%;
        text-align: center;
    }}
    .progress-text {{
        position: absolute;
        top: -25px;
        width: 50%;
        display: inline-block;
        font-weight: bold;
    }}
    .progress-text:nth-child(1) {{
        left: 0%;
        text-align: left;
        {progress_styles[0]}
    }}
    .progress-text:nth-child(2) {{
        left: 40%;
        text-align: left;
        {progress_styles[1]}
    }}
    .progress-text:nth-child(3) {{
        right: 0%;
        text-align: right;
        {progress_styles[2]}
    }}
    </style>

    <div class="progress-container">
        <span class="progress-text">{progress_texts[0]}</span>
        <span class="progress-text">{progress_texts[1]}</span>
        <span class="progress-text">{progress_texts[2]}</span>
    </div>
    """, unsafe_allow_html=True)

st.progress(progress)

if st.session_state.question_index < total_questions:
    img_list = list(img.keys())
    question_list = list(questions.keys())
    current_topic = question_list[st.session_state.question_index // 2]
    current_question_index = st.session_state.question_index % 2
    current_question, current_options = questions[current_topic][current_question_index]
    
    st.image(img[current_topic][current_question_index][0])
    st.markdown(f"### {current_question}")

    cols = st.columns(len(current_options))
    selected_answer = None
    
    for i, option in enumerate(current_options):
        with cols[i]:
            st.image(img[current_topic][current_question_index][1][i][0])
            if st.checkbox(option, key=f"option_{st.session_state.question_index}_{i}"):
                selected_answer = option

    col, col1, col2, col3 = st.columns([0.3, 1, 3, 1])

    with col1:
        if st.button("< BACK", key="back_question"):
            if st.session_state.question_index > 0:
                st.session_state.question_index -= 1
                st.rerun()
            else:
                st.switch_page('pages/start_personal.py')
                st.rerun()
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
                width: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    with col3:
        if st.button("NEXT >", key="next_question"):
            if selected_answer: 
                st.session_state.answers[st.session_state.question_index] = selected_answer
                if selected_answer != 1:
                    st.warning("Please choose only 1 option !!")
                if st.session_state.question_index < total_questions - 1:
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    st.session_state.show_results = True
                    st.rerun()
            else:
                st.warning("Please choose the option !!")
                
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
                width: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

if st.session_state.show_results:
    ans = st.session_state.answers
    info = personal(ans)
    pers = info.pers_t()
    st.divider()
    st.markdown(f"<h1 style='text-align:center; font-size: 40px;'> YOUR RESULT is {pers.upper()} !</h1>", unsafe_allow_html=True)
    st.image(os.path.join("picture", s.loc[pers]['img']))
    st.markdown(f"<p style='text-align:center; font-size: 30px; font-weight:600'>{s.loc[pers]['description']} !</p>", unsafe_allow_html=True)
    st.markdown(f"""<div><span style='font-size: 18px; font-weight: bold;'>BEST colors for you : </span>
        <span style='font-size: 18px;'>{s.loc[pers]['Best colors']}</span></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div><span style='font-size: 18px; font-weight: bold;'>Recommend Hair-dyed colors : </span>
        <span style='font-size: 18px;'>{s.loc[pers]['Hair-dyed colors']}</span></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div><span style='font-size: 18px; font-weight: bold;'>Colors you should AVOID : </span>
        <span style='font-size: 18px;'>{s.loc[pers]['Avoid colors']}</span></div>""", unsafe_allow_html=True)
    
    st.divider()
    colQ, line, colR = st.columns([3,0.1,4])
    with colQ:
        st.markdown(f"<h3 style='text-align:center; font-size: 30px;'>WHAT YOU GOT IS</h3>", unsafe_allow_html=True)
        st.image(os.path.join("picture", jewel.loc[info.un_tone]['img']))

    with colR:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(f"""<div style='text-align: center;'><span style='font-size: 30px; font-weight: bold;'>Undertone : </span>
            <span style='font-size: 25px;'>{info.un_tone}</span></div>""", unsafe_allow_html=True)
        st.markdown(f"""<div style='text-align: center;'><span style='font-size: 30px; font-weight: bold;'>Feature : </span>
            <span style='font-size: 25px;'>{info.feature}</span></div>""", unsafe_allow_html=True)
        st.markdown(f"{jewel.loc[info.un_tone]['description']}", unsafe_allow_html=True)
        
    st.divider()    
    cols = st.columns(len(questions))
    for i, (topic, questions_list) in enumerate(questions.items()):
        with cols[i]:
            st.markdown(f"<h2 style='text-align:center; font-size: 30px;'>{topic} :</h2>", unsafe_allow_html=True)
            for j, (question, _) in enumerate(questions_list):
                question_index = i * 2 + j
                st.markdown(f"<h3 style='text-align:center; font-size: 26px;'>{question}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align:center; font-size: 20px;'>{st.session_state.answers[question_index]}</p>", unsafe_allow_html=True)
        
        if i < len(questions) - 1:
            st.markdown(
                """
                <style>
                .divider {
                    height: 100%;
                    border-left: 1px solid gray;
                    margin: 0 10px;
                }
                </style>
                <div class="divider"></div>
                """,
                unsafe_allow_html=True,
            )

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
            width: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col4, col5, col6 = st.columns([2.75, 2, 2])
    with col5:
        if st.button("Redo the Test", key="redo_test"):
            st.session_state.question_index = 0
            st.session_state.answers = [""] * total_questions
            st.session_state.show_results = False
            st.switch_page('pages/start_personal.py')
            st.rerun()

    st.divider()
    st.markdown("<h2 style='text-align:center;'>Find More about your STYLE !</h2>", unsafe_allow_html=True)
    col7, col8, col9 = st.columns([2, 5, 2])
    with col8:
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
            st.session_state.clear()
            st.switch_page("pages/start_style.py")
            st.rerun()

    st.divider()
    if st.button("< HOME", key="back_result"):
        st.session_state.clear()
        st.switch_page('pages/home.py')
        st.rerun()
