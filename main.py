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

# --- Alice's Data (Simplified for now) ---
alice = {
    "name": "Alice",
    "relationship_satisfaction": 70,
    "stress": 30,
}

# --- Player's Actions ---
class Actions:
    Work = "Work"
    Rest = "Rest"
    Spend_time_with_Alice = "Spend time with Alice"

class MyGame(arcade.Window):
    """
    Main application class.
    """

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
        current_time += hours

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