import folium
import pandas as pd
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
map.add_child(fg)
map.save("new_map.html")