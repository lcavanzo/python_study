#Database context manager

import mysql.connector

class ConnError(Exception):
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDatabase:

    def __init__(self, config:dict) -> None:
        self.config = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.ProgrammingError as err:
            raise CredentialsError(err)
        except mysql.connector.errors.DatabaseError as err:
            raise ConnError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)
        
