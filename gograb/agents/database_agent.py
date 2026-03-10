class DatabaseAgent:
    def __init__(self):
        if "DB_AGENT_STORE" not in globals():
            globals()["DB_AGENT_STORE"] = {
                "users": {},
                "decisions": []
            }

        self.store = globals()["DB_AGENT_STORE"]

    def save_user_profile(self, username, profile):
        self.store["users"][username] = profile

    def get_user_profile(self, username):
        return self.store["users"].get(username)

    def save_decision(self, record):
        self.store["decisions"].append(record)

    def get_all_data(self):
        return self.store
