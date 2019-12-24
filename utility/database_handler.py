"""
A simple Database handler for PostgreSQL database.

--

Author : DrLarck

Last update : 24/12/19 (DrLarck)
"""

# dependancies
import psycopg2
import time

from logs.logger import Logger, Logmessage

class Database_handler:
    """
    A simple Database handler for PostgreSQL database.

    - Attribute :

    `name` (str) : The database's name.

    `user` (str) : The user name.

    `password` (str) : The required password to allow the connection to the database.

    `host` (str) : The host adress.

    `port` (str) : By default `'5432'`.

    `connection` (psycopg2.connection) : Represents a database session. `None` if there is no session.
    """

    # attribute
    name = ""  # the database's name
    user = ""
    password = ""
    host = ""
    port = "5432"
    connection = None

    # method
    def connect(self):
        """
        Create the connection to the database.

        --

        Return : `psycopg2.connection` object or `None`.
        """

        if self.connection is None:  # only work if there is no session oppened
            if not (self.name == "" and self.user == "" and self.password == "" and self.host == ""):
                
                # create the connection
                try:
                    self.connection = psycopg2.connect(
                        database = self.name,
                        user = self.user,
                        password = self.password,
                        host = self.host
                    )
                
                # could not connect the database
                except psycopg2.OperationalError as op_error:
                    op_logmsg = Logmessage()

                    op_logmsg.type_ = op_logmsg.type_[0]
                    op_logmsg.content = op_error

                    Logger().log(op_logmsg)

                    print(op_error)
                    time.sleep(5)
                
                except Exception as error:
                    error_logmsg = Logmessage()

                    error_logmsg.type_ = error_logmsg.type_[0]
                    error_logmsg.content = error

                    Logger().log(error_logmsg)

                    print(error)
                    time.sleep(5)

                # worked properly
                else:
                    confirm_message = f"New database session oppened to '{self.name}'"

                    confirm_logmsg = Logmessage()

                    confirm_logmsg.type_ = confirm_logmsg.type_[2]
                    confirm_logmsg.content = confirm_message

                    Logger().log(confirm_logmsg)

                    print(confirm_message)
                    time.sleep(5)

            else:
                no_info = "Some connection informations are missing."

                info_logmsg = Logmessage()

                info_logmsg.type_ = info_logmsg.type_[1]
                info_logmsg.content = no_info

                Logger().log(info_logmsg)

                print(no_info)
                time.sleep(5)
                
        else:
            already_connected = "A session is already oppened."

            already_logmsg = Logmessage()

            already_logmsg.type_ = already_logmsg.type_[1]
            already_logmsg.content = already_connected

            Logger().log(already_logmsg)

            print(already_connected)
            time.sleep(5)

        return