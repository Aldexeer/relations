from characters import Character
import constants as c
import alice as a

class Player(Character):
    def __init__(self, name="Player"):
        super().__init__(name)
        self.money = 0
        self.job = ""
        self.relationship = {
            "Alice": 0
        }
        self.skills = {
            "programming": 0,
            "game_design": 0,
            "web_development": 0
        }
        self.fitness = 0

    def update_relationship(self, character_name, change):
        if character_name in self.relationship:
            self.relationship[character_name] += change

            # Clamp relationship value
            if self.relationship[character_name] > 100:
                self.relationship[character_name] = 100
            if self.relationship[character_name] < -100:
                self.relationship[character_name] = -100

class Actions:
    Work = "Work"
    Rest = "Rest"
    Spend_time_with_Alice = "Spend time with Alice"
    Study = "Study"
    Go_to_the_Gym = "Go to the Gym"
    Socialize = "Socialize"
    Part_time_Job = "Part-time Job"

def update_player(game_logic, hours, action):
    """Updates the player's attributes based on the action taken."""
    player = game_logic.player
    if action == Actions.Work:
        player.update_attributes({"money": 15 * hours, "stress": 5 * hours, "energy": -10 * hours, "skills": {"programming": 1, "game_design": 1}})
        if player.job == "":
            player.job = "Programmer" # temporary
    elif action == Actions.Rest:
        player.update_attributes({"stress": -3 * hours, "energy": 8 * hours})
    elif action == Actions.Spend_time_with_Alice:
        player.update_attributes({"stress": -2 * hours, "energy": -4 * hours})
        game_logic.player.update_relationship("Alice", 5 * hours)
        game_logic.alice.relationship_satisfaction += 5 * hours
    elif action == Actions.Study:
        player.update_attributes({"stress": 3 * hours, "energy": -5 * hours, "skills": {"programming": 1, "game_design": 1, "web_development": 1}})
    elif action == Actions.Go_to_the_Gym:
        player.update_attributes({"stress": -4 * hours, "energy": -6 * hours, "fitness": 2 * hours})
    elif action == Actions.Socialize:
        player.update_attributes({"stress": -4 * hours, "energy": -4 * hours, "money": -5 * hours, "emotions": {"happiness": 3}})
    elif action == Actions.Part_time_Job:
        player.update_attributes({"money": 10 * hours, "stress": 3 * hours, "energy": -6 * hours})

    # --- Basic Attribute Clamping ---
    if player.stress > 100:
        player.stress = 100
    if player.stress < 0:
        player.stress = 0
    if player.energy > 100:
        player.energy = 100
    if player.energy < 0:
        player.energy = 0
    if player.fitness > 100:
        player.fitness = 100
    if player.fitness < 0:
        player.fitness = 0