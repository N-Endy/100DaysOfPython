travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    # Initialize empty dict to hold values
    country_dict = {}

    # Populate country_dict with values
    country_dict["country"] = country
    country_dict["visits"] = visits
    country_dict["cities"] = cities

    # Append country_dict to travel_log list
    travel_log.append(country_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)