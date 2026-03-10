class EligibilitySkepticAgent:
    def argue(self, profile, policy):
        confidence = 0.0
        concerns = []

        age = profile.get("age")
        income = profile.get("income")
        documents = profile.get("documents", [])

        # ---- Hard violations (strong skepticism) ----
        if age is None or age < policy.get("min_age", 0):
            confidence += 0.5
            concerns.append("Age does not meet minimum requirement")

        if income is not None and income > policy.get("max_income", float("inf")):
            confidence += 0.4
            concerns.append("Income exceeds eligibility limit")

        if policy.get("required_documents"):
            for doc in policy["required_documents"]:
                if doc not in documents:
                    confidence += 0.3
                    concerns.append(f"Missing required document: {doc}")

        # ---- SOFT SKEPTICISM (THIS IS THE FIX) ----
        # Borderline income → not a violation, but adds uncertainty
        if income is not None:
            if 300000 < income <= 500000:
                confidence += 0.15
                concerns.append("Income is in a borderline eligibility range")

        # Cap confidence at 1.0
        confidence = min(confidence, 1.0)

        verdict = "NOT_ELIGIBLE" if confidence >= 0.5 else "UNCERTAIN"

        return {
            "verdict": verdict,
            "confidence": confidence,
            "concerns": concerns
        }
