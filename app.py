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
    .main {
        background: linear-gradient(to right, #87CEFA, #FF6347);
        color: #FFFFFF;
    }
    .temp-output {
        font-size: 2rem;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }
    .temp-output:hover {
        transform: scale(1.05);
    }
    .cold {
        background-color: #1E90FF;
    }
    .warm {
        background-color: #FFD700;
    }
    .hot {
        background-color: #FF4500;
    }
    .button {
        background-color: #FFFFFF;
        color: #FF6347;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.
