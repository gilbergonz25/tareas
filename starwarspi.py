import requests


response = requests.get('https://swapi.dev/api/planets/?page=2')
if response.ok:
    planet_data = response.json()
    number_of_films = sum([len(planet['films']) for planet in planet_data['results']])
    print(f"En {number_of_films} películas aparecen planetas cuyo clima es árido.")
else:
    print("xa, no sirvio el API")

# el api funciona, pero no me trae lo que busco
response = requests.get('https://swapi.dev/api/films/3/')
if response.ok:
    film_data = response.json()
    number_of_wookies = sum([1 for character in film_data['characters'] if 'wookie' in requests.get(character).json()['species']])
    print(f"En la sexta película aparecen {number_of_wookies} Wookies.")
else:
    print("xa, no sirvio el API.")


response = requests.get('https://swapi.dev/api/vehicles/')
if response.ok:
    largest_vehicle = max(response.json()['results'], key=lambda vehicle: vehicle['length'])
    print(f"La nave más grande en toda la saga es el {largest_vehicle['name']}.")
else:
    print("xa no sirvio el API.")
