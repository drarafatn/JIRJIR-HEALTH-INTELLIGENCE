import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Jirjir Health Centre Intelligence Platform",
    page_icon="🏥",
    layout="wide"
)

# App Header
st.title("🏥 Jirjir Health Centre - Advanced Health Intelligence")
st.markdown("### Monthly Data Management & Clinical Analysis Report — November 2026")
st.markdown("---")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Dashboard Controls & Filters")
selected_centre = st.sidebar.selectbox("Select Health Facility", ["Jirjir Health Centre", "Xawadle Health Centre", "Qulujeed Health Centre"])
selected_month = st.sidebar.selectbox("Select Reporting Period", ["November 2026", "October 2026", "September 2026"])
view_mode = st.sidebar.radio("View Analytics Mode", ["Full Dashboard", "5 Major Diseases Chart", "Nutrition Breakdown"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Enterprise System:** Compliant with regional health standards and real-time clinical metrics.")

# --- 1. OPD SUMMARY METRICS ---
if view_mode in ["Full Dashboard", "5 Major Diseases Chart"]:
    st.subheader(f"📊 OPD Visits Overview ({selected_centre})")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Visitors", "255", "100%")
    col2.metric("OPD Over 5 Years", "130", "Male: 60 | Female: 70")
    col3.metric("OPD Under 5 Years", "125", "Male: 65 | Female: 60")
    col4.metric("Reporting Status", "Verified", "✅ Active")

    st.markdown("---")

# --- 2. 5 MAJOR DISEASES ANALYSIS & CHARTS ---
if view_mode in ["Full Dashboard", "5 Major Diseases Chart"]:
    st.subheader("🦠 Top 5 Major Diseases Burden & Distribution")

    diseases_data = {
        "Disease Name": ["ARI", "Pneumonia", "Acute Watery Diarrhoea", "Unknown Fever", "UTI"],
        "Over 5 (Male)": [15, 17, 5, 4, 5],
        "Over 5 (Female)": [13, 15, 7, 3, 6],
        "Under 5 (Male)": [10, 14, 7, 4, 1],
        "Under 5 (Female)": [13, 12, 9, 3, 2]
    }

    df_diseases = pd.DataFrame(diseases_data)
    
    # Calculate Total Cases per Disease
    df_diseases["Total Cases"] = (
        df_diseases["Over 5 (Male)"] + df_diseases["Over 5 (Female)"] + 
        df_diseases["Under 5 (Male)"] + df_diseases["Under 5 (Female)"]
    )
    
    st.dataframe(df_diseases, use_container_width=True)

    # Professional Native Bar Chart (Stable on Mobile)
    st.markdown("### 📈 Disease Distribution Visual Chart")
    chart_data = df_diseases.set_index("Disease Name")[["Over 5 (Male)", "Over 5 (Female)", "Under 5 (Male)", "Under 5 (Female)"]]
    st.bar_chart(chart_data)

    st.markdown("---")

# --- 3. NUTRITION SCREENING ANALYSIS ---
if view_mode in ["Full Dashboard", "Nutrition Breakdown"]:
    st.subheader("🥗 Nutrition Screening & Malnutrition Status (Total: 300 Screened)")

    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    col_n1.metric("Total Screened", "300", "100%")
    col_n2.metric("Normal Status", "85 (28.3%)", "M: 40 | F: 45")
    col_n3.metric("MAM (Moderate)", "190 (63.3%)", "M: 80 | F: 110")
    col_n4.metric("SAM (Severe)", "25 (8.3%)", "M: 10 | F: 15")

    nutrition_data = {
        "Nutritional Status": ["Normal", "MAM (Moderate Acute Malnutrition)", "SAM (Severe Acute Malnutrition)", "Total"],
        "Male": [40, 80, 10, 130],
        "Female": [45, 110, 15, 170],
        "Total Count": [85, 190, 25, 300],
        "Percentage (%)": ["28.3%", "63.3%", "8.3%", "100.0%"]
    }

    df_nutrition = pd.DataFrame(nutrition_data)
    st.table(df_nutrition)

# --- 4. EXPORT & DOWNLOAD REPORT BUTTON ---
st.markdown("---")
st.subheader("📥 Export & Share Reports")

csv_data = df_diseases.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download 5 Major Diseases Report (CSV)",
    data=csv_data,
    file_name=f'Jirjir_Health_Diseases_{selected_month}.csv',
    mime='text/csv',
)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Jirjir Health Centre Intelligence Platform — World-Class Healthcare Analytics Suite © 2026</p>", unsafe_allow_html=True)
