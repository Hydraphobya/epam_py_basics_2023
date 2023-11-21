import pyodbc
# Tip: PEP-8 add 1 /n between imports and constants, 2 to the code start, 1 between function definition within class
CONNECTION_STR = r'DRIVER={SQLite3 ODBC Driver};'\
                 r'Direct=True;'\
                 r'Database=tools/DatabaseFiles/map.db;'\
                 r'String Types = Unicode'


class DBConnection:
    def __init__(self, connection_str: str = CONNECTION_STR) -> None:
        with pyodbc.connect(connection_str, autocommit=True) as connection:
            # Nice: good use of _ prefix 
            self._connection = connection
            with connection.cursor() as cursor:
                self._cursor = cursor
                # Tip: This should be decoupled from the __init__ as it will be run every time there is an instantion
                # you could have in the class a method create_tables(self) that uses self._cursor. Then use this method 
                # in another file for example scripts/init_db.py
                cursor.execute('create table if not exists  Cities(city_name text, country_code text, '
                               'longitude real, '
                               'latitude real, '
                               'created_datetime, '
                               'unique(country_code, city_name))')

    # Nice
    def get_cursor(self) -> pyodbc.Cursor:
        return self._cursor

# Tip: Same as said earlier, better if this file is not callable, instead is jut a module
# Make the callable in the root main.py or in scripts/
if __name__ == "__main__":
    conn_str = r'DRIVER={SQLite3 ODBC Driver};' \
                     r'Direct=True;' \
                     r'Database=DatabaseFiles/map.db;' \
                     r'String Types = Unicode'
    con = DBConnection(conn_str)
    print(type(con))
