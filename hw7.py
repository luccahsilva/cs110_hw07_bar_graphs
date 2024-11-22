
'''
COMP_SCI 110: Homework 7
Name:
NetID:
'''
from tkinter import Canvas, Tk
import os
cwd = os.getcwd()

# Constant values for our bar chart
MARGIN = 65
WIDTH = 1000
HEIGHT = 400


# Create our window and canvas
gui = Tk()
gui.title('Bar Chart')
canvas = Canvas(gui, width=WIDTH, height=HEIGHT, background='white')

# add the canvas to the window
canvas.pack()

#drawing the horizontal lines of the bar graph!
kj = 18000
for i in range(9):
    i = i+1
    x = i/2
    kj = kj - 2000
    y = (MARGIN * 0.75) + MARGIN * x
    font_size = 12
    canvas.create_line(MARGIN, y, (WIDTH - MARGIN), y, fill='#999999', width = 1)
    canvas.create_text(MARGIN * .5, y, text = str(kj) + ' kJ', fill = 'blue', font = ("Arial", font_size), anchor = 'center')
    
   
#opening up my CSV and creating the country and food energy variables

file = open(cwd + '/food_data_2018.csv', mode = 'r')
next(file)
energy_by_country = {}
for line in file:
    row = line.strip().split(',')
    
    country = row[0]
    food_energy= int(row [1])

    energy_by_country[country] =food_energy

#creating the code for the bar graph

num_countries = len(energy_by_country)
bar_padding = 5  # pixels between bars
width_of_graph = WIDTH - 2 * MARGIN
width_of_bar = (width_of_graph - (num_countries * bar_padding)) / num_countries

graph_start_x = MARGIN
graph_top_y = MARGIN # NOT THE TOP LINE -- THE TOP THAT A BAR IS ALLOWED TO REACH
graph_bottom_y = (MARGIN * 0.75) + MARGIN * 5

graph_height = graph_bottom_y - graph_top_y
# margin / 2 == 2000 kj
"""
for every kj, the height should go up by (val / 2,000) * (margin / 2)
"""
max_kj = int(float(graph_height) / float(MARGIN / 2.0)) * 2000

# margin = 65 therefore 65 = 2000 kj therefore 1kj = 65/2000 = 0.0325
# one pixel = 0.0325kj


def draw_bar(country, food_energy, index):
    # expects 0-indexing like a normal person
    bar_height = (food_energy / 2000) * (MARGIN / 2)
    y_offset = 0
    if food_energy < max_kj:
        y_offset = (max_kj - food_energy) / (MARGIN / 2000)

    y_offset += graph_top_y
    y0 = y_offset
    y1 = graph_bottom_y
    

    num_paddings = ((index) *2) +1

    x0 = (num_paddings * bar_padding) + (width_of_bar * index) + graph_start_x
    x1 = x0 + width_of_bar

    canvas.create_rectangle(x1, y1, x0, y0, fill="orange")

for i in range(len(energy_by_country)):
    country = list(energy_by_country.keys())[i]
    energy = energy_by_country[country]
    draw_bar(country, energy, i)
    









canvas.mainloop()