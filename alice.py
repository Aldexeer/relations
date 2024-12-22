from characters import Character
import constants as c
import player as p

class Alice(Character):
    def __init__(self, name="Alice"):
        super().__init__(name)
        self.relationship_satisfaction = 70
        self.stress = 30
        self.energy = 100
        self.hobby = "Painting"
        self.schedule = [
            AliceActions.Work_Part_Time,  # 8 AM
            AliceActions.Work_Part_Time,  # 9 AM
            AliceActions.Work_Part_Time,  # 10 AM
            AliceActions.Work_Part_Time,  # 11 AM
            AliceActions.Pursue_Hobby,    # 12 PM
            AliceActions.Relax,           # 1 PM
            AliceActions.Relax,           # 2 PM
            AliceActions.Pursue_Hobby,    # 3 PM
            AliceActions.Relax,           # 4 PM
            AliceActions.Relax,           # 5 PM
            AliceActions.Relax,           # 6 PM
            AliceActions.Relax,           # 7 PM
            AliceActions.Relax,           # 8 PM
            AliceActions.Relax,           # 9 PM
            AliceActions.Relax,           # 10 PM
            AliceActions.Relax,           # 11 PM
            AliceActions.Relax,           # 12 AM
            AliceActions.Relax,           # 1 AM
            AliceActions.Relax,           # 2 AM
            AliceActions.Relax,           # 3 AM
            AliceActions.Relax,           # 4 AM
            AliceActions.Relax,           # 5 AM
            AliceActions.Relax,           # 6 AM
            AliceActions.Spend_Time_with_Player,  # 7 AM
        ]

class AliceActions:
    Work_Part_Time = "Work Part-time"
    Relax = "Relax"
    Pursue_Hobby = "Pursue Hobby"
    Spend_Time_with_Player = "Spend Time with Player"

def update_alice(game_logic, hours, action):
    """Updates Alice's attributes based on her schedule."""
    current_time = game_logic.current_time

    for _ in range(hours):
        alice_current_activity = game_logic.alice.schedule[current_time - 8]
        if alice_current_activity == AliceActions.Work_Part_Time:
            game_logic.alice.update_attributes({"stress": 3, "energy": -5})
        elif alice_current_activity == AliceActions.Relax:
            game_logic.alice.update_attributes({"stress": -2, "energy": 5})
        elif alice_current_activity == AliceActions.Pursue_Hobby:
            game_logic.alice.update_attributes({"stress": -4, "energy": -2})
        elif alice_current_activity == AliceActions.Spend_Time_with_Player:
            if action == p.Actions.Spend_Time_with_Player:
                game_logic.alice.relationship_satisfaction += 5

        # --- Basic Attribute Clamping for Alice ---
        if game_logic.alice.stress > 100:
            game_logic.alice.stress = 100
        if game_logic.alice.stress < 0:
            game_logic.alice.stress = 0
        if game_logic.alice.energy > 100:
            game_logic.alice.energy = 100
        if game_logic.alice.energy < 0:
            game_logic.alice.energy = 0
        if game_logic.alice.relationship_satisfaction > 100:
            game_logic.alice.relationship_satisfaction = 100
        if game_logic.alice.relationship_satisfaction < 0:
            game_logic.alice.relationship_satisfaction = 0

        current_time += 1
        if current_time > c.HOURS_IN_DAY:
            current_time = current_time - c.HOURS_IN_DAY

    # game_logic.current_time = current_time # This line is removed