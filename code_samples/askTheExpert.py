print("Ask the expert - Capital cities of the world")

the_world = {}


def read_from_file():
    with open('countries.txt', 'r') as text_file:
        for line in text_file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city


def write_to_file(country_name, city_name):
    with open('countries.txt', 'a') as text_file:
        text_file.write(country_name + '/' + city_name)
