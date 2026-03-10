class ConfidenceEscalationAgent:
    def decide(self, advocate, skeptic):
        net_confidence = advocate["confidence"] - skeptic["confidence"]

        if net_confidence >= 0.4:
            return {
                "decision": "ELIGIBLE",
                "confidence": round(net_confidence, 2),
                "action": "PROCEED"
            }

        if net_confidence <= -0.3:
            return {
                "decision": "NOT ELIGIBLE",
                "confidence": round(abs(net_confidence), 2),
                "action": "REJECT"
            }

        return {
            "decision": "UNCERTAIN",
            "confidence": round(abs(net_confidence), 2),
            "action": "ESCALATE",
            "message": "High uncertainty – human verification required"
        }
