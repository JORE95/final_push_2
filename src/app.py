# %%
import dash
from dash import html, dcc, Input, Output, State
from dash import callback_context as ctx 
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageFont
from IPython.display import display, Image as IPImage
from io import StringIO
from io import BytesIO

import math
import base64
import io
import requests





# %%
csd = """Roote,Connection,Level,Level1,Level2,Level3
T/I/R/A/J,I/A/J,1,0,0,yes
T/I/R/A/J,T/I/R/A/J,1,0,0,no
I/A/J,I/A,2,0,0,yes
I/A/J,I/A/J,2,0,0,no
T/I/R/A/J,T/I/R/A,2,0,0,yes
T/I/R/A/J,T/I/R/A/J,2,0,0,no
I/A,I,3,0,0,yes
I/A,I/A,3,0,0,no
I/A/J,I,3,0,1,yes
I/A/J,I/A/J,3,0,0,no
T/I/R/A,T/I/R,3,0,0,yes
T/I/R/A,T/I/R/A,3,0,0,no
T/I/R/A/J,T/I/R,3,0,1,yes
T/I/R/A/J,T/I/R/A/J,3,0,0,no
I,0,4,0,0,yes
I,I,4,0,0,no
I/A,A,4,0,0,yes
I/A,I/A,4,0,0,no
I,0,4,1,1,yes
I,I,4,1,1,no
I/A/J,A/J,4,0,0,yes
I/A/J,I/A/J,4,0,0,no
T/I/R,T/R,4,0,0,yes
T/I/R,T/I/R,4,0,0,no
T/I/R/A,T/R/A,4,0,0,yes
T/I/R/A,T/I/R/A,4,0,0,no
T/I/R,T/R,4,1,1,yes
T/I/R,T/I/R,4,1,1,no
T/I/R/A/J,T/R/A/J,4,0,0,yes
T/I/R/A/J,T/I/R/A/J,4,0,0,no
0,0,5,0,0,yes
0,0,5,0,1,no
I,I,5,0,0,yes
I,I,5,0,1,no
A,A,5,0,0,yes
A,A,5,0,1,no
I/A,I/A,5,0,0,yes
I/A,I/A,5,0,1,no
0,0,5,1,2,yes
0,0,5,1,3,no
I,I,5,1,2,yes
I,I,5,1,3,no
A/J,A/J,5,0,0,yes
A/J,A/J,5,0,1,no
I/A/J,I/A/J,5,0,0,yes
I/A/J,I/A/J,5,0,1,no
T/R,R,5,0,0,yes
T/R,T/R,5,0,0,no
T/I/R,I/R,5,0,0,yes
T/I/R,T/I/R,5,0,0,no
T/R/A,R/A,5,0,0,yes
T/R/A,T/R/A,5,0,0,no
T/I/R/A,I/R/A,5,0,0,yes
T/I/R/A,T/I/R/A,5,0,0,no
T/R,R,5,1,1,yes
T/R,T/R,5,1,1,no
T/I/R,I/R,5,1,1,yes
T/I/R,T/I/R,5,1,1,no
T/R/A/J,R/A/J,5,0,0,yes
T/R/A/J,T/R/A/J,5,0,0,no
T/I/R/A/J,I/R/A/J,5,0,0,yes
T/I/R/A/J,T/I/R/A/J,5,0,0,no
0,0,6,0,0,yes
0,0,6,0,1,no
0,0,6,1,2,yes
0,0,6,1,3,no
I,I,6,0,0,yes
I,I,6,0,1,no
I,I,6,1,2,yes
I,I,6,1,3,no
A,A,6,0,0,yes
A,A,6,0,1,no
A,A,6,1,2,yes
A,A,6,1,3,no
I/A,I/A,6,0,0,yes
I/A,I/A,6,0,1,no
I/A,I/A,6,1,2,yes
I/A,I/A,6,1,3,no
0,0,6,2,4,yes
0,0,6,2,5,no
0,0,6,3,6,yes
0,0,6,3,7,no
I,I,6,2,4,yes
I,I,6,2,5,no
I,I,6,3,6,yes
I,I,6,3,7,no
A/J,A/J,6,0,0,yes
A/J,A/J,6,0,1,no
A/J,A/J,6,1,2,yes
A/J,A/J,6,1,3,no
I/A/J,I/A/J,6,0,0,yes
I/A/J,I/A/J,6,0,1,no
I/A/J,I/A/J,6,1,2,yes
I/A/J,I/A/J,6,1,3,no
R,0,6,0,8,yes
R,R,6,0,0,no
T/R,T,6,0,0,yes
T/R,T/R,6,0,0,no
I/R,I,6,0,8,yes
I/R,I/R,6,0,0,no
T/I/R,T/I,6,0,0,yes
T/I/R,T/I/R,6,0,0,no
R/A,A,6,0,4,yes
R/A,R/A,6,0,0,no
T/R/A,T/A,6,0,0,yes
T/R/A,T/R/A,6,0,0,no
I/R/A,I/A,6,0,4,yes
I/R/A,I/R/A,6,0,0,no
T/I/R/A,T/I/A,6,0,0,yes
T/I/R/A,T/I/R/A,6,0,0,no
R,0,6,1,9,yes
R,R,6,1,1,no
T/R,T,6,1,1,yes
T/R,T/R,6,1,1,no
I/R,I,6,1,9,yes
I/R,I/R,6,1,1,no
T/I/R,T/I,6,1,1,yes
T/I/R,T/I/R,6,1,1,no
R/A/J,A/J,6,0,4,yes
R/A/J,R/A/J,6,0,0,no
T/R/A/J,T/A/J,6,0,0,yes
T/R/A/J,T/R/A/J,6,0,0,no
I/R/A/J,I/A/J,6,0,4,yes
I/R/A/J,I/R/A/J,6,0,0,no
T/I/R/A/J,T/I/A/J,6,0,0,yes
T/I/R/A/J,T/I/R/A/J,6,0,0,no
0,0,7,0,0,yes
0,0,7,0,1,no
0,0,7,1,2,yes
0,0,7,1,3,no
0,0,7,2,4,yes
0,0,7,2,5,no
0,0,7,3,6,yes
0,0,7,3,7,no
I,I,7,0,0,yes
I,I,7,0,1,no
I,I,7,1,2,yes
I,I,7,1,3,no
I,I,7,2,4,yes
I,I,7,2,5,no
I,I,7,3,6,yes
I,I,7,3,7,no
A,A,7,0,0,yes
A,A,7,0,1,no
A,A,7,1,2,yes
A,A,7,1,3,no
A,A,7,2,4,yes
A,A,7,2,5,no
A,A,7,3,6,yes
A,A,7,3,7,no
I/A,I/A,7,0,0,yes
I/A,I/A,7,0,1,no
I/A,I/A,7,1,2,yes
I/A,I/A,7,1,3,no
I/A,I/A,7,2,4,yes
I/A,I/A,7,2,5,no
I/A,I/A,7,3,6,yes
I/A,I/A,7,3,7,no
0,0,7,4,8,yes
0,0,7,4,9,no
0,0,7,5,10,yes
0,0,7,5,11,no
0,0,7,6,12,yes
0,0,7,6,13,no
0,0,7,7,14,yes
0,0,7,7,15,no
I,0,7,4,16,yes
I,I,7,4,8,no
I,0,7,5,17,yes
I,I,7,5,9,no
I,0,7,6,18,yes
I,I,7,6,10,no
I,0,7,7,19,yes
I,I,7,7,11,no
A/J,A,7,0,8,yes
A/J,A/J,7,0,0,no
A/J,A,7,1,9,yes
A/J,A/J,7,1,1,no
A/J,A,7,2,10,yes
A/J,A/J,7,2,2,no
A/J,A,7,3,11,yes
A/J,A/J,7,3,3,no
I/A/J,A,7,0,12,yes
I/A/J,I/A/J,7,0,0,no
I/A/J,A,7,1,13,yes
I/A/J,I/A/J,7,1,1,no
I/A/J,A,7,2,14,yes
I/A/J,I/A/J,7,2,2,no
I/A/J,A,7,3,15,yes
I/A/J,I/A/J,7,3,3,no
0,0,7,8,20,yes
0,0,7,8,21,no
R,R,7,0,0,yes
R,R,7,0,1,no
T,0,7,0,22,yes
T,T,7,0,0,no
T/R,R,7,0,2,yes
T/R,T/R,7,0,0,no
I,0,7,8,23,yes
I,I,7,8,12,no
I/R,R,7,0,3,yes
I/R,I/R,7,0,0,no
T/I,0,7,0,24,yes
T/I,T/I,7,0,0,no
T/I/R,R,7,0,4,yes
T/I/R,T/I/R,7,0,0,no
A,A,7,4,16,yes
A,A,7,4,17,no
R/A,R/A,7,0,0,yes
R/A,R/A,7,0,1,no
T/A,A,7,0,18,yes
T/A,T/A,7,0,0,no
T/R/A,R/A,7,0,2,yes
T/R/A,T/R/A,7,0,0,no
I/A,A,7,4,19,yes
I/A,I/A,7,4,8,no
I/R/A,R/A,7,0,3,yes
I/R/A,I/R/A,7,0,0,no
T/I/A,A,7,0,20,yes
T/I/A,T/I/A,7,0,0,no
T/I/R/A,R/A,7,0,4,yes
T/I/R/A,T/I/R/A,7,0,0,no
0,0,7,9,25,yes
0,0,7,9,26,no
R,R,7,1,5,yes
R,R,7,1,6,no
T,0,7,1,27,yes
T,T,7,1,1,no
T/R,R,7,1,7,yes
T/R,T/R,7,1,1,no
I,0,7,9,28,yes
I,I,7,9,13,no
I/R,R,7,1,8,yes
I/R,I/R,7,1,1,no
T/I,0,7,1,29,yes
T/I,T/I,7,1,1,no
T/I/R,R,7,1,9,yes
T/I/R,T/I/R,7,1,1,no
A/J,A,7,4,21,yes
A/J,A/J,7,4,4,no
R/A/J,R/A,7,0,5,yes
R/A/J,R/A/J,7,0,0,no
T/A/J,A,7,0,22,yes
T/A/J,T/A/J,7,0,0,no
T/R/A/J,R/A,7,0,6,yes
T/R/A/J,T/R/A/J,7,0,0,no
I/A/J,A,7,4,23,yes
I/A/J,I/A/J,7,4,4,no
I/R/A/J,R/A,7,0,7,yes
I/R/A/J,I/R/A/J,7,0,0,no
T/I/A/J,A,7,0,24,yes
T/I/A/J,T/I/A/J,7,0,0,no
T/I/R/A/J,R/A,7,0,8,yes
T/I/R/A/J,T/I/R/A/J,7,0,0,no"""
csv_data = StringIO(csd)

pd_data = pd.read_csv(csv_data)






# %%
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Global variable to cache the font
_cached_font = None

def get_cached_font(size):
    global _cached_font
    
    if _cached_font is None:
        # Download and cache the font once
        font_url = "https://github.com/google/fonts/raw/main/ofl/carlito/Carlito-Regular.ttf"
        response = requests.get(font_url)
        font_data = BytesIO(response.content)
        _cached_font = ImageFont.truetype(font_data, size=size)
    
    return _cached_font

def icon(letter):
    size = (200, 200)
    
  
    colors = {
        "A": "green", "B": "blue", "C": "black", "D": "orange", "E": "purple", "F": "yellow", 
        "G": "pink", "H": "brown", "I": "pink", "J": "orange", "K": "cyan", "L": "magenta", 
        "M": "lime", "N": "teal", "O": "indigo", "P": "maroon", "Q": "navy", "R": "turquoise", 
        "S": "aqua", "T": "red", "U": "tan", "V": "turquoise", "W": "violet", "X": "gold", 
        "Y": "khaki", "Z": "lavender"
    }
    

    color = colors.get(letter.upper(), "gray")  
    

    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)


    corner_radius = 20
    draw.rounded_rectangle([(1, 1), (size[0]-1, size[1]-1)], radius=corner_radius, fill=color)
    

    font = get_cached_font(size=180)


    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

 
    text_position = ((size[0] - text_width) // 2, (size[1] - text_height*2) // 2)
    

    draw.text(text_position, letter, fill="white", font=font)
    
    return image




# %%
def create_combined_image(letters, i_con):
    combined_w = []
    combined_h = []
    list = []
    for i in letters:
        yy = i.split('-')[0]
        yy = yy.split('/')  
        num_icons = len(yy)
        icon_size = (200, 200)
        
        if num_icons == 4:
            combined_width = int(icon_size[0] * 2.5)
            combined_height = icon_size[1] * 2
        elif num_icons == 5:
            combined_width = icon_size[0] * 3
            combined_height = icon_size[1] * 2
        elif num_icons == 3:
            combined_width = icon_size[0] * 2
            combined_height = icon_size[1] * 2
        else:
            combined_width = icon_size[0] * num_icons
            combined_height = icon_size[1]
        
        combined_w.append(combined_width)
        combined_h.append(combined_height)

        combined_image = Image.new("RGBA", (combined_width, combined_height), (255, 255, 255, 0))
        
        for j, letter in enumerate(yy):
            icon_image = i_con(letter)
            if num_icons == 3:
                if j == 0:
                    combined_image.paste(icon_image, (icon_size[0] // 2, 0), icon_image)
                else:
                    combined_image.paste(icon_image, ((j - 1) * icon_size[0], icon_size[1]), icon_image)
            elif num_icons == 4:
                if j == 0:
                    combined_image.paste(icon_image, (icon_size[0] // 2, 0), icon_image)
                elif j == 1:
                    combined_image.paste(icon_image, (int(icon_size[0] * 1.5), 0), icon_image)
                else:
                    combined_image.paste(icon_image, ((j - 2) * icon_size[0], icon_size[1]), icon_image)
            elif num_icons == 5:
                if j == 0:
                    combined_image.paste(icon_image, (0, 0), icon_image)
                elif j == 1:
                    combined_image.paste(icon_image, (icon_size[0], 0), icon_image)
                elif j == 2:
                    combined_image.paste(icon_image, (icon_size[0] * 2, 0), icon_image)
                else:
                    combined_image.paste(icon_image, ((j - 3) * icon_size[0], icon_size[1]), icon_image)
            else:
                combined_image.paste(icon_image, (j * icon_size[0], 0), icon_image)
        
        buffered = io.BytesIO()
        combined_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        list.append(img_str)
    
    icon_base64 = dict(zip(letters, list))
    return icon_base64, combined_w, combined_h




# %%
node_labels = ["Hart failure", "ASCD VTE HZ", "Malignancy", "Diverticultis", "AAB DMD", "IG Vaccination", "RA ILD"]



def create_nodes_and_edges_e2(node_labels, background_images):
    radius_x = 600
    radius_y = 400
    center_x = -200
    center_y = -200

    icon_base64 = []
    for i in range(7):
        icon_base64.append(background_images[i])


    elements2 = [
        {
            'data': {'id': f'node{i}', 'label': node_labels[i]},
            'position': {
            'x': center_x - radius_x * math.cos(math.pi * (i - 3) / 14), 
            'y': center_y + radius_y * math.sin(math.pi * (i - 3) / 14) 
            }
        }
        for i in range(7)
    ]

 
    edges2 = [
        {'data': {'source': f'node{i}', 'target': f'node{i+1}'}, "classes": "invisibleEdge"}
        for i in range(6)
    ]
    edges2.append({'data': {'source': 'node6', 'target': 'node0'}, "classes": "invisibleEdge"})

    elements2.extend(edges2)

    stylesheet = [
        {
            'selector': 'node',
            'style': {
                'background-color': '#BFD7B5',
                'width': 50,
                'height': 50,
                'label': 'data(label)',
                'text-halign': 'center',
                'text-valign': 'center',
                'font-size': '12px',
                'color': 'black'

            }
        }
    ]


    stylesheet.extend([
        {
            'selector': f'#node{i}', 
            'style': {
                "background-fit": "contain",
                'background-image': icon_base64[i],  
                "background-position": "50% 50%",
                "background-color": "#ffebee",  
                "border-color": "#f44336", 
                "border-width": 3,
                "border-opacity": 1,
                "border-style": "solid",
                "width": 50,  
                "height": 50,
                "font-size": "12px",
                "text-valign": "bottom",
                "text-halign": "center",
                "text-margin-y": 8,
                'grabify': 'false'
            }
        }
        for i in range(7)
    ])

    stylesheet.append({
        'selector': 'edge.invisibleEdge', 
        'style': {
            'line-color': 'white',  
            'width': 0  
        }
    })

    return elements2, stylesheet, icon_base64







def create_nodes_and_edges_updates(number, node_labels, icon_base64):

    number = int(number) // 10 


    colors = ["#1F77B4",  # Muted Blue
          "#FF7F0E",  # Muted Orange
          "#2CA02C",  # Muted Green
          "#D62728",  # Muted Red
          "#9467BD",  # Muted Purple
          "#8C564B",  # Muted Brown
          "#E377C2"]  # Muted Pink


    radius_x = 400
    radius_y = 200
    center_x = -500
    center_y = 800


    e2 = [
        {
            'data': {'id': f'node{i}', 'label': node_labels[i]},
            'position': {
                'x': center_x - radius_x * math.cos(math.pi * i / 6),
                'y': center_y - radius_y * math.sin(math.pi * i / 6)
            }
        }
        for i in range(7)
    ]

    edges2 = [
        {'data': {'source': f'node{i}', 'target': f'node{i+1}'}, "classes": "invisibleEdge"}
        for i in range(6)
    ]
    edges2.append({'data': {'source': 'node6', 'target': 'node0'}, "classes": "invisibleEdge"})
    e2.extend(edges2)

    s2 = [
        {
            'selector': 'node',
            'style': {
                'background-color': '#BFD7B5',
                'label': 'data(label)',
                'text-halign': 'center',
                'text-valign': 'center',
                'font-size': '12px',
                'color': 'black',
                'bottom': 500
            }
        }
    ]


    s2.extend([
        {
            'selector': f'#node{i}',
            'style': {
                'background-fit': 'contain',
                'background-image': icon_base64[i],
                'width': 100 if i == number else 50,  
                'height': 100 if i == number else 50,
                'background-position': '50% 50%',
                'background-color': colors[i] if i == number else '#e0e0e0',
                'border': f'2px solid {colors[i]}' if i == number else '2px solid #e0e0e0',
                'border-width': 3,
                'border-opacity': 1,
                'background-opacity': 0.5,  
                'border-style': 'solid',
                'font-size': '20px' if i == number else '12px',
                'text-valign': 'bottom',
                'text-halign': 'center',
                'text-margin-y': 8,
                'bootstrap-tooltip': node_labels[i],
                'grabify': 'false'

            }
        }
        for i in range(7)
    ])

    s2.append({
        'selector': 'edge.invisibleEdge',
        'style': {
            'line-color': 'white',
            'width': 0
        }
    })

    return e2, s2

# %% [markdown]
# #Nodes and Edges

# %%
standart_layout={'name': 'preset'}


  
stylesheet_basic = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(id)',
            'font-size': '0px',
            'background-image': 'data(image)',
            'background-clip': 'none',
            'background-color': 'transparent',
            'background-opacity': 0,
            'width': 'data(w)',
            'height': 'data(h)',




        }
    },
    {
        'selector': 'edge',
        'style': {
            'label': 'data(label)',
            'font-size': '0px',
                }
    },
    {
        'selector': 'edge:selected',
        'style': {
            'label': 'data(label)',
            'curve-style': 'bezier',
            'font-size': '40px',
            'color': 'white',
            'text-background-color': 'gray',
            'text-background-opacity': 1,
            'shape': 'ellipse',
            'text-background-padding': '30px',
            'text-border-color': 'black',
            'text-border-opacity': 1,
            'text-border-width': '1px',
            'line-color': 'gray',
            'line-style': 'dashed',
            'target-arrow-color': 'gray',
            'target-arrow-shape': 'triangle',
            'arrow-scale': 3

        }
    },
    {
        'selector': '.highlighted',
        'style': {
            'line-color': 'red',
            'target-arrow-color': 'yellow',
            'source-arrow-color': 'yellow',
            'width': 4

        }
    },
    {
        'selector': '.darken',
        'style': {
            'line-color': 'grey',
            'target-arrow-color': 'grey',
            'source-arrow-color': 'grey',
            'width': 1

        }
    }
]



def create_nodes_and_edges(csd):
    csd = StringIO(csd)
    df = pd.read_csv(csd).reset_index(drop=True)
    df['Level'] = pd.to_numeric(df['Level'], errors='coerce').astype('Int64')
    df['Level1'] = pd.to_numeric(df['Level1'], errors='coerce').astype('Int64')
    df['Level2'] = pd.to_numeric(df['Level2'], errors='coerce').astype('Int64')



    df["Level_R"] = df["Level"].astype(int) - 1
    df["Level_R2"] = df["Level1"]


    df["Roote"] = df["Roote"] + "-" + df["Level_R"].astype(str) + df["Level_R2"].astype(str)
    df["Connection"] = df["Connection"] + "-" + df["Level"].astype(str) + df["Level2"].astype(str)

   
    num_circles = 7
    pi = np.pi

  
    levels = df.groupby('Level').size().reset_index(name='count')


    df['p_x'] = 400
    df['p_y'] = 200
    df['p_x'] = df['p_x'].astype('float64')
    df['p_y'] = df['p_y'].astype('float64')

    for _, row in levels.iterrows():
        level = row['Level']
        num_nodes_on_circle = row['count']
        radius = level * 1200

      
        angles = np.linspace(0, 2 * pi, num=num_nodes_on_circle, endpoint=False)
        
       
        x_scale = 1.5 
        y_scale = 0.8 

    
        df.loc[df['Level'] == level, 'p_x'] = radius * np.cos(angles) * x_scale
        df.loc[df['Level'] == level, 'p_y'] = radius * np.sin(angles) * y_scale



    nodes1 = [i for i in df["Roote"]]
    nodes2 = [i for i in df["Connection"]]
    nodes = nodes1 + nodes2
    nodes=set(nodes)

    df2=pd.DataFrame(nodes, columns=["Connection"])

    df3=pd.merge(df2, df, on="Connection", how="left")[["Connection", "Level3", "p_x", "p_y"]].fillna(0)

    df3=df3.rename(columns={"Connection":"nodes"})

    

    edges = [
        {
            'data': {
                'source': df["Roote"][i],
                'target': df["Connection"][i],
                'label': df["Level3"][i]
            },
            'style': {             
                'label': str(df["Level3"][i]),

            },
            'classes': f'source-{df["Roote"][i]}_target-{df["Connection"][i]}' 
        }
        for i in range(len(df))]
    


    icon_base64, w, h = create_combined_image(nodes, icon)

    df = df.reset_index(drop=True)

    nodes = [
        {
            'data': {
                'id': df3["nodes"][i], 
                'label': df3["nodes"][i], 
                'image': f'data:image/png;base64,{icon_base64[df3["nodes"][i]]}', 
                'w': f'{w[i]}', 
                'h': f'{h[i]}',
            },
            'position': {'x': df3['p_x'][i], 'y': df3['p_y'][i]}, 
            'classes': f'{df3["Level3"][i]}'


        }
        for i in range(len(df3["nodes"]))
    ]
    stylesheet= stylesheet_basic

    return nodes, edges, df, stylesheet







def process_nodes_and_edges(csd, node_id):
    nodes, edges, df, stylesheet = create_nodes_and_edges(csd)
    new_nodes_XX=[]

    def get_matching_edges(nodes, node_id):
        found_node = None
        x = -1  

        for index, node in enumerate(nodes):
            if node['data']['id'] == node_id:
                found_node = node
                x = index
                break 

        if found_node is None:
            return None

        return x

    x = get_matching_edges(nodes, node_id)

    if x is None:
        return None

    matching_edges = [
        {
            'data': edge['data'],
            'style': {         
                'label': edge['data']['label']
            },
            'classes': f"source-{edge['data']['source']}_target-{edge['data']['target']}"  
        }
        for edge in edges if edge['data']['source'] == nodes[x]['data']['id']
    ]

    new_nodes_XX = [matching_edges[i]['data']['target'] for i in range(len(matching_edges))] + [nodes[x]['data']['id']]
    

    dn = pd.DataFrame(new_nodes_XX, columns=["Connection"])
    dn=dn.drop_duplicates()

    
  
    new_nodes_df = pd.merge(dn, df, on="Connection", how="left")[["Connection", "Level3"]].fillna(0)
    new_nodes_df["Level3"] = new_nodes_df["Level3"].astype(str)


    icon_base64, w, h = create_combined_image(new_nodes_df["Connection"].tolist(), icon)


    new_nodes = [
        {
            'data': {'id': new_nodes_df["Connection"][i], 'label': new_nodes_df["Connection"][i],'image': f'data:image/png;base64,{icon_base64[new_nodes_df["Connection"][i]]}', 'w': f'{w[i]}', 'h': f'{h[i]}'},
            'classes': f'{new_nodes_df["Level3"][i]}'

        }
        for i in range(len(new_nodes_df))
    ]
 

  
    stylesheet = stylesheet_basic
 


    return new_nodes, matching_edges, stylesheet



def rebuild_and_highlight_graph(csd, Test,  elements2, nodes_classes, background_images, node_labels):
    layout=standart_layout
    
    nodes, edges, df, stylesheet = create_nodes_and_edges(csd)
    
    elements2, stylesheet_graphic, icon_base64=create_nodes_and_edges_e2(node_labels, background_images)



    for edge in edges:
        if edge['classes'] in Test:
            edge['classes'] = 'highlighted'
        else:
            edge['classes'] = 'darken'
    

    elements = nodes + edges
    s2 = stylesheet_graphic
    e2 = elements2

    outy = "End of story"
    outy2= "This is what youb selected"
    stylesheet= stylesheet_basic
    layout=standart_layout
    postion={'width': '100%', 'height': '100%','left':-500, 'position': 'absolute','zIndex': 1}
    positon_g1={'width': '100%', 'height': '100%', 'position': 'absolute', 'zIndex': 0}
    


    Test=[]
    save=[]

    
    return layout, elements,stylesheet, s2, e2, nodes_classes, outy, Test, outy2, postion, positon_g1, save

# %%
edges = []
nodes = []




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
server = app.server 



icon_list=["covid:covid19-virus-3", "covid:virus-lab-research-medicine-pill", "game-icons:abstract-036", "game-icons:abstract-015", "fontisto:oracle", "fontisto:helicopter-ambulance", "iwwa:connection-o"]
background_images=[]

for i in icon_list:
    icony=f"https://api.iconify.design/{i}.svg"
    background_images.append(icony)


node_labels = ["Welcome to the tharpeutic matchmaking","Heart failure?", "SCVD, VTE, HZ?", "Malignancy?", "Diverticulitis?", "Autoantibodies, DMD?", "HG, vaccination?", "RA-ILD?"]


nodes, edges, df, stylesheet1 = create_nodes_and_edges(csd)
elements2, stylesheet_graphic, icon_base64=create_nodes_and_edges_e2(node_labels, background_images)

# %%
def logic(n):
    if n == 0:
        return "TNFi are contraindicated in moderate to severe heart failure (NYHA III/IV), and rituximab in severe heart failure (NYHA IV)."
    if n == 1:
        return "TNFi are contraindicated in moderate to severe heart failure (NYHA III/IV), and rituximab in severe heart failure (NYHA IV)."
    elif n == 2:
        return "JAKi should be prescribed only after careful consideration of benefit and risk in patients with current or history of ASCVD, VTE, and HZ."
    elif n == 3:
        return "Abatacept and JAKi might increase the risk of malignancies and might not be favored in patients with current or recent malignancies."
    elif n == 4:
        return "IL6i increase the risk for gastrointestinal perforations, especially in patients with current or history of diverticulitis; this potential risk has recently also been observed for JAKi."
    elif n == 5:
        return "Hypogammaglobulinemia may disfavor rituximab, and response to any planned vaccination may be limited after rituximab has been started."
    elif n == 6:
        return "Auto-antibody formation (like anti-nuclear antibodies, ANA, or double-stranded DNA antibodies, dsDNA) and demyelinating diseases (DMD) like Multiple sclerosis or Guillain-Barré syndrome have been observed in patients under TNFi therapy."
    elif n == 7:
        return "Conversely, specific extraarticular efficacy may positively select DMARDs: in RA-ILD, rituximab or abatacept may be favored over TNFi, IL6i, and JAKi."

    
def logic2(n):
    n=node_labels[n]
    return n





# %%



standart_layout={'name': 'preset',}
 
 
game_layout={
            'name': 'breadthfirst',
            'randomize': False,
            'gravity': 2,
            'idealEdgeLength': 2,
            'refresh': 20,
            'curved': 'straight',
            'move': False,
              
        }


w_=80
h_=80

qq=h_-20
s=60


# %%
controls = dbc.Card(
    [
        # Circular buttons with icons only and stronger border colors
        html.Div(
            [
                dbc.Button(
                    [  # Icon only, no text
                        html.I(className="fas fa-play-circle", style={'font-size': qq})  # Font Awesome Play Icon
                    ],
                    id="Start", color="primary", className="btn-lg",
                    style={
                        'width': w_,  # Circular button
                        'height': h_,  
                        'border-radius': '50%',  # Perfect circle
                        'background-color': '#5A9BD4',  # Soft blue background
                        'color': 'white',  
                        'border': '3px solid #3A6FA4',  # Stronger border in darker tone
                        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                        'transition': 'background-color 0.2s ease-in-out',
                        'display': 'flex',
                        'align-items': 'center',  # Center icon vertically
                        'justify-content': 'center',  # Center icon horizontally
                        'margin-bottom': s,  # Larger spacing between buttons
                    }
                ),
                dbc.Button(
                    [  # Icon only, no text
                        html.I(className="fas fa-sync", style={'font-size': qq})  # Font Awesome Sync Icon
                    ],
                    id="Reset", color="secondary", className="btn-lg",
                    style={
                        'width': w_,  # Circular button
                        'height': h_,  
                        'border-radius': '50%',  # Perfect circle
                        'background-color': '#E57373',  # Warm coral background
                        'color': 'white',  
                        'border': '3px solid #B64B4B',  # Stronger border in darker tone
                        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                        'transition': 'background-color 0.2s ease-in-out',
                        'display': 'flex',
                        'align-items': 'center',  
                        'justify-content': 'center',  
                        'margin-bottom': s,  
                    }
                ),
                dbc.Button(
                    [  # Icon only, no text
                        html.I(className="fas fa-check-circle", style={'font-size': qq})  # Font Awesome Check Circle Icon
                    ],
                    id="Yes", color="success", className="btn-lg",
                    style={
                        'width': w_,  # Circular button
                        'height': h_,    
                        'border-radius': '50%',  # Perfect circle
                        'background-color': '#66BB6A',  # Soft green background
                        'color': 'white',
                        'border': '3px solid #4A8B4A',  # Stronger border in darker tone
                        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',  
                        'display': 'flex',
                        'align-items': 'center',  
                        'justify-content': 'center',  
                        'margin-bottom': s,  
                        'transition': 'background-color 0.2s ease-in-out',
                    }
                ),
                dbc.Button(
                    [  # Icon only, no text
                        html.I(className="fas fa-times-circle", style={'font-size': qq})  # Font Awesome Times Circle Icon
                    ],
                    id="No", color="danger", className="btn-lg",
                    style={
                        'width': w_,  # Circular button
                        'height': h_,  
                        'border-radius': '50%',  # Perfect circle
                        'background-color': '#EF5350',  # Soft red background
                        'color': 'white',
                        'border': '3px solid #C62828',  # Stronger border in darker tone
                        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                        'display': 'flex',
                        'align-items': 'center',  
                        'justify-content': 'center',  
                        'margin-bottom': s,  
                        'transition': 'background-color 0.2s ease-in-out',
                    }
                ),
                dbc.Button(
                    [  # Icon only, no text
                        html.I(className="fas fa-stop-circle", style={'font-size':qq })  # Font Awesome Stop Circle Icon
                    ],
                    id="End", color="primary", 
                    style={
                        'width': w_,  # Circular button
                        'height': h_,  
                        'border-radius': '50%',  # Perfect circle
                        'background-color': '#7986CB',  # Muted slate blue background
                        'color': 'white', 
                        'border': '3px solid #4D5BAA',  # Stronger border in darker tone
                        'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                        'display': 'flex',
                        'align-items': 'center',  
                        'justify-content': 'center',  
                        'transition': 'background-color 0.2s ease-in-out',
                    }
                ),
            ],
            style={'textAlign': 'center'}
        ),
    ],
    style={
        'padding': '20px',
        'border-radius': '40px',  # Rounded for pill shape
        'background-color': 'rgba(255, 255, 255, 0.2)',  # Semi-transparent white background
        'backdrop-filter': 'blur(10px)',  # Frosted glass effect
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.3)',  # Stronger shadow for glassy effect
        'width': '80px',  # Adjust width to fit the circular buttons
        'position': 'absolute',
        'top': '200px',
        'right': '20px',
        'zIndex': 3,
        'textAlign': 'center',
        'color': '#000',  # Text color for contrast
        'font-family': '"San Francisco", "Segoe UI", sans-serif',  # Apple-like font family
    }
)

# %%


header = html.H1(
    "Welcome to the Network Graph", 
    style={
        'textAlign': 'center', 
        'color': 'black', 
        'font-size': '50px',  # Increase the font size
        'font-weight': '300',  # Lighter font
        'position': 'absolute',  
        'top': '10px',  # Add some space from the top
        'left': '50%', 
        'transform': 'translateX(-50%)',  # Center the text horizontally
        'zIndex': 10 
    }
)



reset=html.Div([dbc.Button("Reset", id="Reset", color="primary",  style={'margin': 10, 'width': '150px'})])
start=html.Div([dbc.Button("Start", id="Start", color="primary", style={'margin': 10, 'width': '150px'})])

text_output = html.Div([html.P("Output: ", id="Outy")])
text_output2 = html.Div([html.H1("Output: ", id="Outy2")])

header = html.H1(
    "Welcome to the Network Graph", 
    style={
        'textAlign': 'center', 
        'color': 'black', 
        'font-size': '50px',  # Increase the font size
        'font-weight': '300',  # Lighter font
        'position': 'absolute',  
        'top': '10px',  # Add some space from the top
        'left': '50%', 
        'transform': 'translateX(-50%)',  # Center the text horizontally
        'zIndex': 10 
    }
)



reset=html.Div([dbc.Button("Reset", id="Reset", color="primary",  style={'margin': 10, 'width': '150px'})])
start=html.Div([dbc.Button("Start", id="Start", color="primary", style={'margin': 10, 'width': '150px'})])

text_output = html.Div([html.P("Output: ", id="Outy")])
text_output2 = html.Div([html.H1("Output: ", id="Outy2")])

positon1={'width': '100%', 'height': '100%','left':-500, 'position': 'absolute','zIndex': 0}
positon2={'width': '100%', 'height': '100%','left':0, 'top':-200, 'position': 'absolute','zIndex': 0}
positon3={'overflow': 'hidden','width': '100%', 'height': '100%', "top":"100px", 'position': 'absolute', 'zIndex': 1}
positon4={'overflow': 'hidden','width': '100%', 'height': '100%', 'position': 'absolute', 'zIndex': 1}



cyto1 = cyto.Cytoscape(
    id='cytoscape',
    elements=nodes + edges,
    style=positon3,
    layout=standart_layout,
    maxZoom=1,
    minZoom=0.01,
    stylesheet=stylesheet1	
   
    )



cyto2 = cyto.Cytoscape(
    id='cytoscape2',
    elements=elements2,
    layout={'name': 'preset'},
    style=positon1,
    maxZoom=1,
    stylesheet=stylesheet_graphic
    )



zoom_level=0.5
 




jumbotron = html.Div(
    id='jumbotron',  
    children=dbc.Container(
        [
      
            html.H1(text_output2, className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                text_output,
                className="lead",
            ),

            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
            
        ],
        fluid=True,
        className="py-3"
    ),
    style={
        'position': 'absolute',
        'bottom': '10px',  
        'left': '50%',  
        'transform': 'translateX(-50%)',  
        'zIndex': 3,
        'width': '800px',
        'border': '1px solid #e0e0e0',
        'border-radius': '12px',
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.15)',
        'padding': '20px',
        'background-color': '#f7f7f7',
        'zIndex': 4,
    },
    className="p-3 bg-body-secondary rounded-3"
)





# %%
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([header,jumbotron, controls, cyto2, cyto1], 
            style={'width': '100%', 'height': '120vh'}),
            width=12
        )
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Store(id='nodes_classes'),
            dcc.Store(id='Test'),
            dcc.Store(id='save'),


        ])
    ])
], fluid=True, className='dashboard-container')



# %%





@app.callback(
    [   
        Output('cytoscape', 'layout'),
        Output('cytoscape', 'elements'),
        Output('cytoscape', 'stylesheet'),
        Output('cytoscape2', 'stylesheet'),
        Output('cytoscape2', 'elements'),
        Output('nodes_classes', 'data'),
        Output('Outy', 'children'),
        Output('Test', 'data'),
        Output('Outy2', 'children'),
        Output('cytoscape2', 'style'),
        Output('cytoscape', 'style'),
        Output('save', 'data')

    ],
    [
        Input('Reset', 'n_clicks'),
        Input("Start", 'n_clicks'),
        Input('cytoscape', 'tapNodeData'),
        Input('Yes', 'n_clicks'),
        Input('No', 'n_clicks'),
        Input('End', 'n_clicks')
    ],
    [State('nodes_classes', 'data'),
     State('Test', 'data'),
     State('save', 'data')])

def update_branch(reset_clicks, start_clicks, nd, yes, no, end, nodes_classes,Test, save):
    elements = []
    s2 = []
    e2 = []
    stylesheet3 = []
    outy = "Wellcome to matchmaking"
    outy2 = ""
    # pr = cProfile.Profile()
    # pr.enable()  # Start profiling
    positon=positon1
    positon_g1=positon3

    Test=[] if Test is None else Test

    if nodes_classes is None:
        nodes_classes = []

    if save is None:
        save = []


    button_clicked = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_clicked == 'Reset':
        Test=[]
        nodes, edges, df, stylesheet3 = create_nodes_and_edges(csd)
        elements = nodes + edges
        s2 = stylesheet_graphic
        e2 = elements2
        nodes_classes = []
        layout = standart_layout
        positon=positon1
        positon_g1=positon3
        save=[]
  

    elif button_clicked == "Start":
        node_id = 'T/I/R/A/J-00'
        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id)
        number = node_id.split("-")[1]
        outy = logic(0)
        outy2 = logic2(0)
        layout = game_layout
        positon=positon2
        positon_g1=positon4
        save=[]
        Test=[]

        


        e2, s2 = create_nodes_and_edges_updates(number, node_labels, icon_base64)
        elements = nodes + edges

        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id']!= node_id]
        Test.append({'source':node_id,'target':node_id})
        

       
###
    elif button_clicked == 'Yes':

 
        if not nodes_classes:
            node_id = 'T/I/R/A/J-00'
            Test.append({'source':node_id,'target':node_id})
        else:
           node_id = [node for node in nodes_classes if node['class'] == 'yes'][0]["id"]
           Test.append({'source':Test[-1]['target'],'target':node_id})

        


        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id)
        elements = nodes + edges
     
        

        number = node_id.split("-")[1]
        n=number[0]
        outy = logic(int(n))
        outy2 = logic2(int(n))
        layout = game_layout
        positon=positon2
        positon_g1=positon4
     


        e2, s2 = create_nodes_and_edges_updates(number, node_labels, icon_base64)

        
        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]

        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0] != "0"])
        else:
            pass


     
        if id!=[]:
         if id[0]==id[1] or id[1]=="0" or id[1]==0:
                 elements= [[sa for sa in save ][-1]]

        else:
             elements= [[sa for sa in save ][-1]]

   
 ####   

    elif button_clicked == 'No':
   
      
        if not nodes_classes:
            node_id = 'T/I/R/A/J-00'
            Test.append({'source':node_id,'target':node_id})
        else:
           node_id = [node for node in nodes_classes if node['class'] == 'no'][0]["id"]
           Test.append({'source':Test[-1]['target'],'target':node_id})



        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id)
        elements = nodes + edges
        number = node_id.split("-")[1]
        n=number[0]
        outy = logic(int(n))
        outy2 = logic2(int(n))
      
        layout = game_layout
        positon_g1=positon4
        positon=positon2    
        e2, s2 = create_nodes_and_edges_updates(number, node_labels, icon_base64)
   


        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]
        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0] != "0"])
        else:
            pass


     
        if id!=[]:
         if id[0]==id[1] or id[1]=="0" or id[1]==0:
                 elements= [[sa for sa in save ][-1]]

        else:
             elements= [[sa for sa in save ][-1]]



    elif button_clicked == 'cytoscape':
      

        
        node_id = nd['id']

        if not nodes_classes:
            node_id = 'T/I/R/A/J-00'
            Test.append({'source':node_id,'target':node_id})
        else:
           node_id = nd['id']
           Test.append({'source':Test[-1]['target'],'target':node_id})


        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id)
        elements = nodes + edges
        
        number = node_id.split("-")[1]
        outy = logic(int(number[0]))
        outy2 = logic2(int(number[0]))
        positon=positon2
        positon_g1=positon4

        e2, s2 = create_nodes_and_edges_updates(number, node_labels, icon_base64)

        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]
        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0] != "0"])
        else:
            pass


     
        if id!=[]:
         if id[0]==id[1] or id[1]=="0" or id[1]==0:
                 elements= [[sa for sa in save ][-1]]
                 positon_g1["zoom"]=1
        else:
             elements= [[sa for sa in save ][-1]]
             positon_g1["zoom"]=1

  
        layout = game_layout
       
   
        
    elif button_clicked == 'End':
        tasty = [f"source-{item['source']}_target-{item['target']}" for item in Test]
        return rebuild_and_highlight_graph(csd, tasty,elements2, nodes_classes, background_images, node_labels)
    

    else:
        nodes, edges,df, stylesheet3 = create_nodes_and_edges(csd)
        elements = nodes + edges
        s2 = stylesheet_graphic
        e2 = elements2
        layout = standart_layout
        positon_g1=positon3
        positon=positon1
        

    return layout,elements,stylesheet3, s2, e2, nodes_classes, outy, Test, outy2, positon, positon_g1, save




if __name__ == '__main__':
    app.run_server(debug=True)




    



