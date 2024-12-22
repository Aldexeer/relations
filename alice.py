import constants as c
# --- Alice's Activities ---
class AliceActions:
    Work_Part_Time = "Work Part-time"
    Relax = "Relax"
    Pursue_Hobby = "Pursue Hobby"
    Spend_Time_with_Player = "Spend Time with Player"

# --- Alice's Data ---
alice = {
    "name": "Alice",
    "relationship_satisfaction": 70,
    "stress": 30,
    "energy": 100,
    "hobby": "Painting",  # Add a hobby
}

# --- Alice's Daily Schedule (Fixed for now) ---
alice_schedule = [
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
    AliceActions.Spend_Time_with_Player,  # 7 AM # updated
]

def update_alice(hours, action):
    """Updates Alice's attributes based on her schedule."""
    global current_time

    for _ in range(hours):
        alice_current_activity = alice_schedule[current_time - 8]
        if alice_current_activity == AliceActions.Work_Part_Time:
            alice["stress"] += 3
            alice["energy"] -= 5
        elif alice_current_activity == AliceActions.Relax:
            alice["stress"] -= 2
            alice["energy"] += 5
        elif alice_current_activity == AliceActions.Pursue_Hobby:
            alice["stress"] -= 4
            alice["energy"] -= 2
        elif alice_current_activity == AliceActions.Spend_Time_with_Player:
            alice["relationship_satisfaction"] += 5 * hours # updated

        # --- Basic Attribute Clamping for Alice ---
        if alice["stress"] > 100:
            alice["stress"] = 100
        if alice["stress"] < 0:
            alice["stress"] = 0
        if alice["energy"] > 100:
            alice["energy"] = 100
        if alice["energy"] < 0:
            alice["energy"] = 0

        current_time += 1
        if current_time > c.HOURS_IN_DAY:
            current_time = current_time - c.HOURS_IN_DAY

# --- Global Variables ---
current_day = 1  # Start at day 1
current_time = 8  # Start at 8:00 AM (in hours)