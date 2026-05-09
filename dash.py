import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide")

st.title("Smart Health Monitoring Dashboard")

if not os.path.exists("health_data.csv"):
    data = []
    for t in range(1, 25):
        data.append([
            t,
            np.random.randint(60, 120),
            np.random.randint(90, 100),
            round(np.random.uniform(36, 39), 1)
        ])
    pd.DataFrame(data, columns=["Time", "HeartRate", "SpO2", "Temperature"]).to_csv("health_data.csv", index=False)

if st.button("Generate New Data"):
    data = []
    for t in range(1, 25):
        data.append([
            t,
            np.random.randint(60, 120),
            np.random.randint(90, 100),
            round(np.random.uniform(36, 39), 1)
        ])
    pd.DataFrame(data, columns=["Time", "HeartRate", "SpO2", "Temperature"]).to_csv("health_data.csv", index=False)

df = pd.read_csv("health_data.csv")

st.header("Patient Data")
st.dataframe(df, hide_index=True)

st.header("Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Heart Rate", round(df["HeartRate"].mean(), 2))

with col2:
    st.metric("Max Heart Rate", df["HeartRate"].max())

with col3:
    st.metric("Min Heart Rate", df["HeartRate"].min())

st.header("Health Trends")
df_chart = df.set_index("Time")
st.line_chart(df_chart)

st.header("Risk Analysis")

high_risk = df[
    (df["HeartRate"] > 110) |
    (df["SpO2"] < 92) |
    (df["Temperature"] > 38)
]

if not high_risk.empty:
    st.error("High Risk Cases Detected")
    st.dataframe(high_risk, hide_index=True)
else:
    st.success("All readings are within normal range")