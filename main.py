import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Relationship Simulator"

# --- Game Variables (We'll add more later) ---
current_day = 1  # Start at day 1
current_time = "8:00"  # Start at 8:00 AM (We'll format this better later)

# --- Alice's Data (Simplified for now) ---
alice = {
    "name": "Alice",
    "relationship_satisfaction": 70,
    "stress": 30,
}

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

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # --- Draw the day and time ---
        day_text = f"Day: {current_day}"
        time_text = f"Time: {current_time}"

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

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        pass  # We'll add time updates and other logic later

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()