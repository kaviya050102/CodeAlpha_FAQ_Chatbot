import streamlit as st
from chatbot import get_answer
import time
import base64
from datetime import datetime


# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==============================
# LOAD CSS
# ==============================

def load_css():

    with open("style.css", "r") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()



# ==============================
# BACKGROUND
# ==============================

def add_background(image_file):

    try:

        with open(image_file, "rb") as file:

            encoded = base64.b64encode(
                file.read()
            ).decode()


        st.markdown(
            f"""
            <style>

            .stApp {{

                background-image:

                linear-gradient(
                rgba(5,8,22,0.85),
                rgba(5,8,22,0.90)
                ),

                url(
                "data:image/png;base64,{encoded}"
                );

                background-size:cover;

                background-attachment:fixed;

            }}

            </style>
            """,

            unsafe_allow_html=True
        )

    except:

        pass



add_background(
    "assets/background.png"
)



# ==============================
# HEADER
# ==============================


col1, col2 = st.columns([1,5])


with col1:

    try:

        st.image(
            "assets/chatbot_avatar.png",
            width=180
        )

    except:

        st.write("🤖")



with col2:

    st.markdown(
        """
        <h1 class="title">
        🤖 AI FAQ Assistant
        </h1>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <p class="subtitle">
        Powered by NLP • TF-IDF • Machine Learning
        </p>
        """,
        unsafe_allow_html=True
    )



st.write("")



# ==============================
# SIDEBAR
# ==============================


with st.sidebar:


    st.image(
        "assets/chatbot_avatar.png",
        width=120
    )


    st.markdown(
        """
        # 🤖 AI Assistant


        ## Technology

        🐍 Python

        🧠 NLP

        📊 TF-IDF

        🤖 Machine Learning

        🌐 Streamlit



        ## Features

        ✅ FAQ Matching

        ✅ Smart Answers

        ✅ Chat History

        ✅ Similarity Search



        ## Internship

        CodeAlpha AI Internship

        """,
        unsafe_allow_html=True
    )




# ==============================
# CHAT MEMORY
# ==============================


if "messages" not in st.session_state:

    st.session_state.messages = []





# ==============================
# SHOW CHAT
# ==============================


for message in st.session_state.messages:


    if message["role"] == "user":


        st.markdown(
            f"""
            <div class="user-message">

            👤 <b>You</b>

            <br><br>

            {message["content"]}

            </div>
            """,
            unsafe_allow_html=True
        )



    else:


        st.markdown(
            f"""
            <div class="bot-message">

            <div class="assistant-title">

            🤖 AI Assistant

            </div>


            <br>


            <div class="bot-answer">

            {message["content"]}

            </div>


            </div>
            """,
            unsafe_allow_html=True
        )





# ==============================
# INPUT
# ==============================


question = st.chat_input(
    "Ask anything about Artificial Intelligence..."
)



if question:


    current_time = datetime.now().strftime(
        "%H:%M"
    )


    # User message

    st.session_state.messages.append(

        {
            "role":"user",
            "content":question,
            "time":current_time
        }

    )


    # AI answer

    with st.spinner(
        "🤖 AI is thinking..."
    ):

        time.sleep(1)

        answer = get_answer(question)



    # Safety check

    if answer is None or answer == "":

        answer = "Sorry, I could not find a suitable answer."



    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":answer,
            "time":current_time
        }

    )


    st.rerun()




# ==============================
# CLEAR CHAT
# ==============================


if st.button(
    "🗑 Clear Conversation"
):

    st.session_state.messages.clear()

    st.rerun()



# ==============================
# FOOTER
# ==============================


st.divider()


st.caption(
    "✨ Developed by Kaviya | CodeAlpha Artificial Intelligence Internship"
)