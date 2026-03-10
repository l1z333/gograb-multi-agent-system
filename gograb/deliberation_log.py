def build_log(profile, advocate, skeptic, final):
    return [
        f"UserProfileAgent: Missing info -> {profile['missing_info']}",
        f"AdvocateAgent: {advocate}",
        f"SkepticAgent: {skeptic}",
        f"FinalDecisionAgent: {final}"
    ]
