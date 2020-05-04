# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:45:31 2020

@author: tuf97085
"""
import folium
import os
import geopandas as gpd
os.chdir('C://Users//tuf97085//Gis_Health//Final_project')

corona = 'pos_pop_full.shp'
corona_gdf = gpd.read_file(corona)

m = folium.Map(location=[40.005, -75.155338], zoom_start=11, tiles= 'OpenStreetMap', control_scale=True)

### tiles = 'Stamen Terrain'

march_31 = folium.Choropleth(
    geo_data=corona_gdf.to_json(),
    name='March 31st',
    data=corona_gdf,
    columns=['CODE', 'pos_pop'],
    key_on='feature.properties.CODE',
    fill_color='YlOrRd', #YlGn#PuBu ### https://github.com/dsc/colorbrewer-python
    fill_opacity=0.7,
    line_opacity=0.2,
    #threshold_scale=[0, 0.001, 0.003, 0.005, 0.007, 0.009, 0.011, 0.013],
    legend_name='March 31st Postive accounts of Covid19 by Zip-code population',
    highlight = True
).add_to(m)
    
march_31.geojson.add_child(
    folium.features.GeoJsonTooltip(
        fields= ['CODE' ,'Positives', 'P001001', 'pos_pop'],
        aliases = ['Zip Code:','Total Positive COVID-19 Cases for Zip Code as of March 31st:','Total Zip Code Population:', 'March 31st Positive Tests per Zip population:']))


april_21 = folium.Choropleth(
    geo_data=corona_gdf.to_json(),
    name='April 21st',
    data=corona_gdf,
    columns=['CODE', 'april_posp'],
    key_on='feature.properties.CODE',
    fill_color='YlOrRd', #YlGn#PuBu ### https://github.com/dsc/colorbrewer-python
    fill_opacity=0.7,
    line_opacity=0.2,
    #threshold_scale=[0, 0.001, 0.003, 0.005, 0.007, 0.009, 0.011, 0.013],
    legend_name='April 21st Positive accounts of Covid19 by Zip-code population',
    highlight = True,
    show = False
).add_to(m)

april_21.geojson.add_child(
    folium.features.GeoJsonTooltip(
        fields= ['CODE', 'Count','P001001','april_posp', 'increase'],
        aliases = ['Zip Code:','Total Positive COVID-19 Cases for Zip Code as of April 21st:','Total Zip Code Population:', 'April 21st Positive Tests per Zip population:', 'Increase of positive cases from March 31st to April 21st']))

folium.LayerControl().add_to(m)

## folium parameters link -> https://python-visualization.github.io/folium/modules.html#module-folium.map

m.save("choropleth.html")