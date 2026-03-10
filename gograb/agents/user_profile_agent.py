class UserProfileAgent:
    def analyze(self, user_input):
        profile = {
            "age": int(user_input.get("age")) if user_input.get("age") else None,
            "income": int(user_input.get("income")) if user_input.get("income") else None,
            "documents": user_input.get("documents", [])
        }

        missing = [k for k, v in profile.items() if v is None]

        return {
            "profile": profile,
            "missing_info": missing
        }
