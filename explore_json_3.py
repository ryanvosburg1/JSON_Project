import json #installing json library

in_file = open('eq_data_30_day_m1.json', 'r') #putting file in readable format

out_file = open('readable_eq_data.json', 'w')

eq_data = json.load(in_file) #creates giant dictionary named eq_data

json.dump(eq_data, out_file,indent=4) #4 bc dictionary goes 4 deep to get to magnitude, coordinates
#key 1: type, key 2: metadata, 3: features-with a list of dictionaries
#take native json file, load into eq data, 
# #then this step dumps data loaded into out file

list_of_eqs = eq_data['features']
    #get list of all earthquakes, new one starts at type:feature
    #keys are type, metadata, features
print(len(list_of_eqs)) #finds number of eq's, 158

#create lists for latitudes, longitudes, and magnitude to plot

mags,lons,lats, hover_texts = [],[],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    title = eq['properties']['title']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)


'''print("Mags")
print(mags[:10])'''

import plotly
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#basic layout #data = [Scattergeo(lon=lons, lat=lats)] #lon and lat needed for scattergeo to plot

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        #list comprehension, easy way to make list
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'} #for each magnitude in list of magnitudes
    },
}]


my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')


