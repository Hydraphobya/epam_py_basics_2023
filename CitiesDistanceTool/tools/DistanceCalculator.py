from CitiesDistanceTool.tools.City import City
import decimal
import math
from geopy import distance


def calculate_geopy_distance(city_start: City, city_end: City) -> decimal:
    st_point = (city_start.get_latitude(), city_start.get_longitude())
    end_point = (city_end.get_latitude(), city_end.get_longitude())
    return distance.distance(st_point, end_point).km


def calculate_distance(city_start: City, city_end: City) -> decimal:
    earth_r = 6371 # Radius of the earth in km
    st_lat = city_start.get_latitude()
    st_long = city_start.get_longitude()
    end_lat = city_end.get_latitude()
    end_long = city_end.get_longitude()
    d_lat = deg2rad(end_long - st_long)
    d_long = deg2rad(end_lat - st_lat)

    calc_helper = (math.sin(d_lat / 2) * math.sin(d_lat / 2) +
                   math.cos(deg2rad(st_lat)) * math.cos(deg2rad(end_lat)) *
                   math.sin(d_long / 2) * math.sin(d_long / 2)
                   )
    calc_helper2 = 2 * math.atan2(math.sqrt(calc_helper), math.sqrt(1 - calc_helper))
    res_distance = earth_r * calc_helper2
    return res_distance


def deg2rad(deg: decimal) -> decimal:
    return decimal.Decimal(deg) * decimal.Decimal(math.pi / 180)
