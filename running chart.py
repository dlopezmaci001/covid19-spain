# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:32:54 2020

@author: Daniel
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
import datetime as dt

df = pd.read_csv(r'C:\Users\Daniel\Documents\GitHub\coronas\grafana_data_export (4).csv',sep=';')

current_year = '26-03-2020'
dff = (df[df['Time'].eq(current_year)]
       .sort_values(by='values', ascending=True)
       )

dff

fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(dff['Series'], dff['values'])

# colors 

colors = dict(zip(['Aragón', 'Asturias', 'Baleares', 'Canarias', 'Cantabria',
       'Castilla La Mancha', 'Castilla y León', 'Cataluña', 'Ceuta',
       'C Valenciana', 'Extremadura', 'Galicia', 'Madrid', 'Melilla',
       'Murcia', 'Navarra', 'País Vasco', 'La Rioja', 'Andalucía'],
                  ['#de4d44','#9e3744','#ff842a','#fc766a',
                  '#c83e74', '#8d9440','#fed65e','#2e5d9f','#755841',
                  '#daa03d','#616247','#3b3a50','#615550','#f2edd7',
                  '#d7c49e','#d13b40','#ffaf12','#4ec5a5','#565d47']))

group_lk = df.set_index('Time')['Series'].to_dict()


fig, ax = plt.subplots(figsize=(15, 8))
df = df[::-1]   # flip values from top to bottom
# pass colors values to `color=`
ax.barh(df['Series'], df['values'], color=[colors[x] for x in df['Series']])
# iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
for i, (value, name) in enumerate(zip(df['values'], df['Series'])):
    ax.text(value, i,     name,            ha='right')  # Tokyo: name
    # ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: group name
    ax.text(value, i,     value,           ha='right')   # 38194.2: value
# Add year right middle portion of canvas
ax.text(1, 0.4, current_year, transform=ax.transAxes, size=32, ha='right')