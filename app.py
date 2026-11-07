import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jirjir Health Centre Intelligence Platform",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS for World-Class UI
st.markdown("""
    <style>
    .main-header {font-size: 2rem; color: #1E3A8A; font-weight: 700;}
    .sub-header {font-size: 1.1rem; color: #475569; font-weight: 500;}
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🏥 Jirjir Health Centre - Advanced Health Intelligence")
st.markdown("### Monthly Data Management & Clinical Analysis Report — November 2026")
st.markdown("---")

# --- ENTERPRISE MODULAR CONTROL PANEL ---
st.markdown("#### ⚙️ Enterprise Dashboard View Controls")
ctrl_col1, ctrl_col2 = st.columns(2)

with ctrl_col1:
    selected_view = st.selectbox(
        "📂 Select Project Section to View", 
        [
            "Full Comprehensive Dashboard", 
            "1. OPD Visits Overview", 
            "2. Top 5 Major Diseases & Charts", 
            "3. Nutrition Screening & Analysis"
        ]
    )

with ctrl_col2:
    facility_status = st.selectbox(
        "🏥 Facility Operational Status", 
        ["Jirjir Health Centre — Active & Verified", "Pending Review"]
    )

st.markdown("---")

# --- DATASETS ---
diseases_data = {
    "Disease Name": ["ARI", "Pneumonia", "Acute Watery Diarrhoea", "Unknown Fever", "UTI"],
    "Over 5 (Male)": [15, 17, 5, 4, 5],
    "Over 5 (Female)": [13, 15, 7, 3, 6],
    "Under 5 (Male)": [10, 14, 7, 4, 1],
    "Under 5 (Female)": [13, 12, 9, 3, 2]
}

df_diseases = pd.DataFrame(diseases_data)
df_diseases["Total Cases"] = (
    df_diseases["Over 5 (Male)"] + df_diseases["Over 5 (Female)"] + 
    df_diseases["Under 5 (Male)"] + df_diseases["Under 5 (Female)"]
)

# --- SECTION 1: OPD VISITS OVERVIEW ---
if selected_view in ["Full Comprehensive Dashboard", "1. OPD Visits Overview"]:
    st.subheader("📊 OPD Visits Overview (Jirjir Health Centre)")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Visitors", "255", "100%")
    col2.metric("OPD Over 5 Years", "130", "Male: 60 | Female: 70")
    col3.metric("OPD Under 5 Years", "125", "Male: 65 | Female: 60")
    col4.metric("Reporting Status", "Verified", "✅ Active")

    st.markdown("---")

# --- SECTION 2: 5 MAJOR DISEASES & CHARTS ---
if selected_view in ["Full Comprehensive Dashboard", "2. Top 5 Major Diseases & Charts"]:
    st.subheader("🦠 Top 5 Major Diseases Burden & Distribution")
    st.dataframe(df_diseases, use_container_width=True)

    st.markdown("### 📈 Disease Distribution Visual Chart")
    chart_data_diseases = df_diseases.set_index("Disease Name")[["Over 5 (Male)", "Over 5 (Female)", "Under 5 (Male)", "Under 5 (Female)"]]
    st.bar_chart(chart_data_diseases)

    st.markdown("---")

# --- SECTION 3: NUTRITION SCREENING ANALYSIS & CHARTS ---
if selected_view in ["Full Comprehensive Dashboard", "3. Nutrition Screening & Analysis"]:
    st.subheader("🥗 Nutrition Screening & Malnutrition Status (Total: 300 Screened)")

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    col_n1.metric("Total Screened", "300", "100%")
    col_n2.metric("Normal Status", "85 (28.3%)", "M: 40 | F: 45")
    col_n3.metric("MAM (Moderate)", "190 (63.3%)", "M: 80 | F: 110")
    col_n4.metric("SAM (Severe)", "25 (8.3%)", "M: 10 | F: 15")

    nutrition_data = {
        "Nutritional Status": ["Normal", "MAM (Moderate)", "SAM (Severe)"],
        "Male": [40, 80, 10],
        "Female": [45, 110, 15]
    }

    df_nutrition = pd.DataFrame(nutrition_data)
    st.table(df_nutrition)

    st.markdown("### 📊 Nutrition Screening Visual Chart (Male vs Female)")
    chart_data_nutrition = df_nutrition.set_index("Nutritional Status")
    st.bar_chart(chart_data_nutrition)

    st.markdown("---")

# --- EXPORT & DOWNLOAD REPORT BUTTON ---
st.subheader("📥 Export & Share Reports")

csv_data = df_diseases.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download November 2026 Disease Report (CSV)",
    data=csv_data,
    file_name='Jirjir_Health_Diseases_November_2026.csv',
    mime='text/csv',
)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Jirjir Health Centre Intelligence Platform — World-Class Healthcare Analytics Suite © 2026</p>", unsafe_allow_html=True)
