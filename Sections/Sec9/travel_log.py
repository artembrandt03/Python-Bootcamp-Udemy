country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

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
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  travel_log.append(
    {
      "country": country,
      "visits": visits,
      "cities": list_of_cities
    }
  )

"""
teacher's solution: 
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

feedback: 
- You directly use a dictionary literal as the argument to the append() method. This is concise and often considered more readable.
- You provide the function with parameters country, visits, and list_of_cities, making the function self-contained.
- Your teacher's code explicitly creates an empty dictionary new_country and then sets its keys and values before appending it to the travel_log.
The function takes parameters name, times_visited, and cities_visited, which are then used to populate the dictionary.
"""


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")