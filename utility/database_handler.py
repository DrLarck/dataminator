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

    `host` (str) : The host address.

    `port` (str) : By default `'5432'`.

    - Method :

    `reset_db_info()` : `None` - Reset the db info.
    
    `get_db_info()` : `None` - Ask for the user to give info about the database he wants to connect.

    `connection()` : `psycopg2.connection` - Represents a database session. `None` if there is no session.
    """

    # attribute
    name = ""  # the database's name
    user = ""
    password = ""
    host = ""
    port = "5432"
    connection = None

    # method
    def reset_db_info(self):
        """
        Reset the informations about the database and close the connection.

        --

        Return : `None`
        """

        self.name, self.user, self.password, self.host, self.port = "", "", "", "", "5432"

        if not self.connection is None:
            self.connection.close()
            self.connection = None
        
        return

    def get_db_info(self):
        """
        Get the connection informations.

        --

        Return : `None`
        """

        # init
        self.reset_db_info()
        clear = False
        name_ok, user_ok, password_ok, host_ok, port_ok = False, False, False, False, False

        input_name, input_user, input_host, input_port = "", "", "", ""

        while not clear:
            # ask for the db name
            if not name_ok:
                while not name_ok:
                    input_name = input("Enter the name of the database you want to connect to : ")

                    if not input_name is "":
                        name_ok = True
                    
                    else:
                        print("Please enter the name of the database you want to connect to.")
                        time.sleep(5)
            
            # ask for the db user
            if not user_ok:
                while not user_ok:
                    input_user = input(f"Enter the name of the user for the database {self.name} : ")

                    if not input_user is "":
                        user_ok = True
                    
                    else:
                        print(f"Please enter a user name for the database {self.name}.")
            
            # ask for password
            if not password_ok:
                input_password = input("Enter the password : ")
                password_ok = True
            
            # ask for the host
            if not host_ok:
                input_host = input(f"Enter the host address : ")

                host_ok = True

            # ask for the port
            if not port_ok:
                input_port = input("By default the port is '5432', leave it blank if you don't want to change it : ")

                if input_port is "":
                    input_port = "5432"
                
                port_ok = True
            
            if(name_ok == True and user_ok == True and password_ok == True and host_ok == True and port_ok == True):
                clear = True
            
        # set the info
        self.name = input_name
        self.user = input_user
        self.password = input_password
        self.host = input_host
        self.port = input_port

        return

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

        return(self.connection)