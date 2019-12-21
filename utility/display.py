"""
Utility functions for the displaying.

--

Author : DrLarck

Last update : 21/12/19 (DrLarck)
"""

# dependancies
import os

class Util_display:
    """
    Utility functions for the displaying.

    - Method :

    `clear_display()` : `None` - Clear the console.
    """

    # method
    def clear_display(self):
        """
        Clear the console's display.

        --

        Return : `None`
        """

        os.system('cls' if os.name == 'nt' else 'clear')

        return