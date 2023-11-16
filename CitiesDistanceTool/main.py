import tools.City as City
import decimal
import tools.DistanceCalculator as dc

def define_coordinate(coord_type: str) -> decimal:
    coord_str = input(f'Please, enter city {coord_type}: ')
    try:
        coord_dec = decimal.Decimal(coord_str)
    except decimal.InvalidOperation as input_error:
        print(f'Invalid {coord_type}')
        print(input_error)
        return 0, 0
    else:
        return coord_dec, 1

def define_point() -> City:
    country_code = input('Please, input country code (i.e. CZE, USA, GBR): \n')
    city_name = input('Please, input city name: \n')

    city_lat = decimal.Decimal(0.0)
    city_long = decimal.Decimal(0.0)
    save_new_city = 0
    cities_list = City.City.get_city(city_name, country_code)
    if len(cities_list) == 0:
        print('The city was not found')
        lat_result = 0
        while not lat_result:
            city_lat, lat_result = define_coordinate('latitude')
        long_result = 0
        while not long_result:
            city_long, long_result = define_coordinate('longitude')
        save_new_city = 1
    else:
        city_lat = cities_list[0].get_latitude()
        city_long = cities_list[0].get_longitude()

    city = City.City(city_name, country_code, city_long, city_lat)
    if save_new_city:
        city.load_city_to_db()
    return city


if __name__ == "__main__":
    print('Define start point. ')
    start_city = define_point()

    print('Define end point. ')
    end_city = define_point()

    points_distance = dc.calculate_distance(start_city, end_city)

    print(f'Distance between cities : {points_distance}')

    geopy_points_distance = dc.calculate_geopy_distance(start_city, end_city)

    print(f'Distance between cities calculated by geopy : {geopy_points_distance}')

