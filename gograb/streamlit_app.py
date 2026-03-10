import streamlit as st
from auth_ui import signup_ui, login_ui
from dashboard_ui import dashboard_ui

st.set_page_config(page_title="GoGrab", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ---------- AUTH ----------
if not st.session_state["logged_in"]:
    tab1, tab2 = st.tabs(["📝 Sign Up", "🔐 Login"])

    with tab1:
        signup_ui()

    with tab2:
        login_ui()

else:
    dashboard_ui()
