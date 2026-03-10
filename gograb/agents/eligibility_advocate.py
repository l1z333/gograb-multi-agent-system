class EligibilityAdvocateAgent:
    def argue(self, profile, policy):
        reasons = []
        confidence = 0.0

        if profile["age"] and profile["age"] >= policy["min_age"]:
            reasons.append("Age requirement satisfied")
            confidence += 0.3

        if profile["income"] and profile["income"] <= policy["max_income"]:
            reasons.append("Income within limit")
            confidence += 0.3

        if "income_certificate" in profile["documents"]:
            reasons.append("Required document present")
            confidence += 0.2

        return {
            "verdict": "ELIGIBLE",
            "confidence": round(confidence, 2),
            "reasons": reasons
        }
