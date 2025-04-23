import requests 
from pprint import pprint 

API_Key = 'dj4526ccdg1563215foce451dhn1n54h5'
city = input("Enter a city: ")


# why we use pprint ? Ans: In Python, the pprint module, which stands for "pretty-print," is used to format and print Python data structures in a more visually appealing and readable way. This is especially useful for complex data types such as lists or dictionaries with nested structures.

base_url = "http://api.openweathermap.org/data/2.5/weather"+API_Key+"&q=" +city

weather_data = requests.get (base_url).json()

pprint(weather_data)