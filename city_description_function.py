def get_population_city_country(city, country, population=''):
    if population:
        date = city + ' ' + country + ' ' + population
    else:
        date = city + ' ' + country
    return date.title()
