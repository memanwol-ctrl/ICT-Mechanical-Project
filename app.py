# =========================================================
# Mechanical Unit Converter & Material Density Checker
# Developed Using Python & Streamlit
# Student Name: Aasiya Ismail
# Roll Number: 25-ME-52
# Department: Mechanical Engineering
# =========================================================

# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Mechanical Engineering Toolkit",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS STYLING ----------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #f4f7fa;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* Main Title */
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #0f172a;
    text-align: center;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #334155;
    text-align: center;
    margin-bottom: 25px;
}

/* Information Card */
.info-card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 8px solid #2563eb;
    margin-bottom: 20px;
}

/* Section Header */
.section-header {
    background-color: #2563eb;
    padding: 12px;
    border-radius: 10px;
    color: white;
    font-size: 24px;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 15px;
    color: gray;
    margin-top: 30px;
    font-size: 14px;
}

/* Metric Box */
.metric-box {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

/* Button Styling */
.stButton>button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.title("⚙️ Navigation Menu")

    st.markdown("---")

    page = st.radio(
        "Select Feature",
        [
            "🏠 Home",
            "🔄 Unit Converter",
            "🧪 Material Density Checker"
        ]
    )

    st.markdown("---")

    st.success("Mechanical Engineering Toolkit v1.0")

    st.info("Designed using Python & Streamlit")

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown('<div class="main-title">⚙️ Mechanical Engineering Toolkit</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">Mechanical Unit Converter & Material Density Checker</div>',
        unsafe_allow_html=True
    )

    # Student Information Card
    st.markdown(f"""
    <div class="info-card">
        <h3>🎓 Student Information</h3>
        <hr>
        <p><b>👩 Full Name:</b> Aasiya Ismail</p>
        <p><b>🆔 Roll Number:</b> 25-ME-52</p>
        <p><b>🏛️ Department:</b> Mechanical Engineering</p>
    </div>
    """, unsafe_allow_html=True)

    # Welcome Message
    st.success("✅ Welcome to the Mechanical Engineering Toolkit")

    st.write("""
    This professional web application is designed for Mechanical Engineering students 
    and professionals to perform quick engineering calculations and material property checks.
    """)

    # Project Features
    st.markdown('<div class="section-header">📌 Project Features</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        ### 🔄 Mechanical Unit Converter
        
        Convert:
        - Length
        - Force
        - Pressure
        - Temperature
        - Speed
        """)

    with col2:
        st.info("""
        ### 🧪 Material Density Checker
        
        Check:
        - Material Density
        - Engineering Properties
        - Industrial Applications
        """)

    # Expandable Section
    with st.expander("📖 About This Project"):
        st.write("""
        This project was developed using:
        - Python
        - Streamlit
        - GitHub
        - Streamlit Cloud
        
        The objective is to create a modern engineering toolkit with 
        a clean and user-friendly interface.
        """)

# =========================================================
# UNIT CONVERTER PAGE
# =========================================================

elif page == "🔄 Unit Converter":

    st.markdown('<div class="section-header">🔄 Mechanical Unit Converter</div>', unsafe_allow_html=True)

    st.write("Convert engineering units accurately and efficiently.")

    # Select Conversion Category
    category = st.selectbox(
        "Select Conversion Category",
        [
            "Length",
            "Force",
            "Pressure",
            "Temperature",
            "Speed"
        ]
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # =====================================================
    # LENGTH CONVERSION
    # =====================================================

    if category == "Length":

        units = {
            "meter": 1,
            "centimeter": 0.01,
            "millimeter": 0.001,
            "inch": 0.0254,
            "foot": 0.3048
        }

        with col1:
            value = st.number_input("Enter Value", value=1.0)
            from_unit = st.selectbox("From Unit", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To Unit", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # FORCE CONVERSION
    # =====================================================

    elif category == "Force":

        units = {
            "Newton": 1,
            "kiloNewton": 1000
        }

        with col1:
            value = st.number_input("Enter Force Value", value=1.0)
            from_unit = st.selectbox("From Unit", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To Unit", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # PRESSURE CONVERSION
    # =====================================================

    elif category == "Pressure":

        units = {
            "Pascal": 1,
            "bar": 100000,
            "psi": 6894.76
        }

        with col1:
            value = st.number_input("Enter Pressure Value", value=1.0)
            from_unit = st.selectbox("From Unit", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To Unit", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # TEMPERATURE CONVERSION
    # =====================================================

    elif category == "Temperature":

        with col1:
            value = st.number_input("Enter Temperature", value=25.0)
            from_unit = st.selectbox(
                "From Unit",
                ["Celsius", "Fahrenheit", "Kelvin"]
            )

        with col2:
            to_unit = st.selectbox(
                "To Unit",
                ["Celsius", "Fahrenheit", "Kelvin"]
            )

        # Conversion Logic
        if from_unit == to_unit:
            result = value

        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            else:
                result = value + 273.15

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (value - 32) * 5/9
            else:
                result = ((value - 32) * 5/9) + 273.15

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = value - 273.15
            else:
                result = ((value - 273.15) * 9/5) + 32

        st.metric("Converted Value", f"{result:.2f}")

    # =====================================================
    # SPEED CONVERSION
    # =====================================================

    elif category == "Speed":

        units = {
            "m/s": 1,
            "km/h": 0.277778
        }

        with col1:
            value = st.number_input("Enter Speed", value=1.0)
            from_unit = st.selectbox("From Unit", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To Unit", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # Reset Button
    if st.button("🔄 Reset Converter"):
        st.rerun()

# =========================================================
# MATERIAL DENSITY CHECKER
# =========================================================

elif page == "🧪 Material Density Checker":

    st.markdown('<div class="section-header">🧪 Material Density Checker</div>', unsafe_allow_html=True)

    st.write("Check density and engineering properties of common materials.")

    # Material Database
    materials = {

        "Steel": {
            "density": 7850,
            "description": "High strength and durability material widely used in structures and machinery.",
            "application": "Construction, machine parts, automotive structures"
        },

        "Aluminum": {
            "density": 2700,
            "description": "Lightweight and corrosion-resistant metal.",
            "application": "Aircraft bodies, automobile panels, heat exchangers"
        },

        "Copper": {
            "density": 8960,
            "description": "Excellent conductor of heat and electricity.",
            "application": "Electrical wiring, motors, heat transfer equipment"
        },

        "Brass": {
            "density": 8500,
            "description": "Copper-zinc alloy with excellent machinability.",
            "application": "Valves, fittings, musical instruments"
        },

        "Cast Iron": {
            "density": 7200,
            "description": "Strong compression-resistant material.",
            "application": "Engine blocks, pipes, machine bases"
        },

        "Titanium": {
            "density": 4500,
            "description": "Very strong and lightweight metal with corrosion resistance.",
            "application": "Aerospace, biomedical implants, racing components"
        }
    }

    selected_material = st.selectbox(
        "Select Engineering Material",
        list(materials.keys())
    )

    st.markdown("---")

    density_kg = materials[selected_material]["density"]
    density_g = density_kg / 1000

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Density (kg/m³)", f"{density_kg:,}")

    with col2:
        st.metric("Density (g/cm³)", f"{density_g:.3f}")

    st.info(f"📘 Description: {materials[selected_material]['description']}")

    st.success(f"🏭 Industrial Application: {materials[selected_material]['application']}")

    with st.expander("📚 Engineering Explanation"):
        st.write("""
        Density is one of the most important material properties in mechanical engineering.
        It affects:
        - Weight
        - Strength-to-weight ratio
        - Structural design
        - Manufacturing applications
        """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
⚙️ Developed using Python & Streamlit | Mechanical Engineering Mini Project
</div>
""", unsafe_allow_html=True)
