import streamlit as st

# --- PAGE CONFIGURATION ---
# This sets the browser tab title and layout
st.set_page_config(page_title="Mechanical Engineering Tool", page_icon="⚙️", layout="wide")

# --- CUSTOM CSS FOR MODERN UI ---
# This makes the app look more professional with custom colors and button styles
st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
        font-weight: bold;
    }
    /* Style for the student info box */
    .student-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #e1f5fe;
        border-left: 5px solid #01579b;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ Navigation")
    st.markdown("---")
    selection = st.radio("Go to:", ["Home & Student Info", "Unit Converter", "Material Density Checker"])
    st.markdown("---")
    st.info("Engineering Tool v1.0")

# --- HOME PAGE & STUDENT INFO ---
if selection == "Home & Student Info":
    st.title("🏗️ Mechanical Unit Converter & Material Density Checker")
    
    # Professional Header for University Project
    st.markdown(f"""
    <div class="student-box">
        <h3>Project Submission Details</h3>
        <p><b>Full Name:</b> Aasiya Ismail</p>
        <p><b>Roll Number:</b> 25-ME-52</p>
        <p><b>Department:</b> Mechanical Engineering</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Project Overview")
    st.write("""
    This application is a specialized toolkit designed for mechanical engineers to perform 
    daily calculations efficiently. It features a robust unit conversion system and a 
    comprehensive material property database.
    """)
    st.success("👈 Use the sidebar to navigate between features!")

# --- UNIT CONVERTER PAGE ---
elif selection == "Unit Converter":
    st.title("🔄 Mechanical Unit Converter")
    st.write("Perform precise conversions across major mechanical dimensions.")
    
    category = st.selectbox("Select Measurement Category", ["Length", "Force", "Pressure", "Temperature", "Speed"])
    
    # Create two columns for input and output
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["meter", "centimeter", "millimeter", "inch", "foot"])
        with col2:
            unit_to = st.selectbox("To", ["meter", "centimeter", "millimeter", "inch", "foot"])
        
        # Conversion Dictionary (Values relative to 1 Meter)
        to_meters = {"meter": 1.0, "centimeter": 0.01, "millimeter": 0.001, "inch": 0.0254, "foot": 0.3048}
        result = val * to_meters[unit_from] / to_meters[unit_to]
        st.metric(label=f"Converted Value ({unit_to})", value=f"{result:.4f}")

    elif category == "Force":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Newton", "kiloNewton"])
        with col2:
            unit_to = st.selectbox("To", ["Newton", "kiloNewton"])
        
        factor = 1000 if unit_from == "kiloNewton" and unit_to == "Newton" else (0.001 if unit_from == "Newton" and unit_to == "kiloNewton" else 1)
        st.metric(label="Result", value=f"{val * factor:.4f} {unit_to}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal", "bar", "psi"])
        with col2:
            unit_to = st.selectbox("To", ["Pascal", "bar", "psi"])
        
        # Values relative to 1 Pascal
        to_pascal = {"Pascal": 1.0, "bar": 100000.0, "psi": 6894.76}
        result = val * to_pascal[unit_from] / to_pascal[unit_to]
        st.metric(label="Result", value=f"{result:.4f} {unit_to}")

    elif category == "Temperature":
        with col1:
            val = st.number_input("Enter Value", value=25.0)
            unit_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            unit_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
        if unit_from == unit_to: result = val
        elif unit_from == "Celsius":
            result = (val * 9/5) + 32 if unit_to == "Fahrenheit" else val + 273.15
        elif unit_from == "Fahrenheit":
            result = (val - 32) * 5/9 if unit_to == "Celsius" else (val - 32) * 5/9 + 273.15
        elif unit_from == "Kelvin":
            result = val - 273.15 if unit_to == "Celsius" else (val - 273.15) * 9/5 + 32
        
        st.metric(label="Result", value=f"{result:.2f} °{unit_to[0]}")

    elif category == "Speed":
        with col1:
            val = st.number_input("Enter Value", value=1.0)
            unit_from = st.selectbox("From", ["m/s", "km/h"])
        with col2:
            unit_to = st.selectbox("To", ["m/s", "km/h"])
        
        factor = 3.6 if unit_from == "m/s" and unit_to == "km/h" else (1/3.6 if unit_from == "km/h" and unit_to == "m/s" else 1)
        st.metric(label="Result", value=f"{val * factor:.4f} {unit_to}")

# --- MATERIAL DENSITY PAGE ---
elif selection == "Material Density Checker":
    st.title("🧪 Material Density Checker")
    st.write("Select a material to view its physical properties and engineering description.")
    
    materials = {
        "Steel": {"density": 7850, "desc": "High strength and durability, primarily composed of iron and carbon. Standard for structural engineering."},
        "Aluminum": {"density": 2700, "desc": "Lightweight and corrosion-resistant. Crucial for aerospace and modern automotive design."},
        "Copper": {"density": 8960, "desc": "Superior electrical and thermal conductivity. Frequently used in heat exchangers and electronics."},
        "Brass": {"density": 8500, "desc": "An alloy of copper and zinc. Popular for valves, fittings, and low-friction applications."},
        "Cast Iron": {"density": 7200, "desc": "Exceptional castability and vibration damping. Used for engine blocks and machine bases."},
        "Titanium": {"density": 4500, "desc": "Remarkable strength-to-weight ratio and bio-compatibility. Used in high-performance racing and implants."}
    }
    
    selected_mat = st.selectbox("Choose Engineering Material", list(materials.keys()))
    
    density_kg_m3 = materials[selected_mat]["density"]
    density_g_cm3 = density_kg_m3 / 1000
    
    # Visual Layout for Density
    st.markdown("---")
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Density (kg/m³)", f"{density_kg_m3:,}")
    with res_col2:
        st.metric("Density (g/cm³)", f"{density_g_cm3:.3f}")
    
    st.warning(f"**Engineering Note:** {materials[selected_mat]['desc']}")
