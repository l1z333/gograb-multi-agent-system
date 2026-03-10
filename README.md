# GoGrab — Multi-Agent Opportunity Discovery System

GoGrab is a multi-agent AI system designed to help students discover relevant scholarships, internships, fellowships, and government schemes based on their eligibility.

The system uses a **debate-based reasoning architecture**, where multiple agents analyze user data, interpret policy constraints, and collaboratively determine eligibility with a confidence score.

---

## 🚀 Features

* Multi-agent AI architecture
* Policy-based eligibility analysis
* Debate-based reasoning between agents
* Confidence-based decision system
* Opportunity discovery and recommendations
* Interactive Streamlit dashboard

---

## 🧠 System Architecture

The system is composed of multiple specialized agents coordinated by an **orchestrator**.

### Core Agents

* **UserProfileAgent** – extracts structured information from user input
* **PolicyReaderAgent** – retrieves eligibility rules for schemes
* **EligibilityAdvocateAgent** – argues why the user qualifies
* **EligibilitySkepticAgent** – challenges eligibility by identifying violations
* **ConfidenceEscalationAgent** – determines the final decision
* **DatabaseAgent** – stores user profiles and decisions
* **ResourceAgent** – recommends relevant opportunities

---
## Project Structure

gograb-multi-agent-system
│
├── agents/
│   ├── user_profile_agent.py
│   ├── policy_reader_agent.py
│   ├── eligibility_advocate.py
│   ├── eligibility_skeptic.py
│   ├── confidence_agent.py
│   ├── resource_agent.py
│   └── database_agent.py
│
├── orchestrator.py
├── streamlit_app.py
├── dashboard_ui.py
├── auth_ui.py
├── requirements.txt
└── README.md

## 🔄 System Flow

User Input
→ Profile Extraction
→ Policy Evaluation
→ Agent Debate
→ Confidence Decision
→ Opportunity Recommendations

---

## 🛠 Tech Stack

* Python
* Streamlit
* Multi-Agent Architecture
* Rule-based reasoning

---

## ▶️ Running the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run streamlit_app.py

---

## 📌 Future Improvements

* Integrate real government policy APIs
* Add LLM-based reasoning agents
* Implement persistent database storage
* Improve explainability of agent decisions
