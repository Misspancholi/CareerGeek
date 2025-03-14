import streamlit as st
import pandas as pd
import base64
import time

# Function to encode image
@st.cache_data
def get_base64_from_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Encode background image
bg_image = get_base64_from_file("logo.jpg")

def apply_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: indigo;
                font-family: Arial, sans-serif;
            }
            .navbar {
                background-color: rgba(0, 0, 0, 0.8);
                padding: 15px;
                text-align: center;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }
            .content-container {
                text-align: center;
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
            }
            .stButton>button {
                background-color: #E0B0FF;
                color: black;
                font-size: 18px;
                padding: 12px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                width: 100%;
                margin-top: 10px;
                transition: transform 0.2s, background-color 0.3s, box-shadow 0.3s;
            }
            .stButton>button:hover {
                background-color: #E0B0FF;
                transform: scale(1.05);
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            .fade-in {
                animation: fadeIn 2s ease-in-out;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

apply_custom_css()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "intro"

# Intro Animation Page
if st.session_state.page == "intro":
    st.markdown(f"""
         <div style='display: flex; justify-content: center; align-items: center; height: 100vh;' class='fade-in'>
            <img src='data:image/jpeg;base64,{logo_image}' style='width: 100%; max-width: 700px;'>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2)  # Show logo for 2 seconds
    st.session_state.page = "login"
    st.rerun()

# Login Page
elif st.session_state.page == "login":
    st.markdown("<div class='navbar'>🔐 Login Page</div>", unsafe_allow_html=True)
    st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Login"):
        if username == "admin" and password == "password123":
            st.session_state.page = "index"
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid username or password")
    st.markdown("</div>", unsafe_allow_html=True)


# Main Dashboard
elif st.session_state.page == "index":
    st.markdown("<div class='navbar'>🌟 Welcome to the Dashboard</div>", unsafe_allow_html=True)
    #st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.subheader("Select an Option")
    
    if st.button("Quiz"):
        st.session_state.page = "quiz"
        st.rerun()
    if st.button("Quiz Results"):
        st.session_state.page = "results"
        st.rerun()
    if st.button("Chatbot"):
        st.session_state.page = "chatbot"
        st.rerun()
    if st.button("Logout"):
        st.session_state.page = "login"
        st.session_state.authenticated = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Quiz Page
elif st.session_state.page == "quiz":
    st.markdown("<div class='navbar'>📊 Take Quiz</div>", unsafe_allow_html=True)
    st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.subheader("Retake Quiz")
    if "question   " in st.session_state:
        df = pd.DataFrame(st.session_state["quiz"], columns=["Question", "Your Answer", "Correct Answer", "Result"])
        st.table(df)
    else:
        st.write("No quiz results found. Please take the quiz first.")
    if st.button("Back to Dashboard"):
        st.session_state.page = "index"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# Quiz Results Page
elif st.session_state.page == "results":
    st.markdown("<div class='navbar'>📊 Quiz Results</div>", unsafe_allow_html=True)
    st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.subheader("Your Performance")
    if "quiz_results" in st.session_state:
        df = pd.DataFrame(st.session_state["quiz_results"], columns=["Question", "Your Answer", "Correct Answer", "Result"])
        st.table(df)
    else:
        st.write("No quiz results found. Please take the quiz first.")
    if st.button("Back to Dashboard"):
        st.session_state.page = "index"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# Chatbot Page
elif st.session_state.page == "chatbot":
    st.markdown("<div class='navbar'>🤖 Chatbot</div>", unsafe_allow_html=True)
    st.markdown("<div class='content-container'>", unsafe_allow_html=True)
    st.subheader("Ask me anything!")
    user_input = st.text_input("You:", "", key="chat_input")
    if st.button("Send"):
        if user_input.strip():
            st.write(f"**Bot:** I'm here to help with {user_input}!")
        else:
            st.warning("Please enter a message.")
    if st.button("Back to Dashboard"):
        st.session_state.page = "index"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
