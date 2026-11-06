import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Jirjir Health Centre Intelligence",
    page_icon="🏥",
    layout="wide"
)

# App Header
st.title("🏥 Jirjir Health Centre - Data Health Management & Analysis")
st.markdown("### Monthly Report: November 2026")
st.markdown("---")

# 1. OPD Summary Metrics
st.subheader("📊 OPD Visits Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total OPD Visitors", "255", "November 2026")
col2.metric("OPD Over 5 Years", "130", "Male: 60 | Female: 70")
col3.metric("OPD Under 5 Years", "125", "Male: 65 | Female: 60")

st.markdown("---")

# 2. 5 Major Diseases Analysis Table
st.subheader("🦠 Top 5 Major Diseases Breakdown")

diseases_data = {
    "Disease Name": ["ARI", "Pneumonia", "Acute Watery Diarrhoea", "Unknown Fever", "UTI"],
    "Over 5 (Male)": [15, 17, 5, 4, 5],
    "Over 5 (Female)": [13, 15, 7, 3, 6],
    "Under 5 (Male)": [10, 14, 7, 4, 1],
    "Under 5 (Female)": [13, 12, 9, 3, 2]
}

df_diseases = pd.DataFrame(diseases_data)
st.dataframe(df_diseases, use_container_width=True)

# Visualizing Diseases with a Bar Chart
st.markdown("### 📈 Disease Distribution Chart")
df_chart = df_diseases.set_index("Disease Name")
st.bar_chart(df_chart)

st.markdown("---")

# 3. Nutrition Screening Analysis
st.subheader("🥗 Nutrition Screening (Total: 300 Screened)")

col_n1, col_n2, col_n3 = st.columns(3)
col_n1.metric("Normal Status", "85", "Male: 40 | Female: 45")
col_n2.metric("MAM (Moderate)", "190", "Male: 80 | Female: 110")
col_n3.metric("SAM (Severe)", "25", "Male: 10 | Female: 15")

nutrition_data = {
    "Nutritional Status": ["Normal", "MAM", "SAM", "Total Screened"],
    "Male": [40, 80, 10, 130],
    "Female": [45, 110, 15, 170],
    "Total": [85, 190, 25, 300]
}

df_nutrition = pd.DataFrame(nutrition_data)
st.table(df_nutrition)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Jirjir Health Centre Data Analytics Dashboard — November 2026</p>", unsafe_allow_html=True)
