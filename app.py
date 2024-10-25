import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Stylish Temperature Converter",
    page_icon="🌡️",
    layout="centered",
    initial_sidebar_state="auto",
)

# CSS for custom styles
st.markdown(
    """
    <style>
    @keyframes backgroundAnimation {
        0% { background-color: #FF5733; }
        50% { background-color: #FFC300; }
        100% { background-color: #FF5733; }
    }
    .main {
        background: linear-gradient(135deg, #FF5733, #FFC300);
        animation: backgroundAnimation 5s ease infinite;
        color: #FFFFFF;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    h1 {
        font-size: 3rem;
        text-shadow: 2px 2px #000;
    }
    .temp-output {
        font-size: 2rem;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        opacity: 0;
        animation: fadeIn 0.5s forwards;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
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
        color: #FF5733;
        border: none;
        border-radius: 5px;
        padding: 15px 30px;
        font-size: 1.2rem;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .button:hover {
        background-color: #FF5733;
        color: #FFFFFF;
        transform: scale(1.05);
    }
    .footer {
        background: linear-gradient(135deg, #ff7e5f, #feb47b);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }
    .footer p {
        font-size: 1.5rem;
        color: #fff;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🌡️ Stylish Temperature Converter")

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

# Enhanced footer
st.markdown(
    """
    <div class="footer">
        <p>Made with ❤️ using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True,
)
