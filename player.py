import constants as c
import alice as a

# --- Player's Data ---
player = {
    "money": 0,
    "stress": 0,
    "energy": 100,
}

# --- Player's Actions ---
class Actions:
    Work = "Work"
    Rest = "Rest"
    Spend_time_with_Alice = "Spend time with Alice"

def update_player(hours, action):
    """Updates the player's attributes based on the action taken."""
    if action == Actions.Work:
        player["money"] += 15 * hours
        player["stress"] += 5 * hours
        player["energy"] -= 10 * hours
    elif action == Actions.Rest:
        player["stress"] -= 3 * hours
        player["energy"] += 8 * hours
    elif action == Actions.Spend_time_with_Alice:
        player["stress"] -= 2 * hours
        player["energy"] -= 4 * hours
        a.alice["relationship_satisfaction"] += 5 * hours # updated

    # --- Basic Attribute Clamping ---
    if player["stress"] > 100:
        player["stress"] = 100
    if player["stress"] < 0:
        player["stress"] = 0
    if player["energy"] > 100:
        player["energy"] = 100
    if player["energy"] < 0:
        player["energy"] = 0