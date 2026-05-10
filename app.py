import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mechanical Engineering Project", page_icon="⚙️", layout="wide")

# --- CUSTOM CSS FOR HIGH VISIBILITY ---
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Highlighted Student Info Header */
    .header-box {
        background-color: #1e3a8a; /* Dark Blue */
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-box h1 {
        margin: 0;
        font-size: 32px;
    }
    .header-box h2 {
        margin: 10px 0 0 0;
        color: #fbbf24; /* Gold/Amber for the Roll No */
        font-weight: bold;
    }
    
    /* Card styling for features */
    .feature-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP VISIBILITY HEADER (Visible on every page) ---
st.markdown(f"""
    <div class="header-box">
        <h1>Mechanical Unit Converter & Material Checker</h1>
        <h2>Student: Aasiya Ismail | Roll No: 25-ME-52</h2>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Menu")
    selection = st.radio("Select Feature:", ["Project Dashboard", "Unit Converter", "Material Density Checker"])
    st.markdown("---")
    st.write("**Course:** Mechanical Engineering")
    st.write("**Semester:** Spring 2026")

# --- DASHBOARD / HOME ---
if selection == "Project Dashboard":
    st.subheader("Welcome to the Engineering Toolkit")
    st.info("This application provides real-time conversions and material property data for mechanical engineering design.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("✅ **Unit Converter** includes Force, Pressure, and Temperature.")
    with col_b:
        st.success("✅ **Material Checker** includes Density and Descriptions.")

# --- UNIT CONVERTER PAGE ---
elif selection == "Unit Converter":
    st.subheader("🔄 Mechanical Unit Converter")
    
    category = st.selectbox("Measurement Type", ["Length", "Force", "Pressure", "Temperature", "Speed"])
    
    c1, c2 = st.columns(2)
    
    if category == "Length":
        with c1:
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["meter", "centimeter", "millimeter", "inch", "foot"])
        with c2:
            u_to = st.selectbox("To", ["meter", "centimeter", "millimeter", "inch", "foot"])
        conv = {"meter": 1.0, "centimeter": 0.01, "millimeter": 0.001, "inch": 0.0254, "foot": 0.3048}
        res = val * conv[u_from] / conv[u_to]
        st.metric("Converted Value", f"{res:.4f} {u_to}")

    elif category == "Force":
        with c1:
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["Newton", "kiloNewton"])
        with c2:
            u_to = st.selectbox("To", ["Newton", "kiloNewton"])
        f = 1000 if u_from == "kiloNewton" and u_to == "Newton" else (0.001 if u_from == "Newton" and u_to == "kiloNewton" else 1)
        st.metric("Converted Value", f"{val * f:.4f} {u_to}")

    elif category == "Pressure":
        with c1:
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["Pascal", "bar", "psi"])
        with c2:
            u_to = st.selectbox("To", ["Pascal", "bar", "psi"])
        conv = {"Pascal": 1.0, "bar": 100000.0, "psi": 6894.76}
        res = val * conv[u_from] / conv[u_to]
        st.metric("Converted Value", f"{res:.4f} {u_to}")

    elif category == "Temperature":
        with c1:
            val = st.number_input("Value", value=25.0)
            u_from = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        with c2:
            u_to = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        if u_from == u_to: res = val
        elif u_from == "Celsius":
            res = (val * 9/5) + 32 if u_to == "Fahrenheit" else val + 273.15
        elif u_from == "Fahrenheit":
            res = (val - 32) * 5/9 if u_to == "Celsius" else (val - 32) * 5/9 + 273.15
        elif u_from == "Kelvin":
            res = val - 273.15 if u_to == "Celsius" else (val - 273.15) * 9/5 + 32
        st.metric("Converted Value", f"{res:.2f} {u_to}")

    elif category == "Speed":
        with c1:
            val = st.number_input("Value", value=1.0)
            u_from = st.selectbox("From", ["m/s", "km/h"])
        with c2:
            u_to = st.selectbox("To", ["m/s", "km/h"])
        f = 3.6 if u_from == "m/s" and u_to == "km/h" else (1/3.6 if u_from == "km/h" and u_to == "m/s" else 1)
        st.metric("Converted Value", f"{val * f:.4f} {u_to}")

# --- MATERIAL DENSITY PAGE ---
elif selection == "Material Density Checker":
    st.subheader("🧪 Material Density Checker")
    
    materials = {
        "Steel": {"density": 7850, "desc": "High strength, primary structural alloy of iron and carbon."},
        "Aluminum": {"density": 2700, "desc": "Low density, excellent corrosion resistance for aerospace."},
        "Copper": {"density": 8960, "desc": "Excellent conductor of heat and electricity."},
        "Brass": {"density": 8500, "desc": "Low-friction alloy of copper and zinc."},
        "Cast Iron": {"density": 7200, "desc": "Brittle but excellent for damping and casting."},
        "Titanium": {"density": 4500, "desc": "High strength-to-weight ratio, extreme corrosion resistance."}
    }
    
    selected_mat = st.selectbox("Select Material", list(materials.keys()))
    
    d_kg = materials[selected_mat]["density"]
    d_g = d_kg / 1000
    
    st.markdown("---")
    m1, m2 = st.columns(2)
    m1.metric("Density (kg/m³)", f"{d_kg:,}")
    m2.metric("Density (g/cm³)", f"{d_g:.3f}")
    
    st.info(f"**Engineering Note:** {materials[selected_mat]['desc']}")
