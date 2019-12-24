"""
A simple logger.

--

Author : DrLarck

Last update : 24/12/19 (DrLarck)
"""

# dependancies
import time

class Logger:
    """
    A simple logger.

    - Method :

    `log(message)` (logmessage) : `None` - Write the content of the logmessage in the log file.

    `get_message_type(message)` (logmessage) : `str` - Get the str type of the log message.
    """

    # method
    def log(self, message):
        """
        Write a message in the log file.

        - Parameter : 

        `message` (logmessage) : The message to write in the file.
        """

        # init
        message_type = self.get_message_type(message)
        logfile = open("logs/log.txt", "a")

        log = f"{message_type}{time.strftime('%d/%m/%y %H:%M', time.gmtime())} - {message.content}\n"
        
        logfile.write(log)
        logfile.close()

        return
    
    def get_message_type(self, message):
        """
        Get the message type.

        - Parameter : 

        `message` (logmessage) : The log message.

        --

        Return : `str`
        """

        # init
        message_type = "[INFO] "

        # get the message type
        if(message.type_.lower() == "bug"):
            message_type = "[BUG] "
        
        elif(message.type_.lower() == "warning"):
            message_type = "[WARNING] "
        
        elif(message.type_.lower() == "information"):
            message_type = "[INFO] "

        return(message_type)

class Logmessage:
    """
    Represents a message to write in the log file.

    - Attribute :

    `type_` (list) : Represents the message type : [0, bug][1, warning][2, information].

    `content` (str) : Represents the message content.
    """

    # attribute
    def __init__(self):
        self.type_ = ["bug", "warning", "information"]
        self.content = ""