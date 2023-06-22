import time
import geopandas as gpd
import matplotlib.pyplot as plt
import keyboard
from shapely import LineString

def on_key_press(event):
    if event.name == 'space':
        Vreme_tekst = ax.text(0.01, 0.01, "Vreme : ", transform=ax.transAxes, fontsize=8, verticalalignment='bottom')
        Ime_tekst = ax.text(0.01, 0.04, "Naziv Objekta : ", transform=ax.transAxes, fontsize=8, verticalalignment='bottom')

        sorted_shapefile = putanja_shapefile.sort_values('Redosled')

        for geometry, Stajaliste, vreme, ime in zip(sorted_shapefile['geometry'],
                                                    sorted_shapefile['Stajaliste'],
                                                    sorted_shapefile['Vreme'],
                                                    sorted_shapefile['Objekat']):
            linestring = LineString(geometry)
            gs_linestring = gpd.GeoSeries([linestring])
            gs_linestring.plot(ax=ax, color='red', linewidth=4)

            if Stajaliste == 1:
                Vreme_tekst.set_text("Vreme : "+vreme)
                Ime_tekst.set_text("Naziv stajalista : "+ime)

            plt.draw()
            time.sleep(1)
        ax.text(0.01, 0.07, "Duzina puta : 5.5km", transform=ax.transAxes, fontsize=8, verticalalignment='bottom')
        plt.draw()

karaburma_shapefile = gpd.read_file("shp_files/NaseljeSHP.shp")
putanja_shapefile = gpd.read_file("shp_files/Nova putanja.shp")
stajaliste_shapefile = gpd.read_file("shp_files/StajalistaXY.shp")

keyboard.on_press(on_key_press)

fig, ax = plt.subplots(figsize=(15,15))

karaburma_shapefile.plot(ax=ax, color='lightgrey', edgecolor='black')
stajaliste_shapefile.plot(ax=ax, color='green', markersize=20)

point_counter = 1
x_offset = 1
y_offset = 3
for x, y, label in zip(stajaliste_shapefile.geometry.x,
                       stajaliste_shapefile.geometry.y,
                       stajaliste_shapefile['Naziv']):
    if point_counter == 2 or point_counter == 6:
        y_offset = -2
    ax.annotate(point_counter, xy=(x, y), xytext=(x_offset, y_offset), textcoords="offset points", color='green')
    point_counter += 1
    x_offset = 4
    y_offset = 4

ax.text(0.18, 1.00, "Putanja odvozenja otpada - Karaburma", transform=ax.transAxes, fontsize=20, verticalalignment='bottom')

plt.show()