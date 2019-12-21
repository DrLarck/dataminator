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
        "major" : 1,
        "medium" : 0,
        "minor" : 0,
        "submin" : 0
    }