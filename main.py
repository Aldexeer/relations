import arcade
import time

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Relationship Simulator"
SECONDS_IN_HOUR = 1 # Game time will pass this amount of real time seconds
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR # Placeholder, seconds in 1 day for testing purposes

# --- Game Variables (We'll add more later) ---
current_day = 1  # Start at day 1
current_time = 8 * SECONDS_IN_HOUR  # Start at 8:00 AM (in seconds for simplicity)
last_time_update = 0

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
        global last_time_update
        # Initialize your variables here
        last_time_update = time.time()
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # --- Draw the day and time ---
        # Convert time back to hours and minutes for display
        hours = current_time // SECONDS_IN_HOUR
        minutes = (current_time % SECONDS_IN_HOUR) * 60 // SECONDS_IN_HOUR
        time_text = f"Time: {hours:02d}:{minutes:02d}"

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

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        global current_time, current_day, last_time_update

        # Get the current real-world time
        current_real_time = time.time()

        # Check if one second has passed in real time
        if current_real_time - last_time_update >= 1:
            current_time += SECONDS_IN_HOUR
            last_time_update = current_real_time

            # Check for a new day
            if current_time >= SECONDS_IN_DAY:
                current_day += 1
                current_time = 8 * SECONDS_IN_HOUR # Reset to 8:00 AM on the new day

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()