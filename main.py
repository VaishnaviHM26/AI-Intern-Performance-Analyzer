import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ai_feedback import generate_feedback

# Login Credentials
users = {
    "admin": "admin123",
    "leader": "leader123",
    "intern": "intern123"
}

# Sidebar Login
st.sidebar.title("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Login Validation
if username in users and users[username] == password:

    st.success(f"Welcome {username}")

    st.title("AI Intern Performance Analyzer")

    # Upload CSV
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    # Read CSV
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_csv("sample_data.csv")

    # Search Filter
    search = st.text_input("Search Topic")

    if search:

        df = df[
            df["topic"].str.contains(
                search,
                case=False
            )
        ]

    # Trend Analysis
    df["percentage_change"] = (
        (df["new_score"] - df["old_score"]) / df["old_score"]
    ) * 100

    # Efficiency Detection
    def efficiency_status(row):

        if row["new_score"] < row["old_score"] and row["time_taken"] > 50:
            return "Inefficient"

        return "Efficient"

    df["efficiency"] = df.apply(
        efficiency_status,
        axis=1
    )

    # Dashboard
    st.subheader("Performance Data")
    st.dataframe(df)

    # Trend Analysis Chart
    st.subheader("Trend Analysis")

    st.bar_chart(
        df.set_index("topic")["percentage_change"]
    )

    # Efficiency Status
    st.subheader("Efficiency Status")

    st.write(
        df[["topic", "efficiency"]]
    )

    # Pie Chart Visualization
    st.subheader("Efficiency Distribution")

    efficiency_counts = df["efficiency"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        efficiency_counts,
        labels=efficiency_counts.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig)

    # AI Feedback
    st.subheader("AI Feedback")

    data = df.to_dict(orient="records")

    feedback = generate_feedback(data)

    st.write(feedback)

    # Download Report
    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Report",
        data=csv,
        file_name="intern_report.csv",
        mime="text/csv"
    )

else:

    st.warning("Please login first")