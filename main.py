"""
A simple program that allows the user to do operations on the Database of its choice.

--

Author : DrLarck

Birth : 21/12/19

Last update : 21/12/19 (DrLarck)
"""

# dependancies
from configuration.config import Config
from utility.display import Util_display

class Main:
    """
    The main class of the program.

    Displays the Menu.

    - Attribute :

    `user_choice` (int) : Represent the user's choice from the `menu()`.

    - Method :

    `run()` : `None` - Launch the program.

    `menu()` : `None` - Display the menu.
    """

    # attribute
    user_choice = 0  # represent the user choice from the `menu()`

    # util
    display = Util_display()
    
    # method
    def run(self):
        """
        Launch the program.

        --

        Return : `None`
        """

        # call the menu
        self.menu()

        return
    
    def menu(self):
        """
        Display the Menu and allows the user to choose what he wants to do.

        --

        Return : `None`
        """

        # init
        stop = False
        config_ = Config()
        version = config_.version

        # text menu
        menu_display = f"Welcome to {config_.name} v{version['major']}.{version['medium']}.{version['minor']}.{version['submin']}.\n\nChoose an action :"

        while not stop:
            self.display.clear_display()
            print(menu_display)

        return

if(__name__ == "__main__"):
    Main().run()