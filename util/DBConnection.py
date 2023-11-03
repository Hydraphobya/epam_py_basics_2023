import pyodbc
CONNECTION_STR = 'DRIVER={SQLite3 ODBC Driver};'\
                 'Direct=True;'\
                 'Database=util/PubTypes.db;'\
                 'String Types = Unicode'


class DBConnection:
    def __init__(self, connection_str: str = CONNECTION_STR) -> None:
        with pyodbc.connect(connection_str, autocommit=True) as connection:
            self._connection = connection
            with connection.cursor() as cursor:
                self._cursor = cursor

    def get_cursor(self) -> pyodbc.Cursor:
        return self._cursor
