import folium
import pandas as pd
import json
import codecs
import io
data=pd.read_csv("Volcanoes_USA.txt")
map=folium.Map(location=[20.5937, 78.9629],zoom_start="4.3",tiles="Mapbox Bright")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
loc=list(data["LOCATION"])
elev=list(data["ELEV"])
fg=folium.FeatureGroup(name="My Map")
for lt,ln,n,l,e in zip(lat,lon,name,loc,elev):
    if e < 1500:
        fg.add_child(folium.CircleMarker(location=[lt,ln],popup="NAME: "+n+"\nLOCATON: "+l,radius=6,fill_color="green",color="black",fill_opacity=0.7))
    elif e <3000:
        fg.add_child(folium.CircleMarker(location=[lt,ln],popup="NAME: "+n+"\nLOCATON: "+l,radius=6,fill_color="blue",color="black",fill_opacity=0.7))
    else:
        fg.add_child(folium.CircleMarker(location=[lt,ln],popup="NAME: "+n+"\nLOCATON: "+l,radius=6,fill_color="red",color="black",fill_opacity=0.7))
fg.add_child(folium.GeoJson(data=io.open("world.json",encoding = "utf-8-sig").read(),
style_function=lambda x: {'fillColor':'blue' if x['properties']
['POP2005'] < 10000000 else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("new_map1.html")