class DeliberationAgent:
    def conduct_debate(self, advocate, skeptic):
        conversation = []

        conversation.append(
            f"Advocate: I believe the user is eligible because {', '.join(advocate['reasons'])}"
        )

        conversation.append(
            f"Skeptic: I disagree due to {', '.join(skeptic['concerns'])}"
        )

        return conversation
