import json #installing json library

in_file = open('US_fires_9_14.json', 'r') #putting file in readable format

fire_data = json.load(in_file) #creates giant dictionary named eq_data


brights,lons,lats = [],[],[]

for fire in fire_data:
    if fire['brightness'] > 450:
        bright = fire['brightness']
        brights.append(bright)
        lon = fire['longitude']
        lat = fire['latitude']
        lons.append(lon)
        lats.append(lat)

import plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'locationmode': 'USA-states',
    'marker': {
        'color': brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'},
    },
}]


my_layout = Layout(
    title='US Fires - 9/14/2020 through 9/20/2020',
    geo = dict(
        projection_scale=6,
        center=dict(lat=36.7783, lon=-117.4179)
        ),
    )
fig = {'data':data, 'layout':my_layout}



offline.plot(fig, filename='US_fires_9_14.html')