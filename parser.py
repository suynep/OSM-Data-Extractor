# Purpose: To parse the lat/lon filled data into something that's workable with
# i.e. convert lat/lon data into screen resolution w/ proper scaling?

import math
from pprint import pprint

with open('boundData', 'r') as f:
    global bounds
    bounds = f.readline()
    bounds = eval(bounds.strip())

with open('nodeData', 'r') as f:
    global nodes
    nodes = []
    dummy = f.readlines()
    for d in dummy:
        d = eval(d.strip())
        nodes.append(d)

with open('wayData', 'r') as f:
    global ways
    ways = []
    dummy = f.readlines()
    for d in dummy:
        d = eval(d.strip())
        ways.append(d)

minlat = float(bounds['minlat'])
minlon = float(bounds['minlon'])
maxlat = float(bounds['maxlat'])
maxlon = float(bounds['maxlon'])

def convert_to_xy(lat, lon):
    rad = 6371
    x = rad * lon * math.cos((minlat + maxlat) / 2)
    y = rad * lat
    return x, y

# for i in range(len(nodes)):
#     lat = float(nodes[i]['lat']) - minlat
#     lon = float(nodes[i]['lon']) - minlon
#     x, y = convert_to_xy(lat, lon)
#     nodes[i]['lon'] = x
#     nodes[i]['lat'] = y
