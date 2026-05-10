# =========================================================
# Mechanical Unit Converter & Material Density Checker
# Developed Using Python & Streamlit
# =========================================================

# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Mechanical Engineering Toolkit",
    page_icon="⚙️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS STYLING
# =========================================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #020617;
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: #ffffff;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Glassmorphism Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 4px 25px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Section Headers */
.section-header {
    font-size: 28px;
    font-weight: bold;
    color: #38bdf8;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #06b6d4, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 48px;
    font-size: 17px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #0891b2, #2563eb);
}

/* Metric Styling */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

/* Input Boxes */
.stTextInput input,
.stNumberInput input,
.stSelectbox div {
    background-color: #1e293b;
    color: white;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    padding-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("⚙️ Engineering Toolkit")

    st.markdown("---")

    page = st.radio(
        "📌 Navigation",
        [
            "🏠 Home",
            "🔄 Unit Converter",
            "🧪 Density Checker"
        ]
    )

    st.markdown("---")

    st.success("Mechanical Engineering Project")

    st.info("Developed using Streamlit")

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">⚙️ Mechanical Engineering Toolkit</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Mechanical Unit Converter & Material Density Checker</div>',
        unsafe_allow_html=True
    )

    # Student Information Card
    st.markdown("""
    <div class="glass-card">
        <h2>🎓 Student Information</h2>
        <hr>
        <h4>👩 Full Name: Aasiya Ismail</h4>
        <h4>🆔 Roll Number: 25-ME-52</h4>
        <h4>🏛️ Department: Mechanical Engineering</h4>
    </div>
    """, unsafe_allow_html=True)

    # Welcome Banner
    st.success("✅ Welcome to the Professional Mechanical Engineering Toolkit")

    # Features
    st.markdown(
        '<div class="section-header">📌 Project Features</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="glass-card">
            <h3>🔄 Mechanical Unit Converter</h3>
            <p>
            Convert engineering units including:
            </p>
            <ul>
                <li>Length</li>
                <li>Force</li>
                <li>Pressure</li>
                <li>Temperature</li>
                <li>Speed</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass-card">
            <h3>🧪 Material Density Checker</h3>
            <p>
            Check engineering material properties:
            </p>
            <ul>
                <li>Density</li>
                <li>Applications</li>
                <li>Descriptions</li>
                <li>Industrial Uses</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Expandable Section
    with st.expander("📖 About This Project"):

        st.write("""
        This project was developed using Python and Streamlit.

        It is designed for Mechanical Engineering students to perform
        engineering calculations and material analysis using a clean
        and modern interface.
        """)

# =========================================================
# UNIT CONVERTER
# =========================================================

elif page == "🔄 Unit Converter":

    st.markdown(
        '<div class="section-header">🔄 Mechanical Unit Converter</div>',
        unsafe_allow_html=True
    )

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

    col1, col2 = st.columns(2)

    # =====================================================
    # LENGTH
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
            from_unit = st.selectbox("From", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # FORCE
    # =====================================================

    elif category == "Force":

        units = {
            "Newton": 1,
            "kiloNewton": 1000
        }

        with col1:
            value = st.number_input("Enter Force", value=1.0)
            from_unit = st.selectbox("From", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # PRESSURE
    # =====================================================

    elif category == "Pressure":

        units = {
            "Pascal": 1,
            "bar": 100000,
            "psi": 6894.76
        }

        with col1:
            value = st.number_input("Enter Pressure", value=1.0)
            from_unit = st.selectbox("From", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # =====================================================
    # TEMPERATURE
    # =====================================================

    elif category == "Temperature":

        with col1:
            value = st.number_input("Enter Temperature", value=25.0)
            from_unit = st.selectbox(
                "From",
                ["Celsius", "Fahrenheit", "Kelvin"]
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                ["Celsius", "Fahrenheit", "Kelvin"]
            )

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
    # SPEED
    # =====================================================

    elif category == "Speed":

        units = {
            "m/s": 1,
            "km/h": 0.277778
        }

        with col1:
            value = st.number_input("Enter Speed", value=1.0)
            from_unit = st.selectbox("From", list(units.keys()))

        with col2:
            to_unit = st.selectbox("To", list(units.keys()))

        result = value * units[from_unit] / units[to_unit]

        st.metric("Converted Value", f"{result:.4f} {to_unit}")

    # Reset Button
    if st.button("🔄 Reset Converter"):
        st.rerun()

# =========================================================
# DENSITY CHECKER
# =========================================================

elif page == "🧪 Density Checker":

    st.markdown(
        '<div class="section-header">🧪 Material Density Checker</div>',
        unsafe_allow_html=True
    )

    materials = {

        "Steel": {
            "density": 7850,
            "description": "Strong and durable engineering material.",
            "application": "Buildings, bridges, machinery"
        },

        "Aluminum": {
            "density": 2700,
            "description": "Lightweight and corrosion resistant.",
            "application": "Aircraft, automobiles, heat exchangers"
        },

        "Copper": {
            "density": 8960,
            "description": "Excellent electrical conductor.",
            "application": "Electrical systems, motors"
        },

        "Brass": {
            "density": 8500,
            "description": "Copper-zinc alloy with good machinability.",
            "application": "Valves, fittings, decorative parts"
        },

        "Cast Iron": {
            "density": 7200,
            "description": "High compressive strength material.",
            "application": "Engine blocks, pipes"
        },

        "Titanium": {
            "density": 4500,
            "description": "Very strong and lightweight.",
            "application": "Aerospace, medical implants"
        }
    }

    selected_material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density_kg = materials[selected_material]["density"]
    density_g = density_kg / 1000

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Density (kg/m³)", f"{density_kg:,}")

    with col2:
        st.metric("Density (g/cm³)", f"{density_g:.3f}")

    st.info(f"📘 Description: {materials[selected_material]['description']}")

    st.success(f"🏭 Application: {materials[selected_material]['application']}")

    with st.expander("📖 Learn More"):

        st.write("""
        Density is a critical engineering property that affects:
        - Weight
        - Structural strength
        - Design efficiency
        - Material selection
        """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
⚙️ Developed Using Python & Streamlit | Mechanical Engineering Mini Project
</div>
""", unsafe_allow_html=True)
