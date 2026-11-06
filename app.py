import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jirjir Health Centre Intelligence",
    page_icon="🏥",
    layout="wide"
)

# App Header
st.title("🏥 Jirjir Health Centre - Health Intelligence")
st.markdown("### Monthly Data Management & Analysis — November 2026")
st.markdown("---")

# --- 1. OPD SUMMARY METRICS ---
st.subheader("📊 OPD Visits Overview")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Visitors", "255", "100%")
col2.metric("OPD Over 5 Years", "130", "Male: 60 | Female: 70")
col3.metric("OPD Under 5 Years", "125", "Male: 65 | Female: 60")
col4.metric("Status", "Verified", "✅ Active")

st.markdown("---")

# --- 2. 5 MAJOR DISEASES ANALYSIS ---
st.subheader("🦠 Top 5 Major Diseases Breakdown")

diseases_data = {
    "Disease Name": ["ARI", "Pneumonia", "Acute Watery Diarrhoea", "Unknown Fever", "UTI"],
    "Over 5 (Male)": [15, 17, 5, 4, 5],
    "Over 5 (Female)": [13, 15, 7, 3, 6],
    "Under 5 (Male)": [10, 14, 7, 4, 1],
    "Under 5 (Female)": [13, 12, 9, 3, 2]
}

df_diseases = pd.DataFrame(diseases_data)

# Calculate Total Cases
df_diseases["Total Cases"] = (
    df_diseases["Over 5 (Male)"] + df_diseases["Over 5 (Female)"] + 
    df_diseases["Under 5 (Male)"] + df_diseases["Under 5 (Female)"]
)

st.dataframe(df_diseases, use_container_width=True)
st.markdown("---")

# --- 3. NUTRITION SCREENING ANALYSIS ---
st.subheader("🥗 Nutrition Screening (Total: 300 Screened)")

col_n1, col_n2, col_n3, col_n4 = st.columns(4)
col_n1.metric("Screened", "300", "100%")
col_n2.metric("Normal", "85 (28.3%)", "M: 40 | F: 45")
col_n3.metric("MAM", "190 (63.3%)", "M: 80 | F: 110")
col_n4.metric("SAM", "25 (8.3%)", "M: 10 | F: 15")

nutrition_data = {
    "Nutritional Status": ["Normal", "MAM (Moderate Acute Malnutrition)", "SAM (Severe Acute Malnutrition)", "Total"],
    "Male": [40, 80, 10, 130],
    "Female": [45, 110, 15, 170],
    "Total Count": [85, 190, 25, 300],
    "Percentage (%)": ["28.3%", "63.3%", "8.3%", "100.0%"]
}

df_nutrition = pd.DataFrame(nutrition_data)
st.table(df_nutrition)

# --- 4. DOWNLOAD REPORT ---
st.markdown("---")
csv_data = df_diseases.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Disease Report (CSV)",
    data=csv_data,
    file_name='Jirjir_Health_Diseases_Nov_2026.csv',
    mime='text/csv',
)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Jirjir Health Centre Intelligence Platform — November 2026</p>", unsafe_allow_html=True)
