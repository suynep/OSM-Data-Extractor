import pygame
import sys
from pprint import pprint
from parser import nodes, ways, minlat, maxlat, minlon, maxlon


pygame.init()

WIDTH, HEIGHT = 1000, 800
BACKGROUND = (50, 50, 50)
FOREGROUND = (255, 255, 255)
LINE = (255, 0, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Map")

running = True

# print(nodes, ways, minlat, maxlat, minlon, maxlon)
# map_vals(ip_start, ip_end, op_start, op_end, ip)

def map_vals(ip_start, ip_end, op_start, op_end, ip):
    slope = (op_end - op_start) / (ip_end - ip_start)
    return op_start + slope * (ip - ip_start)

outNodesCount = 0
for node in nodes:
    node['lat'] = float(node['lat'])
    node['lon'] = float(node['lon'])
    # below is done just to check for nodes that are out of range of the bounding box (contingent on OSM data?)
    if node['lat'] < minlat or node['lat'] > maxlat or node['lon'] < minlon or node['lon'] > maxlon:
        outNodesCount += 1
    node['lat'] = map_vals(minlat, maxlat, HEIGHT, 0, float(node['lat']))
    node['lon'] = map_vals(minlon, maxlon, 0, WIDTH, float(node['lon']))

# print(outNodesCount)
pprint(nodes)

def draw_lines_between_nodes(arr):
    coords = []
    for id in arr:
        for node in nodes:
            if node['id'] == id:
                coords.append((node['lon'], node['lat']))
                break

    pygame.draw.lines(screen, LINE, False, coords)


# print(ways)

def draw_node(x, y):
    pygame.draw.circle(screen, FOREGROUND, (x, y), 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND)
    for node in nodes:
        draw_node(node['lon'], node['lat'])
    for way in ways:
        draw_lines_between_nodes(way['nodes'])

    pygame.display.flip()
