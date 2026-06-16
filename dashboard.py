import streamlit as st
import requests
import time
import pandas as pd

st.title("🚨 Real-Time DDoS Detection")

if "data" not in st.session_state:
    st.session_state.data = []

placeholder = st.empty()

while True:
    try:
        res = requests.get("http://127.0.0.1:5000/status").json()

        result = res["prediction"]
        rate = res.get("rate", 0)

        st.session_state.data.append({
            "time": time.time(),
            "rate": rate,
            "attack": 1 if result == "Attack" else 0
        })

        df = pd.DataFrame(st.session_state.data)
        df["time"] -= df["time"].min()

        with placeholder.container():
            st.subheader("📈 Live Traffic Graph")
            st.line_chart(df[["rate", "attack"]])

            if result == "Attack":
                st.error("🚨 Attack Detected")
            else:
                st.success("✅ Normal")

        time.sleep(0.5)

    except:
        st.warning("Waiting for Flask...")
        time.sleep(1)