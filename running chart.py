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

df = pd.read_csv(r'C:\Users\dlopezmacias\Documents\GitHub\covid19-spain\grafana_data_export (4).csv',sep=';')

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
                  '#daa03d','#616247','#7fffD4','#ff4500','#f2edd7',
                  '#d7c49e','#d13b40','#ffaf12','#4ec5a5','#008000']))

group_lk = dff.set_index('Time')['Series'].to_dict()


fig, ax = plt.subplots(figsize=(15, 8))

# pass colors values to `color=`
ax.barh(dff['Series'], dff['values'], color=[colors[x] for x in dff['Series']])
# iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
for i, (value, name) in enumerate(zip(dff['values'], dff['Series'])):
    ax.text(value, i,     name,            ha='right')  # Tokyo: name
    # ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: group name
    ax.text(value, i,     value,           ha='left')   # 38194.2: value
# Add year right middle portion of canvas
ax.text(1, 0.4, current_year, transform=ax.transAxes, size=32, ha='right')

fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(current_year):
    dff = df[df['Time'].eq(current_year)].sort_values(by='values', ascending=True)
    ax.clear()
    ax.barh(dff['Series'], dff['values'], color=[colors[x] for x in dff['Series']])
    dx = dff['values'].max() / 200
    for i, (value, name) in enumerate(zip(dff['values'], dff['Series'])):
        ax.text(value-dx, i,     name,           size=12, weight=600, ha='right', va='center')
        # ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.4, current_year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Casos positivos', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'Número de casos de COVID-19 por CCAA',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0, 'by @Nimerya', transform=ax.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
    
draw_barchart('26-03-2020')

import matplotlib.animation as animation
from IPython.display import HTML

mini = min(df.Time)

maxi = max(df.Time)

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=df.Time,interval = 0.5)
HTML(animator.to_jshtml()) 
animator.save('carrera.mp4')
# or use animator.to_html5_video() or animator.save() 
animator.to_html5_video(animator.to_jshtml()) 
animator.save('video_to_show.mp4')
animator.to_html5_video()
animator.save('2osc.mp4', writer="ffmpeg")
fig.show()

