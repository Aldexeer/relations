class Character:
    def __init__(self, name):
        self.name = name
        self.stress = 0
        self.energy = 100
        self.emotions = {
            "happiness": 0,
            "anger": 0,
            "fear": 0,
            "sadness": 0,
            "disgust": 0,
            "surprise": 0,
            "trust": 0,
            "anticipation": 0,
            "joy": 0
        }
        self.personality = {
            "openness": 0,
            "conscientiousness": 0,
            "extraversion": 0,
            "agreeableness": 0,
            "neuroticism": 0
        }
        self.skills = {
            "cooking": 0,
            "cleaning": 0,
            "communication": 0,
            "problem_solving": 0,
            "time_management": 0,
            "stress_management": 0,
            "financial_management": 0
        }

    def update_attributes(self, changes):
        """Updates the character's attributes based on the given changes."""
        for attribute, change in changes.items():
            if attribute in ["stress", "energy", "relationship_satisfaction", "fitness"]:
                setattr(self, attribute, getattr(self, attribute) + change)

                # Basic attribute clamping
                if getattr(self, attribute) > 100:
                    setattr(self, attribute, 100)
                if getattr(self, attribute) < 0:
                    setattr(self, attribute, 0)
            elif attribute == "emotions":
                for emotion, change in changes["emotions"].items():
                    self.emotions[emotion] = max(0, min(100, self.emotions[emotion] + change))
            elif attribute == "personality":
                for personality_trait, change in changes["personality"].items():
                    self.personality[personality_trait] = max(0, min(100, self.personality[personality_trait] + change))
            elif attribute == "skills":
                for skill, change in changes["skills"].items():
                    self.skills[skill] = max(0, self.skills[skill] + change)

    def update_emotion(self, emotion, change):
        """Updates a specific emotion."""
        if emotion in self.emotions:
            self.emotions[emotion] += change
            # Clamp emotion between 0 and 100
            self.emotions[emotion] = max(0, min(100, self.emotions[emotion]))

    def update_personality(self, personality_trait, change):
        """Updates a specific personality trait."""
        if personality_trait in self.personality:
            self.personality[personality_trait] += change
            # Clamp personality trait between 0 and 100
            self.personality[personality_trait] = max(0, min(100, self.personality[personality_trait]))

    def update_skill(self, skill, change):
        """Updates a specific skill."""
        if skill in self.skills:
            self.skills[skill] += change
            # No upper limit for skills
            self.skills[skill] = max(0, self.skills[skill])