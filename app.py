import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mechanical Engineering Tool", page_icon="⚙️", layout="wide")

# --- CUSTOM CSS FOR MODERN UI ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_all_map=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ Navigation")
    selection = st.radio("Go to:", ["Home & Student Info", "Unit Converter", "Material Density Checker"])
    st.info("This app provides quick mechanical calculations for engineers.")

# --- HOME PAGE & STUDENT INFO ---
if selection == "Home & Student Info":
    st.title("🏗️ Mechanical Unit Converter & Material Density Checker")
    st.subheader("University Project Submission")
    
    # Student Details Card
    st.success(f"""
    **Student Details:**
    - **Full Name:** Aasiya Ismail
    - **Roll Number:** 25-ME-52
    """)
    
    st.markdown("""
    ### Project Overview
    This application is designed to assist mechanical engineering students and professionals in:
    1.  **Converting** common physical units used in mechanics.
    2.  **Checking** densities and properties of standard engineering materials.
    
    *Use the sidebar on the left to start!*
    """)

# --- UNIT CONVERTER PAGE ---
elif selection == "Unit Converter":
    st.title("🔄 Mechanical Unit Converter")
    
    category = st.selectbox("Select Category", ["Length", "Force", "Pressure", "Temperature", "Speed"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["meter", "centimeter", "millimeter", "inch", "foot"])
        with col2:
            unit_to = st.selectbox("To", ["meter", "centimeter", "millimeter", "inch", "foot"])
        
        # Conversion Dictionary to Meters
        to_meters = {"meter": 1.0, "centimeter": 0.01, "millimeter": 0.001, "inch": 0.0254, "foot": 0.3048}
        result = val * to_meters[unit_from] / to_meters[unit_to]
        st.metric("Result", f"{result:.4f} {unit_to}")

    elif category == "Force":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Newton", "kiloNewton"])
        with col2:
            unit_to = st.selectbox("To", ["Newton", "kiloNewton"])
        
        # Logic: 1 kN = 1000 N
        factor = 1000 if unit_from == "kiloNewton" and unit_to == "Newton" else (0.001 if unit_from == "Newton" and unit_to == "kiloNewton" else 1)
        st.metric("Result", f"{val * factor:.4f} {unit_to}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal", "bar", "psi"])
        with col2:
            unit_to = st.selectbox("To", ["Pascal", "bar", "psi"])
        
        # Convert to Pascal first
        to_pascal = {"Pascal": 1.0, "bar": 100000.0, "psi": 6894.76}
        result = val * to_pascal[unit_from] / to_pascal[unit_to]
        st.metric("Result", f"{result:.4f} {unit_to}")

    elif category == "Temperature":
        with col1:
            val = st.number_input("Enter Value", value=25.0)
            unit_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            unit_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
        # Conversion Logic
        if unit_from == unit_to: result = val
        elif unit_from == "Celsius":
            result = (val * 9/5) + 32 if unit_to == "Fahrenheit" else val + 273.15
        elif unit_from == "Fahrenheit":
            result = (val - 32) * 5/9 if unit_to == "Celsius" else (val - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin":
            result = val - 273.15 if unit_to == "Celsius" else (val - 273.15) * 9/5 + 32
        
        st.metric("Result", f"{result:.2f} {unit_to}")

    elif category == "Speed":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["m/s", "km/h"])
        with col2:
            unit_to = st.selectbox("To", ["m/s", "km/h"])
        
        factor = 3.6 if unit_from == "m/s" and unit_to == "km/h" else (1/3.6 if unit_from == "km/h" and unit_to == "m/s" else 1)
        st.metric("Result", f"{val * factor:.4f} {unit_to}")

# --- MATERIAL DENSITY PAGE ---
elif selection == "Material Density Checker":
    st.title("🧪 Material Density Checker")
    
    # Data Dictionary
    materials = {
        "Steel": {"density": 7850, "desc": "High strength and durability, primarily composed of iron and carbon."},
        "Aluminum": {"density": 2700, "desc": "Lightweight and corrosion-resistant, vital for aerospace and automotive industries."},
        "Copper": {"density": 8960, "desc": "Excellent electrical and thermal conductivity; commonly used in wiring."},
        "Brass": {"density": 8500, "desc": "An alloy of copper and zinc; prized for low friction and acoustic properties."},
        "Cast Iron": {"density": 7200, "desc": "Known for its excellent castability and vibration damping qualities."},
        "Titanium": {"density": 4500, "desc": "High strength-to-weight ratio and exceptional corrosion resistance."}
    }
    
    selected_mat = st.selectbox("Choose a Material", list(materials.keys()))
    
    density_kg_m3 = materials[selected_mat]["density"]
    density_g_cm3 = density_kg_m3 / 1000
    
    # Display results in columns
    c1, c2 = st.columns(2)
    c1.metric("Density (kg/m³)", f"{density_kg_m3}")
    c2.metric("Density (g/cm³)", f"{density_g_cm3}")
    
    st.info(f"**Description:** {materials[selected_mat]['desc']}")
