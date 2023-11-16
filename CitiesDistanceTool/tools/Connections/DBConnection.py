import pyodbc
CONNECTION_STR = r'DRIVER={SQLite3 ODBC Driver};'\
                 r'Direct=True;'\
                 r'Database=tools/DatabaseFiles/map.db;'\
                 r'String Types = Unicode'


class DBConnection:
    def __init__(self, connection_str: str = CONNECTION_STR) -> None:
        with pyodbc.connect(connection_str, autocommit=True) as connection:
            self._connection = connection
            with connection.cursor() as cursor:
                self._cursor = cursor
                cursor.execute('create table if not exists  Cities(city_name text, country_code text, '
                               'postal_code text, '
                               'longitude real, '
                               'latitude real, '
                               'created_datetime, '
                               'unique(country_code, city_name, postal_code))')

    def get_cursor(self) -> pyodbc.Cursor:
        return self._cursor


if __name__ == "__main__":
    conn_str = r'DRIVER={SQLite3 ODBC Driver};' \
                     r'Direct=True;' \
                     r'Database=DatabaseFiles/map.db;' \
                     r'String Types = Unicode'
    con = DBConnection(conn_str)
    print(type(con))
