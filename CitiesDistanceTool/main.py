import tools.City as City
import decimal
import tools.DistanceCalculator as dc


def define_point() -> City:
    country_code = input('Please, input country code (i.e. CZE, USA, GBR): \n')
    city_name = input('Please, input city name: \n')
    city_postcode = input('please, input city postcode: \n')

    save_new_city = 0
    cities_list = City.City.get_city(city_name, country_code, city_postcode)
    if len(cities_list) == 0:
        city_lat = decimal.Decimal(input('The city was not found. Please, enter city latitude: '))
        city_long = decimal.Decimal(input('Please, enter city longitude: '))
        save_new_city = 1
    else:
        city_lat = cities_list[0].get_latitude()
        city_long = cities_list[0].get_longitude()

    city = City.City(city_name, country_code, city_postcode, city_long, city_lat)
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

