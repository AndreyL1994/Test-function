def get_population_city_country(city, country, population=''):
    """Выводит информацию о заданном городе"""
    if population:
        date = city + ' ' + country + ' ' + population
    else:
        date = city + ' ' + country
    return date.title()
