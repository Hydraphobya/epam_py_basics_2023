from CitiesDistanceTool.tools.Connections.DBConnection import DBConnection
from datetime import datetime
import decimal

# Tip: Class Name sould be defined as ThisIsAClass. However, python file should be this_is_a_class.py, same as modules
# Nice: great use of decorators, private/public, staticmethod, etc.
class City:
    def __init__(self, city_name: str,
                 country_code: str,
                 longitude: decimal,
                 latitude: decimal) -> None:
        self._city_name = city_name
        self._country_code = country_code
        self._longitude = longitude
        self._latitude = latitude

    def get_longitude(self) -> decimal:
        return self._longitude

    def get_latitude(self) -> decimal:
        return self._latitude

    def load_city_to_db(self):
        connection = DBConnection()
        cursor = connection.get_cursor()
        query_str = (f'insert into Cities(city_name, country_code, latitude, longitude, created_datetime) '
                     f'values("{self._city_name}", '
                     f'"{self._country_code}", '
                     f'{self._latitude}, '
                     f'{self._longitude}, '
                     f'"{datetime.now()}") ')
        cursor.execute(query_str)

    @staticmethod
    def get_city(city_name: str, country_code: str = '') -> list:
        connection = DBConnection()
        cursor = connection.get_cursor()
        query_str = (f'select * from Cities where ' +
                     f'city_name = "{city_name}"' +
                     f' and country_code = "{country_code}"' if len(country_code) > 0 else '')
        query_result = cursor.execute(query_str).fetchall()
        result_list = []
        for city_db in query_result:
            city = City(city_db.city_name,
                        city_db.country_code,
                        city_db.longitude,
                        city_db.latitude)
            result_list.append(city)
        return result_list
