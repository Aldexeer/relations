import constants as c
import player as p
import alice as a

class GameLogic:
    def __init__(self, game_window):
        self.game_window = game_window
        self.player = p.Player()
        self.alice = a.Alice()
        self.current_day = 1  # Start at day 1
        self.current_time = 8  # Start at 8:00 AM (in hours)

    def advance_time(self, hours, action):
        """
        Advances the in-game time based on the action taken.
        """
        print(f"Player chose to {action} for {hours} hours.")

        # --- Update Player Attributes Based on Action ---
        p.update_player(self, hours, action)

        # --- Update Alice's Attributes Based on Her Schedule ---
        a.update_alice(self, hours, action)

        self.current_time += hours # Update time after updating the attributes

        # Check for a new day
        if self.current_time >= c.HOURS_IN_DAY:
            self.current_day += 1
            self.current_time = 8  # Reset to 8:00 AM on the new day
            if self.current_time > c.HOURS_IN_DAY: # added condition
                self.current_time = self.current_time - c.HOURS_IN_DAY # added current time update