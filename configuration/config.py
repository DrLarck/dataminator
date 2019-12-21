"""
Basic configuration of the program.

--

Author : DrLarck

Last update : 21/12/19 (DrLarck)
"""

class Config:
    """
    Manages the configuragtion of the program.

    - Attribute : 

    `name` (str) : The program's name.

    `version` (dict of `int` ['major', 'medium', 'minor', 'submin']) : Represents the program's version number.
    """

    # attribute
    name = "Dataminator"
    version = {
        "major" : 1,    # very important changes
        "medium" : 0,   # feature changes
        "minor" : 0,    # minor changes
        "submin" : 4    # file changes
    }