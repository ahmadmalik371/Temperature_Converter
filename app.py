import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS for custom background and style
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #87CEFA, #FF6347);
        color: #FFFFFF;
    }
    .temp-output {
        font-size: 1.5rem;
        padding: 10px;
        border-radius: 8px;
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
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌡️ Temperature Converter")

# Input slider for Celsius
celsius = st.slider("Select temperature in Celsius:", -100.0, 100.0, 25.0)

# Convert to Fahrenheit and Kelvin
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Function to determine temperature class
def get_temp_class(temp_c):
    if temp_c <= 0:
        return "cold"
    elif 0 < temp_c < 30:
        return "warm"
    else:
        return "hot"

# Display results with color-coded boxes
st.write("### Converted Temperatures:")
st.write(f'<div class="temp-output {get_temp_class(celsius)}">Celsius: {celsius:.2f} °C</div>', unsafe_allow_html=True)
st.write(f'<div class="temp-output {get_temp_class(celsius)}">Fahrenheit: {fahrenheit:.2f} °F</div>', unsafe_allow_html=True)
st.write(f'<div class="temp-output {get_temp_class(celsius)}">Kelvin: {kelvin:.2f} K</div>', unsafe_allow_html=True)
