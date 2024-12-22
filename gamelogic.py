import constants as c
import arcade
import arcade.gui
import player as p
import alice as a

class GameLogic:
    def __init__(self, game_window):
        self.game_window = game_window

    def advance_time(self, hours, action):
        """
        Advances the in-game time based on the action taken.
        """
        print(f"Player chose to {action} for {hours} hours.")

        # --- Update Player Attributes Based on Action ---
        p.update_player(hours, action)

        # --- Update Alice's Attributes Based on Her Schedule ---
        a.update_alice(hours, action) # Added action

        # Check for a new day
        if a.current_time >= c.HOURS_IN_DAY:
            a.current_day += 1
            a.current_time = 8  # Reset to 8:00 AM on the new day