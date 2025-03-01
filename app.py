import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Session state to manage dark mode
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Function to toggle dark mode
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Dark Mode Toggle Button
if st.sidebar.button("🌙 Toggle Dark Mode"):
    toggle_dark_mode()

# Apply CSS dynamically
brown_mode_css = """
    <style>
    .st-bw, .st-emotion-cache-jh76sn, .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    .stTextInput, .stSidebar, .st-bx, .st-emotion-cache-124cvek, .st-emotion-cache-124cvek:hover, .st-emotion-cache-topux, .st-d9 {
        background-color: #2a2929;
        color: #FFFFFF;
    }
    </style>
    """

dark_mode_css = """
    <style>
    .st-emotion-cache-jh76sn, .stApp {
        background-color: #0E1117;
        color: #ffffff;
    }
    </style>
    """

# Inject CSS based on dark mode state
if st.session_state.dark_mode:
    st.markdown(brown_mode_css, unsafe_allow_html=True)
else:
    st.markdown(dark_mode_css, unsafe_allow_html=True)

# Title of the app
st.title("Unit Converter - The Ultimate Conversion Tool 🚀")

st.markdown("---")

# Sidebar for selecting the type of conversion
st.sidebar.header("🔧 Select Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type:",
    ["📏 Length", "⚖️ Weight", "🌡️ Temperature", "🧪 Volume", "⏰ Time"]
)

# Length Conversion
if conversion_type == "📏 Length":
    st.header("📏 Length Conversion")
    length_units = ["Meters", "Foot", "Inches", "Centimeters"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    length_value = st.number_input("Enter Value", value=1.0)

    if from_unit == "Meters":
        if to_unit == "Foot":
            result = length_value * 3.28084
        elif to_unit == "Inches":
            result = length_value * 39.3701
        elif to_unit == "Centimeters":
            result = length_value * 100
        else:
            result = length_value
    elif from_unit == "Foot":
        if to_unit == "Meters":
            result = length_value / 3.28084
        elif to_unit == "Inches":
            result = length_value * 12
        elif to_unit == "Centimeters":
            result = length_value * 30.48
        else:
            result = length_value
    elif from_unit == "Inches":
        if to_unit == "Meters":
            result = length_value / 39.3701
        elif to_unit == "Foot":
            result = length_value / 12
        elif to_unit == "Centimeters":
            result = length_value * 2.54
        else:
            result = length_value
    elif from_unit == "Centimeters":
        if to_unit == "Meters":
            result = length_value / 100
        elif to_unit == "Foot":
            result = length_value / 30.48
        elif to_unit == "Inches":
            result = length_value / 2.54
        else:
            result = length_value

    st.success(f"Result: {length_value} {from_unit} = {result:.2f} {to_unit}")

# Weight Conversion
elif conversion_type == "⚖️ Weight":
    st.header("⚖️ Weight Conversion")
    weight_units = ["Kilograms", "Pounds", "Grams", "Ounces"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    weight_value = st.number_input("Enter Value", value=1.0)

    if from_unit == "Kilograms":
        if to_unit == "Pounds":
            result = weight_value * 2.20462
        elif to_unit == "Grams":
            result = weight_value * 1000
        elif to_unit == "Ounces":
            result = weight_value * 35.274
        else:
            result = weight_value
    elif from_unit == "Pounds":
        if to_unit == "Kilograms":
            result = weight_value / 2.20462
        elif to_unit == "Grams":
            result = weight_value * 453.592
        elif to_unit == "Ounces":
            result = weight_value * 16
        else:
            result = weight_value
    elif from_unit == "Grams":
        if to_unit == "Kilograms":
            result = weight_value / 1000
        elif to_unit == "Pounds":
            result = weight_value / 453.592
        elif to_unit == "Ounces":
            result = weight_value / 28.3495
        else:
            result = weight_value
    elif from_unit == "Ounces":
        if to_unit == "Kilograms":
            result = weight_value / 35.274
        elif to_unit == "Pounds":
            result = weight_value / 16
        elif to_unit == "Grams":
            result = weight_value * 28.3495
        else:
            result = weight_value

    st.success(f"Result: {weight_value} {from_unit} = {result:.2f} {to_unit}")

# Temperature Conversion
elif conversion_type == "🌡️ Temperature":
    st.header("🌡️ Temperature Conversion")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    temp_value = st.number_input("Enter Value", value=0.0)

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (temp_value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = temp_value + 273.15
        else:
            result = temp_value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (temp_value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (temp_value - 32) * 5/9 + 273.15
        else:
            result = temp_value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = temp_value - 273.15
        elif to_unit == "Fahrenheit":
            result = (temp_value - 273.15) * 9/5 + 32
        else:
            result = temp_value

    st.success(f"Result: {temp_value} {from_unit} = {result:.2f} {to_unit}")

# Volume Conversion
elif conversion_type == "🧪 Volume":
    st.header("🧪 Volume Conversion")
    volume_units = ["Liters", "Milliliters", "Gallons", "Cubic Meters"]
    from_unit = st.selectbox("From", volume_units)
    to_unit = st.selectbox("To", volume_units)
    volume_value = st.number_input("Enter Value", value=1.0)

    if from_unit == "Liters":
        if to_unit == "Milliliters":
            result = volume_value * 1000
        elif to_unit == "Gallons":
            result = volume_value * 0.264172
        elif to_unit == "Cubic Meters":
            result = volume_value / 1000
        else:
            result = volume_value
    elif from_unit == "Milliliters":
        if to_unit == "Liters":
            result = volume_value / 1000
        elif to_unit == "Gallons":
            result = volume_value * 0.000264172
        elif to_unit == "Cubic Meters":
            result = volume_value / 1e+6
        else:
            result = volume_value
    elif from_unit == "Gallons":
        if to_unit == "Liters":
            result = volume_value * 3.78541
        elif to_unit == "Milliliters":
            result = volume_value * 3785.41
        elif to_unit == "Cubic Meters":
            result = volume_value * 0.00378541
        else:
            result = volume_value
    elif from_unit == "Cubic Meters":
        if to_unit == "Liters":
            result = volume_value * 1000
        elif to_unit == "Milliliters":
            result = volume_value * 1e+6
        elif to_unit == "Gallons":
            result = volume_value * 264.172
        else:
            result = volume_value

    st.success(f"Result: {volume_value} {from_unit} = {result:.2f} {to_unit}")

# Time Conversion
elif conversion_type == "⏰ Time":
    st.header("⏰ Time Conversion")
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    from_unit = st.selectbox("From", time_units)
    to_unit = st.selectbox("To", time_units)
    time_value = st.number_input("Enter Value", value=1.0)

    if from_unit == "Seconds":
        if to_unit == "Minutes":
            result = time_value / 60
        elif to_unit == "Hours":
            result = time_value / 3600
        elif to_unit == "Days":
            result = time_value / 86400
        else:
            result = time_value
    elif from_unit == "Minutes":
        if to_unit == "Seconds":
            result = time_value * 60
        elif to_unit == "Hours":
            result = time_value / 60
        elif to_unit == "Days":
            result = time_value / 1440
        else:
            result = time_value
    elif from_unit == "Hours":
        if to_unit == "Seconds":
            result = time_value * 3600
        elif to_unit == "Minutes":
            result = time_value * 60
        elif to_unit == "Days":
            result = time_value / 24
        else:
            result = time_value
    elif from_unit == "Days":
        if to_unit == "Seconds":
            result = time_value * 86400
        elif to_unit == "Minutes":
            result = time_value * 1440
        elif to_unit == "Hours":
            result = time_value * 24
        else:
            result = time_value

    st.success(f"Result: {time_value} {from_unit} = {result:.2f} {to_unit}")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2025 Developed by <span style='font-weight: bold;'>Muhammad Ahmed</span>. All rights reserved. 🚀</p>", unsafe_allow_html=True)