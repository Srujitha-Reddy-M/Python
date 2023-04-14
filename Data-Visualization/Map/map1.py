import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")
lat=list(df.LAT)
lon=list(df.LON)
name = list(df.NAME)
el=list(df.ELEV)

def marker_color(e):
    if e<1000:
        return "blue"
    elif 1000 <= e < 2000:
        return "orange"
    else:
        return "red"

map= folium.Map(location=[37.4316, -78.6569], zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, n, e in zip(lat, lon, name, el):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius=6,popup=n+ " Volcano "+ str(e)+"m", color='grey', fill_color=marker_color(e), fill_opacity = 0.7))

fgpop = folium.FeatureGroup(name="Population")
fgpop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'pink' if 10000000 <= x['properties']['POP2005']< 20000000 else 'purple'}))

map.add_child(fgv)
map.add_child(fgpop)
map.add_child(folium.LayerControl())
map.save("MapMake.html")
