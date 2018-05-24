import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")

'''
data = pd.read_json('supermarket.json')

data["completeAddress"] = data["Address"] + "," + data["City"]  + ","  + data["Country"]

from geopy.geocoders import Nominatim
'''

def color(pop):
	if pop > 2000:
		return 'red'
	elif pop > 1000:
		return 'orange'
	else:
		return 'green'

map = folium.Map(location=[38, -99], zoom_start = 6)

fg = folium.FeatureGroup(name='My group')

for lt, ln, pop in zip(data["LAT"], data["LON"], data["ELEV"]):
	fg.add_child(folium.CircleMarker(location = [lt, ln], radius=6, popup=str(pop), fill_color=color(pop), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
	style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
	else 'orange' if 10000000 <= x['properties']['POP2005'] <= 200000000 
	else 'red'}))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map.html")