import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca' : 34126000, 'us' : 309349000, 'mx' : 113423000, 'gr' : 276565})

wm.render_to_file('C:\\Users\\Maria\\Documents\\MyCodes\\DataVisualization\\VisualizeDownloadedData\\na_population.svg')