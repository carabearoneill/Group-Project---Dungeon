"""
Group Members: lauren started; i think done? feel free to check
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINES
import interaction
import screen
# DO NOT CHANGE OR REMOVE THE PRECEDING LINES


def main():
    """
    Starting point for the whole game. Called automatically when script is run.
    """
    interaction.do_load_default_game()
    while True:
        screen.clear_screen()
        screen.draw_screen(interaction.last_message)
        interaction.last_message = ""

        user_input = interaction.get_user_command()
        should_continue = interaction.do_command(user_input)
        # TODO: If should_continue is False then exit this loop.
        if should_continue == False: # LT 
            break
    screen.write_new_line()
    screen.write('Thank you for playing. Goodbye.')


if __name__ == '__main__':
    main()
