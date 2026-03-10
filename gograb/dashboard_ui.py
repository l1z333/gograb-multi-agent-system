import streamlit as st
from orchestrator import Orchestrator


def dashboard_ui():
    if "profile" not in st.session_state:
        st.error("Session expired. Please login again.")
        return

    profile = st.session_state["profile"]

    # ================= SIDEBAR =================
    st.sidebar.title("😄 Your Profile")

    # ---- Education Level ----
    education_level = st.sidebar.selectbox(
        "Education Level",
        ["School", "Undergraduate", "Postgraduate"]
    )

    # ---- Age (CRITICAL for confidence) ----
    age = st.sidebar.number_input(
        "Age",
        min_value=10,
        max_value=60,
        value=21
    )

    # ---- Conditional academic fields ----
    if education_level == "School":
        class_level = st.sidebar.selectbox(
            "Class",
            ["8", "9", "10", "11", "12"]
        )
        year = None
        semester = None

    else:
        class_level = None
        year = st.sidebar.selectbox(
            "Year of Study",
            ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        )

        semester = st.sidebar.selectbox(
            "Semester",
            ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]
        )

    branch = st.sidebar.selectbox(
        "Branch / Stream",
        [
            "CYS", "CSE", "AIE", "ECE", "ME", "CE", "EE", "IT",
            "BA", "BSc", "BCom", "Arts", "Science", "Commerce", "Others"
        ]
    )

    state = st.sidebar.text_input("State", "Kerala")

    # ---- Financial Info ----
    income_label = st.sidebar.selectbox(
        "Annual Family Income",
        [
            "< ₹1 Lakh",
            "₹1–3 Lakh",
            "₹3–5 Lakh",
            "₹5–8 Lakh",
            "> ₹8 Lakh"
        ]
    )

    need_aid = st.sidebar.checkbox("Applying for financial aid")

    income_map = {
        "< ₹1 Lakh": 100000,
        "₹1–3 Lakh": 300000,
        "₹3–5 Lakh": 500000,
        "₹5–8 Lakh": 800000,
        "> ₹8 Lakh": None
    }

    income = income_map[income_label]

    # ================= HEADER =================
    st.title("🤖 GoGrab")
    st.caption(f"👋 {profile['name']} from {profile['college']}")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state.pop("user", None)
        st.session_state.pop("profile", None)
        st.rerun()

    # ================= OPPORTUNITIES =================
    st.subheader("🎯 Select opportunities")

    types = st.multiselect(
        "Choose what you are looking for",
        [
            "internship",
            "scholarship",
            "fellowship",
            "government_scheme",
            "research_grant",
            "entrance_exam",
            "students_discounts"
        ]
    )

    # ================= RUN AGENTS =================
    if st.button("Run Multi-Agent Analysis"):
        orchestrator = Orchestrator()

        user_input = {
            "education_level": education_level,
            "class": class_level,
            "year": year,
            "semester": semester,
            "branch": branch,
            "state": state,
            "age": age,                 # 🔥 FIXES CONFIDENCE
            "income": income,
            "documents": ["income_certificate"] if need_aid else []
        }

        result = orchestrator.run(
            user_input=user_input,
            scheme_name="student_scheme",
            opportunity_types=types
        )

        st.success("Multi-Agent Analysis Complete")

        # ================= CONFIDENCE =================
        st.metric(
            "Final Confidence",
            f"{int(result['final']['confidence'] * 100)}%"
        )

        # ================= RESOURCES =================
        st.subheader("📌 Opportunities Based on Your Selection")

        resources = result.get("resources", {})

        if not resources:
            st.warning("No official resources found.")
        else:
            for category, links in resources.items():
                st.markdown(f"### {category.replace('_', ' ').title()}")
                for link in links:
                    if isinstance(link, str) and link.startswith("http"):
                        st.markdown(f"- [{link}]({link})")
                    else:
                        st.markdown(f"- {link}")

        # ================= DELIBERATION =================
        with st.expander("🧠 Agent Deliberation"):
            for step in result.get("deliberation", []):
                st.write("•", step)

        # ================= DEBATE =================
        with st.expander("🗣️ Agent Debate"):
            st.write("### Advocate")
            st.write(f"Confidence: {int(result['advocate']['confidence'] * 100)}%")
            for r in result['advocate'].get("reasons", []):
                st.write("-", r)

            st.write("### Skeptic")
            st.write(f"Confidence: {int(result['skeptic']['confidence'] * 100)}%")
            for c in result['skeptic'].get("concerns", []):
                st.write("-", c)
