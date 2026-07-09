import streamlit as st
import os
import pandas as pd

info = pd.read_excel("C:\\Users\\ASUS\\Desktop\\python pj\\pages\\info.xlsx", sheet_name=['Fashion'])
f = info['Fashion']
f = f.set_index('style')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt&display=swap');
h1, h2, h3, p, div, a {
    font-family: 'Prompt', sans-serif;
}
</style>
""", unsafe_allow_html=True)

class cloth:
    def __init__(self, gender, body_shape, pers, keyword):
        self.pers = pers
        self.body_shape = body_shape
        self.gender = gender
        self.keyword = keyword
        self.scores = {}

    def calculate_suitability(self):
        self.personality_styles = {
            "Autumn": {"Minimal": 10, "Formal": 9, "Punk": 8},
            "Spring": {"Bohemian": 10, "Athleisure": 9, "Romantic": 8},
            "Summer": {"Minimal": 10, "Romantic": 9, "Elegant": 8},
            "Winter": {"Punk": 10, "Alluring": 9, "Elegant": 8},
        }

        if self.pers in self.personality_styles:
            for style, score in self.personality_styles[self.pers].items():
                self.scores[style] = score

        self.body_style_scores = {
            "Male": {
                "Triangle": {"Minimal": 10, "Formal": 9, "Street": 8},
                "Hourglass": {"Street": 10, "Elegant": 9, "Athleisure": 8},
                "Rectangle": {"Punk": 10, "Bohemian": 9, "Alluring": 8},
                "Inverted Triangle": {"Formal": 10, "Minimal": 9, "Elegant": 8},
                "Round": {"Bohemian": 10, "Street ": 9, "Minimal": 8}
            },
            "Female": {
                "Round": {"Romantic": 10, "Bohemian": 9, "Street": 8},
                "Hourglass": {"Alluring": 10, "Romantic": 9, "Retro": 8},
                "Triangle": {"Alluring": 10, "Elegant": 9, "Athleisure": 8},
                "Rectangle": {"Punk": 10, "Alluring": 9, "Athleisure": 8},
                "Inverted Triangle": {"Formal": 10, "Punk": 9, "Minimal": 8}
            }
        }

        if self.gender in self.body_style_scores and self.body_shape in self.body_style_scores[self.gender]:
            for style, score in self.body_style_scores[self.gender][self.body_shape].items():
                if style in self.scores:
                    self.scores[style] += score
                else:
                    self.scores[style] = score

        self.keyword_style = {
            "Elegant": {"Elegant" : 10, "Formal" : 9, "Minimal" : 9},
            "Sweet": {"Romantic" : 10, "Bohemian" : 9, "Minimal" : 8},
            "Sexy": {"Alluring" : 10, "Punk" : 9, "Retro" : 8},
            "Cool": {"Athleisure" : 10 , "Street" : 9, "Retro" : 8}
        }

        if self.keyword in self.keyword_style:
            for key, score in self.keyword_style[self.keyword].items():
                self.scores[style] = score

class get_recommend(cloth):
    def __init__(self, gender, body_shape, pers, keyword):
        cloth.__init__(self, gender, body_shape, pers, keyword) # แก้ไขตรงนี้
        self.sorted_styles = []
        self.perc_scores = {}

    def get_top_recommendations(self):
        self.calculate_suitability()
        self.sorted_styles = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        top_styles = [style for style, score in self.sorted_styles[:4]]
        for style, score in self.sorted_styles[:4]:
            self.perc_scores[style] = (score / 40) * 100
        return top_styles


st.markdown("<h1 style='text-align:center;'> Let's find your STYLE !</h1>", unsafe_allow_html=True) 
st.write("") 
st.write("") 
st.write("") 
st.write("") 

questions = { 
    "Find your STYLES": [ 
        ("What is your GENDER ?", ["Male", "Female"]), 
        ("What is your SHAPE BODY ?", ["Round", "Hourglass", "Triangle", "Rectangle", "Inverted Triangle"]), 
        ("What is your PERSONAL COLOR ?(or you like most)", ["Autumn",  "Winter", "Spring","Summer"]), 
        ("What do you prefer ?", ["Elegant", "Sweet", "Sexy", "Cool"]) 
    ]} 
img = { 
    "Find your STYLES": [ 
        (os.path.join("picture", "35.png"), [ 
            (os.path.join("picture", "36.png"), "Male"), 
            (os.path.join("picture", "37.png"), "Female") 
        ]), 
        (os.path.join("picture", "39.png"), [ 
            (os.path.join("picture", "40.png"), "Round"), 
            (os.path.join("picture", "41.png"), "Hourglass"), 
            (os.path.join("picture", "42.png"), "Triangle"), 
            (os.path.join("picture", "43.png"), "Rectangle"), 
            (os.path.join("picture", "44.png"), "Inverted Triangle") 
        ]), 
        (os.path.join("picture", "28.png"), [ 
            (os.path.join("picture", "29.png"), "Autumn"), 
            (os.path.join("picture", "30.png"), "Winter"), 
            (os.path.join("picture", "31.png"), "Spring"), 
            (os.path.join("picture", "32.png"), "Summer") 
        ]), 
        (os.path.join("picture", "52.png"), [ 
            (os.path.join("picture", "53.png"), "Elegant"), 
            (os.path.join("picture", "54.png"), "Sweet"), 
            (os.path.join("picture", "55.png"), "Cool"), 
            (os.path.join("picture", "56.png"), "Sexy") 
        ]) 
    ] 
} 

if "current_q_img" not in st.session_state: 
    st.session_state.current_q_img = img["Find your STYLES"][0][0] 
if "current_op_img" not in st.session_state: 
    st.session_state.current_op_img = img["Find your STYLES"][0][1] 

total_questions = sum(len(q_list) for q_list in questions.values()) 

if "question_index" not in st.session_state: 
    st.session_state.question_index = 0 

if "answers" not in st.session_state or len(st.session_state.answers) != total_questions: 
    st.session_state.answers = [""] * total_questions 

if "show_results" not in st.session_state: 
    st.session_state.show_results = False 

progress = (st.session_state.question_index + 1) / total_questions 

if st.session_state.question_index < 3: 
    progress_texts = ["Find your STYLE", "FINISH"] 
    progress_styles = ["font-size: 28px;", "font-size: 18px;"] 
elif st.session_state.question_index == 3: 
    progress_texts = ["Find your STYLE", "FINISH"] 
    progress_styles = ["font-size: 18px;", "font-size: 28px;"] 

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
        right: 0%; 
        text-align: right; 
        {progress_styles[1]} 
    }} 
    </style> 
    <div class="progress-container"> 
        <span class="progress-text">{progress_texts[0]}</span> 
        <span class="progress-text">{progress_texts[1]}</span> 
    </div> 
    """, unsafe_allow_html=True) 

st.progress(progress) 

if st.session_state.question_index < total_questions: 
    img_list = list(img.keys()) 
    question_list = list(questions.keys()) 
    current_topic = question_list[0] 
    current_question_index = st.session_state.question_index 
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
    info = get_recommend(ans[0], ans[1], ans[2], ans[3]) 
    result = info.get_top_recommendations() 
    st.divider() 
    st.markdown(f"""<h1 style='text-align:center;'><span>TOP 3 </span> 
                    <span style='font-size: 32px;'>STYLES RECOMMEND TO YOU !</span></h1>""", unsafe_allow_html=True) 

    st.markdown(f"<p style='text-align:center; font-size: 72px; font-weight:900;'>1</p>", unsafe_allow_html=True)
    st.markdown(f"""<div style='text-align:center;'><span style='font-size: 36px; font-weight:800;'>{result[0].upper()} </span>
                    <span style='font-size: 24px;' font-weight:600;>Match {info.perc_scores[result[0]]:.2f}%</span></div>""", unsafe_allow_html=True) 
    st.write("")
    st.image(os.path.join("picture", f.loc[result[0]]['img'])) 
    st.markdown(f"<div><span style='font-size: 18px;'>คุณนั้นเหมาะกับ{f.loc[result[0]]['Clothes']}</span></div>", unsafe_allow_html=True) 
    st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Recommend Accessories : </h3>", unsafe_allow_html=True) 
    st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[0]]['Accessories']}</span></div>", unsafe_allow_html=True) 
    st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Style Tone : </h3>", unsafe_allow_html=True) 
    st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[0]]['color']}</span></div>", unsafe_allow_html=True) 
    st.markdown(f"""<div><span style='font-size: 24px; font-weight: bold;'>Best for who are  </span> 
                    <span style='font-size: 28px; font-weight: bold;'>{f.loc[result[0]]['personal']}</span></div>""", unsafe_allow_html=True) 
    
    st.divider() 
    col4, col5, col6= st.columns([5.5, 0.1, 5.5]) 
    with col4: 
        st.markdown(f"<p style='text-align:center; font-size: 72px; font-weight:900;'>2</p>", unsafe_allow_html=True) 
        st.markdown(f"<h2 style='text-align:center; font-size: 36px; font-weight:800;'>{result[1].upper()}</h2>", unsafe_allow_html=True) 
        st.markdown(f"<h2 style='text-align:center; font-size: 24px;' font-weight:600;>Match {info.perc_scores[result[1]]:.2f}%</h2>", unsafe_allow_html=True) 
        st.image(os.path.join("picture", f.loc[result[1]]['img']))
        st.markdown(f"<div><span style='font-size: 18px;'>อันดับสองคือ{f.loc[result[1]]['Clothes']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Recommend Accessories : </h3>", unsafe_allow_html=True) 
        st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[1]]['Accessories']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Style Tone : </h3>", unsafe_allow_html=True) 
        st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[1]]['color']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"""<div><span style='font-size: 24px; font-weight: bold;'>Best for who are  </span> 
                    <span style='font-size: 28px; font-weight: bold;'>{f.loc[result[1]]['personal']}</span></div>""", unsafe_allow_html=True) 
    with col5: 
        st.write("")
        st.write("")
        st.markdown( 
            """ 
            <style> 
            .divider { 
                height: 140vh; 
                width: 10px; 
                border-left: 2px solid gray; 
                margin: 0 auto; 
            } 
            </style> 
            <div class="divider"></div> 
            """, 
            unsafe_allow_html=True, 
        ) 
    with col6: 
        st.markdown(f"<p style='text-align:center; font-size: 72px; font-weight:900;'>3</p>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align:center; font-size: 36px; font-weight:800;'>{result[2].upper()}</h2>", unsafe_allow_html=True) 
        st.markdown(f"<h2 style='text-align:center; font-size: 24px;' font-weight:600;>Match {info.perc_scores[result[2]]:.2f}%</h2>", unsafe_allow_html=True) 
        st.image(os.path.join("picture", f.loc[result[2]]['img']))
        st.markdown(f"<div><span style='font-size: 18px;'>อันดับสามคือ{f.loc[result[2]]['Clothes']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Recommend Accessories : </h3>", unsafe_allow_html=True) 
        st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[2]]['Accessories']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"<h3 style='font-size: 24px; font-weight: bold;'>Style Tone : </h3>", unsafe_allow_html=True) 
        st.markdown(f"<div><span style='font-size: 18px;'>{f.loc[result[2]]['color']}</span></div>", unsafe_allow_html=True) 
        st.markdown(f"""<div><span style='font-size: 24px; font-weight: bold;'>Best for who are  </span> 
                    <span style='font-size: 28px; font-weight: bold;'>{f.loc[result[2]]['personal']}</span></div>""", unsafe_allow_html=True) 
    st.divider() 
    for i, (topic, questions_list) in enumerate(questions.items()):
        st.markdown(f"<h2 style='text-align:center; font-size: 30px;'>{topic} :</h2>", unsafe_allow_html=True)
        for j, (question, _) in enumerate(questions_list):
            question_index = i * len(questions_list) + j
            st.markdown(f"<p style='text-align:center; font-size: 20px;'>{question} : {st.session_state.answers[question_index]}</p>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns([2.75, 2, 2]) 
    with col5: 
        if st.button("Redo the Test", key="redo_test"): 
            st.session_state.question_index = 0 
            st.session_state.answers = [""] * total_questions 
            st.session_state.show_results = False 
            st.switch_page('pages/start_personal.py') 
            st.rerun()

    st.divider() 
    if st.button("< HOME", key="back_result"): 
        st.session_state.clear() 
        st.switch_page('pages/home.py') 
        st.rerun()
