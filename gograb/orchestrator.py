from agents.user_profile_agent import UserProfileAgent
from agents.policy_reader_agent import PolicyReaderAgent
from agents.eligibility_advocate import EligibilityAdvocateAgent
from agents.eligibility_skeptic import EligibilitySkepticAgent
from agents.confidence_agent import ConfidenceEscalationAgent
from agents.database_agent import DatabaseAgent
from agents.resource_agent import ResourceAgent


class Orchestrator:
    def __init__(self):
        self.profile_agent = UserProfileAgent()
        self.policy_agent = PolicyReaderAgent()
        self.advocate_agent = EligibilityAdvocateAgent()
        self.skeptic_agent = EligibilitySkepticAgent()
        self.confidence_agent = ConfidenceEscalationAgent()
        self.db_agent = DatabaseAgent()
        self.resource_agent = ResourceAgent()

    def run(self, user_input, scheme_name, opportunity_types, username="debug_user"):

        # ---------- 1. Profile ----------
        user_profile = self.profile_agent.analyze(user_input)
        profile_data = user_profile["profile"]

        self.db_agent.save_user_profile(username, profile_data)

        # ---------- 2. Policy ----------
        policy = self.policy_agent.get_policy(scheme_name)

        # ---------- 3. Debate ----------
        advocate = self.advocate_agent.argue(profile_data, policy)
        skeptic = self.skeptic_agent.argue(profile_data, policy)

        # ---------- 4. Final decision ----------
        final = self.confidence_agent.decide(advocate, skeptic)

        self.db_agent.save_decision({
            "user": username,
            "decision": final["decision"],
            "confidence": final["confidence"]
        })

        # ---------- 5. Deliberation ----------
        deliberation_log = [
            f"UserProfileAgent: age={profile_data.get('age')}, income={profile_data.get('income')}",
            f"PolicyReaderAgent: policy loaded = {scheme_name}",
            f"AdvocateAgent: verdict={advocate['verdict']} ({int(advocate['confidence']*100)}%)",
            f"SkepticAgent: verdict={skeptic['verdict']} ({int(skeptic['confidence']*100)}%)",
            f"ConfidenceAgent: final decision={final['decision']} ({int(final['confidence']*100)}%)"
        ]

        # ---------- 6. Conditional resources ----------
        resources = {}
        if final["confidence"] >= 0.6:
            for opt in opportunity_types:
                links = self.resource_agent.get_resources(opt)
                if links:
                    resources[opt] = links

        return {
            "final": final,
            "advocate": advocate,
            "skeptic": skeptic,
            "debate": {
                "advocate": advocate,
                "skeptic": skeptic
            },
            "deliberation": deliberation_log,
            "resources": resources,
            "required_documents": policy.get("required_documents", [])
        }
