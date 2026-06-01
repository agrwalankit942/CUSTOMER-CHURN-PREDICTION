import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go # type: ignore
import plotly.express as px # pyright: ignore[reportMissingImports]

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Customer Churn Intelligence System",
    page_icon="🌳",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: white;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #333;
}

div[data-testid="stSidebar"] {
    background-color: #161B22;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================
st.title("🌳 Customer Churn Intelligence Dashboard")
st.markdown("""
AI-powered Random Forest Machine Learning System for predicting customer churn risk.
""")

# =====================================================
# LOAD MODEL
# =====================================================
model = joblib.load("rf_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("📊 Customer Input Panel")
st.sidebar.markdown("---")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

monthly_charges = st.sidebar.slider(
    "Monthly Charges ($)",
    18.0,
    120.0,
    70.0
)

avg_spend = st.sidebar.slider(
    "Average Monthly Spend ($)",
    0.0,
    120.0,
    65.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Built using Streamlit + Random Forest")

# =====================================================
# ENCODING MAPS
# =====================================================
contract_map = {
    "Month-to-month": [1, 0],
    "One year": [0, 1],
    "Two year": [0, 0]
}

internet_map = {
    "Fiber optic": [1, 0],
    "DSL": [0, 1],
    "No": [0, 0]
}

# =====================================================
# CREATE INPUT DATA
# =====================================================
input_data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges],
    "AvgMonthlySpend": [avg_spend],
    "Contract_Month-to-month": [contract_map[contract][0]],
    "Contract_One year": [contract_map[contract][1]],
    "InternetService_Fiber optic": [internet_map[internet][0]],
    "InternetService_DSL": [internet_map[internet][1]]
})

# Align columns
input_data = input_data.reindex(columns=feature_names, fill_value=0)

# =====================================================
# TABS
# =====================================================
tab1, tab2 = st.tabs([
    "🔮 Churn Prediction",
    "📂 Bulk Prediction"
])

# =====================================================
# TAB 1 - PREDICTION
# =====================================================
with tab1:

    st.subheader("Customer Risk Analysis")

    if st.button("🚀 Predict Customer Churn"):


        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        risk_score = round(probability * 100, 2)
        
        # =================================================
        # KPI CARDS
        # =================================================
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(
    "Risk Score",
    f"{risk_score}/100"
)
        col1.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

        col2.metric(
            "Tenure",
            f"{tenure} Months"
        )

        col3.metric(
            "Monthly Charges",
            f"${monthly_charges}"
        )

        col4.metric(
            "Contract",
            contract
        )

        st.markdown("---")

        # =================================================
        # GAUGE CHART
        # =================================================
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={'text': "Customer Churn Risk"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 60], 'color': "yellow"},
                    {'range': [60, 100], 'color': "salmon"}
                ]
            }
        ))

        st.plotly_chart(gauge_fig, use_container_width=True)

        # =================================================
        # PREDICTION STATUS
        # =================================================
        st.subheader("📌 Prediction Result")

        if probability < 0.25:
            st.success(f"✅ Low Churn Risk ({probability:.2%})")

        elif probability < 0.60:
            st.warning(f"⚠️ Medium Churn Risk ({probability:.2%})")

        else:
            st.error(f"❌ High Churn Risk ({probability:.2%})")

        # =================================================
        # CUSTOMER SUMMARY
        # =================================================
        st.subheader("🧾 Customer Summary")

        st.info(f"""
### Customer Insights

• Contract Type: {contract}

• Internet Service: {internet}

• Monthly Charges: ${monthly_charges:.2f}

• Average Monthly Spend: ${avg_spend:.2f}

• Customer Tenure: {tenure} Months

Business Interpretation:

Customers with shorter tenure,
month-to-month contracts,
and higher monthly charges
typically show elevated churn risk.
        """)
        # =================================================
        # FEATURE IMPORTANCE
        # =================================================
        st.subheader("🧠 Top Factors Affecting Churn")

        importance = pd.Series(
            model.feature_importances_,
            index=feature_names
        ).sort_values(ascending=False).head(10)

        importance_df = pd.DataFrame({
            "Feature": importance.index,
            "Importance": importance.values
        })

        fig = px.bar(
            importance_df,
            x="Importance",
            y="Feature",
            orientation='h',
            text="Importance",
            title="Feature Importance Analysis"
        )

        st.plotly_chart(fig, use_container_width=True)

        # =================================================
        # PREDICTION EXPLANATION
        # =================================================
        st.subheader("📖 Prediction Explanation")

        if probability > 0.60:
            st.error("""
            High churn probability detected.

            Possible reasons:
            - High monthly charges
            - Unstable month-to-month contract
            - Lower customer loyalty
            - Shorter customer tenure

            Suggested Action:
            Offer discounts or long-term plans.
            """)

        elif probability > 0.30:
            st.warning("""
            Moderate churn probability detected.

            Possible reasons:
            - Medium customer engagement
            - Moderate pricing sensitivity

            Suggested Action:
            Improve customer retention communication.
            """)

        else:
            st.success("""
            Low churn probability detected.

            Reasons:
            - Stable customer relationship
            - Long-term contract
            - Better retention indicators

            Suggested Action:
            Maintain customer satisfaction programs.
            """)

        
# =====================================================
# TAB 2 - BULK PREDICTION
# =====================================================

# =====================================================
# TAB 2 - BULK PREDICTION
# =====================================================

with tab2:

    st.subheader("📂 Bulk Customer Churn Prediction")

    uploaded_file = st.file_uploader(
        "Upload cleaned customer CSV file",
        type=["csv"]
    )

    if uploaded_file:

        # =====================================
        # LOAD FILE
        # =====================================

        bulk_df = pd.read_csv(uploaded_file)

        # =====================================
        # ALIGN FEATURES
        # =====================================

        bulk_input = bulk_df.reindex(
            columns=feature_names,
            fill_value=0
        )

        # =====================================
        # PREDICTIONS
        # =====================================

        bulk_df["Churn_Probability"] = (
            model.predict_proba(bulk_input)[:, 1]
        )

        bulk_df["Churn_Prediction"] = (
            bulk_df["Churn_Probability"] > 0.5
        ).astype(int)

        # =====================================
        # BULK SUMMARY
        # =====================================

        high_risk = (
            bulk_df["Churn_Prediction"] == 1
        ).sum()

        total_customers = len(bulk_df)

        avg_risk = (
            bulk_df["Churn_Probability"].mean()
            * 100
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Customers",
            total_customers
        )

        col2.metric(
            "High-Risk Customers",
            high_risk
        )

        col3.metric(
            "Average Risk",
            f"{avg_risk:.2f}%"
        )

        # =====================================
        # TOP HIGH-RISK CUSTOMERS
        # =====================================

        st.subheader(
            "🚨 Top 10 High-Risk Customers"
        )

        top_risk = (
            bulk_df
            .sort_values(
                "Churn_Probability",
                ascending=False
            )
            .head(10)
            .copy()
        )

        top_risk["Risk (%)"] = (
            top_risk["Churn_Probability"] * 100
        ).round(2)

        display_cols = [
            "tenure",
            "MonthlyCharges",
            "AvgMonthlySpend",
            "Risk (%)"
        ]

        display_cols = [
            col for col in display_cols
            if col in top_risk.columns
        ]

        st.dataframe(
            top_risk[display_cols],
            use_container_width=True
        )

        st.info("""
📌 Key Insights

• Customers with shorter tenure are more likely to churn.

• Higher monthly charges increase churn risk.

• New customers should be targeted with retention campaigns.

• Loyalty programs and discounts can reduce churn probability.
""")

        # =====================================
        # PREDICTION RESULTS
        # =====================================

        st.subheader(
            "📊 Prediction Results"
        )

        show_cols = [
            "tenure",
            "MonthlyCharges",
            "AvgMonthlySpend",
            "Churn_Probability",
            "Churn_Prediction"
        ]

        show_cols = [
            col for col in show_cols
            if col in bulk_df.columns
        ]

        st.dataframe(
            bulk_df[show_cols].head(),
            use_container_width=True
        )

        # =====================================
        # PIE CHART
        # =====================================

        st.subheader(
            "📈 Churn Distribution"
        )

        bulk_df["Churn_Label"] = (
            bulk_df["Churn_Prediction"]
            .map({
                0: "Customer Retained",
                1: "At Risk of Churn"
            })
        )

        churn_counts = (
            bulk_df["Churn_Label"]
            .value_counts()
        )

        pie_fig = px.pie(
            values=churn_counts.values,
            names=churn_counts.index,
            title="Customer Churn Distribution",
            color_discrete_sequence=[
                "darkgreen",
                "red"
            ],
            hole=0.4
        )

        pie_fig.update_traces(
            textinfo="percent+label"
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

        # =====================================
        # BULK INSIGHT
        # =====================================

        st.success(f"""
📊 Bulk Prediction Summary

• Total Customers Analysed: {total_customers}

• High-Risk Customers: {high_risk}

• Average Churn Risk: {avg_risk:.2f}%

💡 Recommendation:

Focus retention efforts on customers
with shorter tenure and higher monthly charges.
""")

        # =====================================
        # DOWNLOAD RESULTS
        # =====================================

        st.download_button(
            label="⬇️ Download Prediction Results",
            data=bulk_df.to_csv(index=False),
            file_name="rf_churn_predictions.csv",
            mime="text/csv"
        )
# =====================================================
# FOOTER
# =====================================================
st.sidebar.markdown("---")

st.sidebar.info("""
Model Information

Algorithm: Random Forest

Training Accuracy: 84.03%

Testing Accuracy: 80.55%

Target: Customer Churn Prediction
""")

st.caption("""
🌳 Random Forest Customer Churn Intelligence Dashboard
Built with Streamlit, Plotly, Scikit-learn
""")