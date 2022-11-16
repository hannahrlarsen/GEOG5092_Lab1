import geopandas as gpd
import pandas as pd

path = '/Users/hannahlarsen/Desktop/UC Denver/FA 2022/Python and GIS/Lab1_data/lab1.gpkg'

soil_co001 = gpd.read_file(path, layer=0)
soil_co618 = gpd.read_file(path, layer=1)
soil_co641 = gpd.read_file(path, layer=2)
soil_co642 = gpd.read_file(path, layer=3)
soil_co643 = gpd.read_file(path, layer=4)
soil_co644 = gpd.read_file(path, layer=5)
soil_co645 = gpd.read_file(path, layer=6)
soil_co651 = gpd.read_file(path, layer=7)
soil_co653 = gpd.read_file(path, layer=8)
watershed = gpd.read_file(path, layer=9)
table_co001 = gpd.read_file(path, layer=10)
table_co618 = gpd.read_file(path, layer=11)
table_co641 = gpd.read_file(path, layer=12)
table_co642 = gpd.read_file(path, layer=13)
table_co643 = gpd.read_file(path, layer=14)
table_co644 = gpd.read_file(path, layer=15)
table_co645 = gpd.read_file(path, layer=16)
table_co651 = gpd.read_file(path, layer=17)
table_co653 = gpd.read_file(path, layer=18)

co001 = soil_co001.merge(table_co001, left_on='MUSYM', right_on='musym')
co618 = soil_co618.merge(table_co618, left_on='MUSYM', right_on='musym')
co641 = soil_co641.merge(table_co641, left_on='MUSYM', right_on='musym')
co642 = soil_co642.merge(table_co642, left_on='MUSYM', right_on='musym')
co643 = soil_co643.merge(table_co643, left_on='MUSYM', right_on='musym')
co644 = soil_co644.merge(table_co644, left_on='MUSYM', right_on='musym')
co645 = soil_co645.merge(table_co645, left_on='MUSYM', right_on='musym')
co651 = soil_co651.merge(table_co651, left_on='MUSYM', right_on='musym')
co653 = soil_co653.merge(table_co653, left_on='MUSYM', right_on='musym')

co001.insert(10, 'mapunit', 'co001')
co618.insert(10, 'mapunit', 'co618')
co641.insert(10, 'mapunit', 'co641')
co642.insert(10, 'mapunit', 'co642')
co643.insert(10, 'mapunit', 'co643')
co644.insert(10, 'mapunit', 'co644')
co645.insert(10, 'mapunit', 'co645')
co651.insert(10, 'mapunit', 'co651')
co653.insert(10, 'mapunit', 'co653')

all_counties = pd.concat([co001, co618, co641, co642, co643, co644, co645, co651, co653])
all_counties = all_counties.set_geometry('geometry_x')

watershed_intersect = gpd.overlay(all_counties, watershed, how='intersection')

