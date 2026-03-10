class PolicyReaderAgent:
    def get_policy(self, scheme_name):
        # Hardcoded for demo; can scale later
        return {
            "min_age": 18,
            "max_income": 200000,
            "required_documents": ["income_certificate"]
        }
