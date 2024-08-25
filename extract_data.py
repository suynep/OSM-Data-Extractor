import xml.etree.ElementTree as ET

tree = ET.parse('map.xml')

root = tree.getroot()


req_keys_node = ['id', 'lat', 'lon']

nodes = []
ways = []
bound = {
    'minlat':'',
    'minlon':'',
    'maxlat':'',
    'maxlon':''
}

for child in root:
    if child.tag == 'bounds':
        for k in list(bound.keys()):
            bound[k] = child.attrib[k]

    if child.tag == 'node':
        d = dict()
        for key in req_keys_node:
            d[key] = child.attrib[key]

        nodes.append(d)
    if child.tag == 'way':
        d = dict()
        d['id'] = child.attrib['id']
        d['nodes'] = []
        for subchild in child:
            if subchild.tag == 'nd':
                d['nodes'].append(subchild.attrib['ref'])
        ways.append(d)

try:
    with open('wayData', 'x') as f:
        for way in ways:
            f.write(str(way) + '\n')

        print('wayData file written\n')
except:
    print('file already exists!!')

try:
    with open('nodeData', 'x') as f:
        for node in nodes:
            f.write(str(node) + '\n')

        print('nodeData file written\n')
except:
    print('file already exists!!')

try:
    with open('boundData', 'x') as f:
        f.write(str(bound) + '\n')
except:
    print('file already exists!!')
