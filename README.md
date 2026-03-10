# GoGrab : Multi-Agent Opportunity Discovery System

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

## 📁 Project Structure

```
gograb-multi-agent-system/
│
├── student_app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── confidence_agent.py
│   │   ├── database_agent.py
│   │   ├── deliberation_agent.py
│   │   ├── eligibility_advocate.py
│   │   ├── eligibility_skeptic.py
│   │   ├── policy_reader_agent.py
│   │   ├── resource_agent.py
│   │   └── user_profile_agent.py
│   │
│   ├── auth_ui.py
│   ├── dashboard_ui.py
│   ├── deliberation_log.py
│   ├── orchestrator.py
│   ├── streamlit_app.py
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/l1z333/gograb-multi-agent-system.git
```

Navigate to the project directory:

```
cd gograb-multi-agent-system/student_app
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```
streamlit run streamlit_app.py
```

After running this command, Streamlit will start a local server and display something similar to:

```
Local URL: http://localhost:8501
```

Open that URL in your browser to access the **GoGrab dashboard**.

---

## 🧪 Example Workflow

1. Create an account or log in using the authentication UI.
2. Enter your academic and financial details.
3. Select opportunity types (scholarships, internships, fellowships, etc.).
4. Run the multi-agent analysis.
5. View eligibility decisions and recommended opportunities.

---

## 📌 Future Improvements

* Integrate real government policy APIs
* Add LLM-based reasoning agents
* Implement persistent database storage
* Improve the explainability and transparency of agent decisions
* Add automated testing for agents
