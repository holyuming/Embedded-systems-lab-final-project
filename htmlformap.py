from config import mykey

import openrouteservice
from openrouteservice import convert
import folium
import json
import os

from coordinates import coord


def htmlformap(org, dst):

    client = openrouteservice.Client(key=mykey)

    coords = ((coord[org][1], coord[org][0]),(coord[dst][1], coord[dst][0]))
    res = client.directions(coords)
    geometry = client.directions(coords)['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
    duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"

    m = folium.Map(location=[24.78666, 120.99694],zoom_start=16, control_scale=True) # tiles="cartodbpositron"
    folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)

    folium.Marker(
        location=list(coords[0][::-1]),
        popup=org,
        icon=folium.Icon(color="green"),
    ).add_to(m)

    folium.Marker(
        location=list(coords[1][::-1]),
        popup=dst,
        icon=folium.Icon(color="red"),
    ).add_to(m)

    dir = "route/"

    path = os.path.join(dir, org + "_" + dst + ".html")

    m.save(path)

if __name__ == "__main__":
    # htmlformap("northdoor", "dorm10")
    dir = "route/"
    path = os.path.join(dir, "north"+"_2_"+"dorm7"".html")
    print(path)