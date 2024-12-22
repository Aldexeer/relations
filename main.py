import arcade
import arcade.gui

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Relationship Simulator"
HOURS_IN_DAY = 24

# --- Game Variables ---
current_day = 1  # Start at day 1
current_time = 8  # Start at 8:00 AM (in hours)

# --- Alice's Data ---
alice = {
    "name": "Alice",
    "relationship_satisfaction": 70,
    "stress": 30,
    "energy": 100,
    "hobby": "Painting",  # Add a hobby
}

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

# --- Alice's Activities ---
class AliceActions:
    Work_Part_Time = "Work Part-time"
    Relax = "Relax"
    Pursue_Hobby = "Pursue Hobby"
    Spend_Time_with_Player = "Spend Time with Player"

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
    AliceActions.Relax,           # 7 AM
]

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        work_button = arcade.gui.UIFlatButton(text="Work (4h)", width=200)
        self.v_box.add(work_button.with_space_around(bottom=20))

        rest_button = arcade.gui.UIFlatButton(text="Rest (2h)", width=200)
        self.v_box.add(rest_button.with_space_around(bottom=20))

        spend_time_button = arcade.gui.UIFlatButton(text="Spend Time with Alice (3h)", width=200)
        self.v_box.add(spend_time_button.with_space_around(bottom=20))

        # --- পৃথক ইভেন্ট হ্যান্ডলারের সাথে বোতামগুলিকে সংযুক্ত করুন
        @work_button.event("on_click")
        def on_click_work(event):
            self.advance_time(4, Actions.Work)

        @rest_button.event("on_click")
        def on_click_rest(event):
            self.advance_time(2, Actions.Rest)

        @spend_time_button.event("on_click")
        def on_click_spend_time(event):
            self.advance_time(3, Actions.Spend_time_with_Alice)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.manager.enable()
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # --- Draw the day and time ---
        time_text = f"Time: {current_time:02d}:00"
        day_text = f"Day: {current_day}"

        # Parameters: text, x, y, color, font size
        arcade.draw_text(day_text, 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 18)
        arcade.draw_text(time_text, 10, SCREEN_HEIGHT - 55, arcade.color.BLACK, 18)

        # --- Draw Alice's Info ---
        alice_name_text = f"Name: {alice['name']}"
        alice_relationship_text = f"Relationship Satisfaction: {alice['relationship_satisfaction']}"
        alice_stress_text = f"Stress: {alice['stress']}"

        arcade.draw_text(alice_name_text, 10, SCREEN_HEIGHT - 90, arcade.color.BLACK, 14)
        arcade.draw_text(alice_relationship_text, 10, SCREEN_HEIGHT - 115, arcade.color.BLACK, 14)
        arcade.draw_text(alice_stress_text, 10, SCREEN_HEIGHT - 140, arcade.color.BLACK, 14)

        # --- Draw Player's Info ---
        player_money_text = f"Money: ${player['money']}"
        player_stress_text = f"Stress: {player['stress']}"
        player_energy_text = f"Energy: {player['energy']}"

        arcade.draw_text(player_money_text, 10, SCREEN_HEIGHT - 165, arcade.color.BLACK, 14)
        arcade.draw_text(player_stress_text, 10, SCREEN_HEIGHT - 190, arcade.color.BLACK, 14)
        arcade.draw_text(player_energy_text, 10, SCREEN_HEIGHT - 215, arcade.color.BLACK, 14)

        # --- Draw Alice's Schedule ---
        schedule_text = "Alice's Schedule:"
        arcade.draw_text(schedule_text, 10, SCREEN_HEIGHT - 240, arcade.color.BLACK, 14)
        y_offset = 265
        for i, activity in enumerate(alice_schedule):
            hour = (8 + i) % 24  # Calculate the hour (8 AM + i)
            am_pm = "AM" if hour < 12 else "PM"
            hour_12 = hour % 12 if hour % 12 != 0 else 12  # Convert to 12-hour format
            activity_text = f"{hour_12} {am_pm}: {activity}"
            arcade.draw_text(activity_text, 10, SCREEN_HEIGHT - y_offset, arcade.color.BLACK, 12)
            y_offset += 20

        # Draw the GUI
        self.manager.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        pass

    def advance_time(self, hours, action):
        """
        Advances the in-game time based on the action taken.
        """
        global current_time, current_day
        print(f"Player chose to {action} for {hours} hours.")

        # --- Update Player Attributes Based on Action ---
        if action == Actions.Work:
            player["money"] += 15 * hours  # Earn $15 per hour worked
            player["stress"] += 5 * hours  # Increase stress
            player["energy"] -= 10 * hours # Decrease energy
        elif action == Actions.Rest:
            player["stress"] -= 3 * hours  # Decrease stress
            player["energy"] += 8 * hours  # Increase energy
        elif action == Actions.Spend_time_with_Alice:
            alice["relationship_satisfaction"] += 5 * hours
            player["stress"] -= 2 * hours # Decrease stress (spending time with Alice is relaxing)
            player["energy"] -= 4 * hours

        # --- Basic Attribute Clamping ---
        if player["stress"] > 100:
            player["stress"] = 100
        if player["stress"] < 0:
            player["stress"] = 0
        if player["energy"] > 100:
            player["energy"] = 100
        if player["energy"] < 0:
            player["energy"] = 0

        # --- Update Alice's Attributes Based on Her Schedule ---
        for _ in range(hours):
          alice_current_activity = alice_schedule[current_time]
          if alice_current_activity == AliceActions.Work_Part_Time:
              alice["stress"] += 3  # Working part-time increases stress
              alice["energy"] -= 5 # Decrease energy
          elif alice_current_activity == AliceActions.Relax:
              alice["stress"] -= 2  # Relaxing decreases stress
              alice["energy"] += 5  # Increase energy
          elif alice_current_activity == AliceActions.Pursue_Hobby:
              alice["stress"] -= 4  # Pursuing a hobby is relaxing
              alice["energy"] -= 2 # Decrease energy
          elif alice_current_activity == AliceActions.Spend_Time_with_Player:
              pass  # We already handle this in the player's actions

          # --- Basic Attribute Clamping for Alice ---
          if alice["stress"] > 100:
              alice["stress"] = 100
          if alice["stress"] < 0:
              alice["stress"] = 0
          if alice["energy"] > 100:
              alice["energy"] = 100
          if alice["energy"] < 0:
              alice["energy"] = 0

          # --- Advance Time ---
          current_time += 1
          # Check for a new day
          if current_time >= HOURS_IN_DAY:
              current_day += 1
              current_time = 8  # Reset to 8:00 AM on the new day

    def on_key_press(self, key, modifiers):
      """ We don't need it anymore"""
      pass

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()