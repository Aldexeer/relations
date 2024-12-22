import arcade
import arcade.gui
import constants as c
import alice as a
import player as p
import gamelogic as gl

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

        # --- Button event handlers ---
        @work_button.event("on_click")
        def on_click_work(event):
            self.game_logic.advance_time(4, p.Actions.Work)

        @rest_button.event("on_click")
        def on_click_rest(event):
            self.game_logic.advance_time(2, p.Actions.Rest)

        @spend_time_button.event("on_click")
        def on_click_spend_time(event):
            self.game_logic.advance_time(3, p.Actions.Spend_time_with_Alice)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        self.game_logic = gl.GameLogic(self)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        self.manager.enable()

    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()

        # --- Draw the day and time ---
        time_text = f"Time: {self.game_logic.current_time:02d}:00"
        day_text = f"Day: {self.game_logic.current_day}"

        # Parameters: text, x, y, color, font size
        arcade.draw_text(day_text, 10, c.SCREEN_HEIGHT - 30, arcade.color.BLACK, 18)
        arcade.draw_text(time_text, 10, c.SCREEN_HEIGHT - 55, arcade.color.BLACK, 18)

        # --- Draw Alice's Info ---
        alice_name_text = f"Name: {self.game_logic.alice.name}"
        alice_relationship_text = f"Relationship Satisfaction: {self.game_logic.alice.relationship_satisfaction}"
        alice_stress_text = f"Stress: {self.game_logic.alice.stress}"
        alice_energy_text = f"Energy: {self.game_logic.alice.energy}"
        alice_current_activity_text = f"Current Activity: {self.game_logic.alice.schedule[self.game_logic.current_time - 8]}"

        arcade.draw_text(alice_name_text, 10, c.SCREEN_HEIGHT - 90, arcade.color.BLACK, 14)
        arcade.draw_text(alice_relationship_text, 10, c.SCREEN_HEIGHT - 115, arcade.color.BLACK, 14)
        arcade.draw_text(alice_stress_text, 10, c.SCREEN_HEIGHT - 140, arcade.color.BLACK, 14)
        arcade.draw_text(alice_energy_text, 10, c.SCREEN_HEIGHT - 165, arcade.color.BLACK, 14)
        arcade.draw_text(alice_current_activity_text, 10, c.SCREEN_HEIGHT - 190, arcade.color.BLACK, 14)

        # --- Draw Player's Info ---
        player_money_text = f"Money: ${self.game_logic.player.money}"
        player_stress_text = f"Stress: {self.game_logic.player.stress}"
        player_energy_text = f"Energy: {self.game_logic.player.energy}"
        player_job_text = f"Job: {self.game_logic.player.job}"

        arcade.draw_text(player_money_text, 310, c.SCREEN_HEIGHT - 90, arcade.color.BLACK, 14)
        arcade.draw_text(player_stress_text, 310, c.SCREEN_HEIGHT - 115, arcade.color.BLACK, 14)
        arcade.draw_text(player_energy_text, 310, c.SCREEN_HEIGHT - 140, arcade.color.BLACK, 14)
        arcade.draw_text(player_job_text, 310, c.SCREEN_HEIGHT - 165, arcade.color.BLACK, 14)

        # --- Draw Alice's Schedule ---
        schedule_text = "Alice's Schedule:"
        arcade.draw_text(schedule_text, 10, c.SCREEN_HEIGHT - 265, arcade.color.BLACK, 14)
        y_offset = 290
        for i, activity in enumerate(self.game_logic.alice.schedule):
            hour = (8 + i) % 24
            am_pm = "AM" if hour < 12 else "PM"
            hour_12 = hour % 12 if hour % 12 != 0 else 12
            activity_text = f"{hour_12:02d} {am_pm}: {activity}"
            arcade.draw_text(activity_text, 10, c.SCREEN_HEIGHT - y_offset, arcade.color.BLACK, 12)
            y_offset += 20

        # Draw the GUI
        self.manager.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        pass

    def on_key_press(self, key, modifiers):
      """ We don't need it anymore"""
      pass

def main():
    """ Main function """
    window = MyGame(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()