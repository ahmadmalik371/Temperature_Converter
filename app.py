import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS for custom styles
st.markdown("""
    <style>
    @keyframes backgroundAnimation {
        0% { background-color: #87CEFA; }
        50% { background-color: #FF6347; }
        100% { background-color: #87CEFA; }
    }
    .main {
        background: linear-gradient(to right, #87CEFA, #FF6347);
        animation: backgroundAnimation 10s ease infinite;
        color: #FFFFFF;
        min-height: 100vh;
    }
    .temp-output {
        font-size: 2rem;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
        opacity: 0;
        animation: fadeIn 0.5s 
