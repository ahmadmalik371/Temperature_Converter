import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS for custom styles
st.markdown(
    """
    <style>
    @keyframes backgroundAnimation {
        0% { background-color: #87CEFA; }
        50% { background-color: #FF6347; }
        100% { background-color: #87CEFA; }
    }
    .main {
        background: linear-gradient(270deg, #87CEFA, #FF6347);
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
        animation: fadeIn 0.5s forwards;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .temp-output:hover {
        transform: scale(1.05);
    }
    .cold {
        background-color: rgba(30, 144, 255, 0.8);
    }
    .warm {
        background-color: rgba(255, 215, 0, 0.8);
    }
    .hot {
        background-color: rgba(255, 69, 0, 0.8);
    }
    .button {
        background-color: #FFFFFF;
        color: #FF6347;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
    }
    .button:hover {
        background-color: #FF6347;
        color: #FFFFFF;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🌡️ Temperature Converter")

# Input section
col1, col2 = st.columns(2)

with col1:
    st.header("Input Temperature")
    celsius = st.slider("Select temperature in Celsius:", -100.0, 100.0, 25.0)

with col2:
    st.header("Convert To")
    if st.button("Convert"):
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

# Adding a footer
st.markdown(
    """
    <footer style='text-align: center; margin-top: 20px;'>
        <p style='color: white;'>Made with ❤️ using Streamlit</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
