import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Streamlit Dockerized App",
    page_icon="🌐",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Data Explorer", "📈 Visualization"])

# 🏠 Home Page
if page == "🏠 Home":
    st.title("Welcome to Dockerized Streamlit App! 🎉")
    st.write(
        """
        - This app demonstrates the capabilities of Dockerized Streamlit Applications.
        - You can:
            - Upload and explore CSV data 📊
            - Visualize interactive charts and graphs 📈
        """
    )
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=300)

# 📊 Data Explorer
elif page == "📊 Data Explorer":
    st.title("Upload and Explore Your CSV Data 📊")
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("✅ **Data Preview:**")
        st.dataframe(df.head(10))

        st.write("🔍 **Summary:**")
        st.write(df.describe())

        st.write("🔢 **Column Information:**")
        st.write(df.info())

# 📈 Visualization Page
elif page == "📈 Visualization":
    st.title("Create Interactive Visualizations 📈")
    uploaded_file = st.file_uploader("Upload CSV File for Visualization", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        chart_type = st.selectbox(
            "Select Visualization Type",
            ["Line Chart", "Bar Chart", "Scatter Plot"]
        )

        st.write("📊 **Data Preview:**")
        st.dataframe(df.head(10))

        x_axis = st.selectbox("Select X-axis:", df.columns)
        y_axis = st.selectbox("Select Y-axis:", df.columns)

        if chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"📈 {chart_type}")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"📊 {chart_type}")
        elif chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"🌐 {chart_type}")
        
        st.plotly_chart(fig)

# 🎯 Footer
st.sidebar.markdown("---")
st.sidebar.write("📚 **Dockerized Streamlit Development Environment** © 2025")

