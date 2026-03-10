import streamlit as st

# ---------------- SESSION STORE ----------------
if "USERS" not in st.session_state:
    st.session_state["USERS"] = {}

# ---------------- SIGN UP UI ----------------
def signup_ui():
    st.subheader("Join GoGrab")

    with st.form("signup_form"):
        col1, col2 = st.columns(2)

        with col1:
            signup_username = st.text_input("Username")
            signup_fullname = st.text_input("Full Name")
            signup_college = st.text_input("College")

        with col2:
            signup_email = st.text_input("Email")
            signup_year = st.selectbox(
                "Year",
                ["1st Year", "2nd Year", "3rd Year", "4th Year"]
            )
            signup_password = st.text_input("Password", type="password")

        submit = st.form_submit_button("🚀 Create Account")

        if submit:
            username = signup_username.strip().lower()

            if not all([
                username,
                signup_fullname,
                signup_email,
                signup_college,
                signup_password
            ]):
                st.error("All fields are required")
                return

            if username in st.session_state["USERS"]:
                st.error("Username already exists")
                return

            st.session_state["USERS"][username] = {
                "name": signup_fullname,
                "email": signup_email,
                "year": signup_year,
                "college": signup_college,
                "password": signup_password
            }

            st.success("Account created! Please login.")

# ---------------- LOGIN UI ----------------
def login_ui():
    st.subheader("Student Login")

    with st.form("login_form"):
        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")

        submit = st.form_submit_button("🔑 Login")

        if submit:
            username = login_username.strip().lower()

            if (
                username in st.session_state["USERS"]
                and st.session_state["USERS"][username]["password"] == login_password
            ):
                st.session_state["logged_in"] = True
                st.session_state["user"] = username
                st.session_state["profile"] = st.session_state["USERS"][username]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")
