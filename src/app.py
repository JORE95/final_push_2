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

_combined_cache = {}
_cached_font = None
_icon_cache = {}

def get_cached_font(size):
    global _cached_font
    
    if _cached_font is None:
        font_url = "https://github.com/google/fonts/raw/main/ofl/carlito/Carlito-Regular.ttf"
        response = requests.get(font_url)
        font_data = BytesIO(response.content)
        _cached_font = ImageFont.truetype(font_data, size=size)
    
    return _cached_font

def icon(letter):

    if letter in _icon_cache:
        return _icon_cache[letter]
    
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
    
   
    text_position = ((size[0] - text_width) // 2, (size[1] - text_height * 2) // 2)

    draw.text(text_position, letter, fill="white", font=font)


    _icon_cache[letter] = image
    
    return image




# %%
def get_cached_icon(letter, i_con):
    if letter not in _icon_cache:
        _icon_cache[letter] = i_con(letter)
    return _icon_cache[letter]

def create_combined_image(letters, i_con):
    combined_w = []
    combined_h = []
    list_base64 = []

    for i in letters:
        if i in _combined_cache:
            list_base64.append(_combined_cache[i]['image_base64'])
            combined_w.append(_combined_cache[i]['width'])
            combined_h.append(_combined_cache[i]['height'])
            continue
        
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
            icon_image = get_cached_icon(letter, i_con)
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
        list_base64.append(img_str)
        
   
        _combined_cache[i] = {
            'image_base64': img_str,
            'width': combined_width,
            'height': combined_height
        }

    icon_base64 = dict(zip(letters, list_base64))
    return icon_base64, combined_w, combined_h






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
            'font-size': '0px'
                }
    },
    {
        'selector': 'edge:selected',
        'style': {
            'label': 'data(label)',
            'curve-style': 'bezier',
            'font-size': '40px',
            'color': 'white',
            'text-background-color': 'blue',
            'text-background-opacity': 1,
            'shape': 'ellipse',
            'text-background-padding': '40px',
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
            'target-arrow-color': 'red',
            'source-arrow-color': 'red',
            'width': 5

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


def process_nodes_and_edges(csd, node_id, status):
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

    stylesheet = stylesheet_basic + [
        {
            'selector': 'edge',
            'style': {

            'text-background-color': 'gray',
            'text-background-opacity': 1,
            'shape': 'ellipse',
            'width': 1,
            'text-background-padding': '20px',
            'text-border-color': 'black',
            'text-border-opacity': 1,
            'text-border-width': '1px',
            'line-color': 'gray',
            'font-size': '30px',
            'color': 'white'

            }
        }
    ]
 


    return new_nodes, matching_edges, stylesheet



def rebuild_and_highlight_graph(csd, Test, nodes_classes, background_images, node_labels):
    layout=standart_layout
    
    nodes, edges, df, stylesheet = create_nodes_and_edges(csd)
    icon_container = incon("off", 0)
    



    for edge in edges:
        if edge['classes'] in Test:
            edge['classes'] = 'highlighted'
        else:
            edge['classes'] = 'darken'
    

    elements = nodes + edges


    outy2 = "This is the end of the RA precision pathway"
    outy= "You’ve completed the therapeutic matchmaking journey. Please press 'End'  to view your path or 'Reset' to start over."
    stylesheet= stylesheet_basic
    layout=standart_layout

    positon_g1=positon3
    


    Test=[]
    save=[]

    
    return layout,elements,stylesheet,nodes_classes, outy, Test, outy2, positon_g1, save, icon_container

# %%
edges = []
nodes = []




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
server = app.server 






nodes, edges, df, stylesheet1 = create_nodes_and_edges(csd)


t1="Welcome!"
t2= "Please press start to begin matchmaking"

# %%
def logic(n):
    if n == 0:
        return "TNFi are contraindicated in moderate to severe heart failure (NYHA III/IV), and rituximab in severe heart failure (NYHA IV)."
    elif n == 1:
        return "JAKi should be prescribed only after careful consideration of benefit and risk in patients with current or history of ASCVD, VTE, and HZ."
    elif n == 2:
        return "Abatacept and JAKi might increase the risk of malignancies and might not be favored in patients with current or recent malignancies."
    elif n == 3:
        return "IL6i increase the risk for gastrointestinal perforations, especially in patients with current or history of diverticulitis; this potential risk has recently also been observed for JAKi."
    elif n == 5:
        return "Hypogammaglobulinemia may disfavor rituximab, and response to any planned vaccination may be limited after rituximab has been started."
    elif n == 4:
        return "Auto-antibody formation (like anti-nuclear antibodies, ANA, or double-stranded DNA antibodies, dsDNA) and demyelinating diseases (DMD) like Multiple sclerosis or Guillain-Barré syndrome have been observed in patients on TNFi therapy."
    elif n == 6:
        return "Conversely, specific extraarticular efficacy may positively select DMARDs: in RA-ILD, rituximab or abatacept may be favored over TNFi, IL6i and JAKi."
    elif n == 7:
        return  "You’ve completed the therapeutic matchmaking journey. Please press “End” to view your path or 'Reset' to start over."


    
def logic2(n):
    n=node_labels[n]
    return n


# %%



standart_layout={'name': 'preset'}
 
 
game_layout={
            'name': 'breadthfirst',
            'randomize': False,
            'gravity': 2,
            'idealEdgeLength': 2,
            'refresh': 20,
            'curved': 'straight',
            'move': False,
              
        }

w_=50
h_=50

qq=h_-20
s=50
controls = dbc.Card(
    [

        html.Div(
            [
                html.Div(
                    [
                        dbc.Button(
                            [  
                                html.I(className="fas fa-play-circle", style={'font-size': qq})  
                            ],
                            id="Start", color="primary", className="btn-lg",
                            style={
                                'width': w_,  
                                'height': h_,
                                'border-radius': '50%',  
                                'background-color': '#5A9BD4',  
                                'color': 'white',
                                'border': '3px solid #3A6FA4',  # Stronger border in darker tone
                                'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                                'transition': 'background-color 0.2s ease-in-out',
                                'display': 'flex',
                                'align-items': 'center',  # Center icon vertically
                                'justify-content': 'center',  # Center icon horizontally
                                'margin-bottom': '10px',  # Spacing between button and label
                            }
                        ),
                        html.P("Start", style={'text-align': 'center'})  
                    ],
                    style={'display': 'inline-block', 'text-align': 'center', 'margin': '10px'}
                ),
                html.Div(
                    [
                        dbc.Button(
                            [  # Icon only, no text
                                html.I(className="fas fa-sync", style={'font-size': qq})  
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
                                'margin-bottom': '10px',
                            }
                        ),
                        html.P("Reset", style={'text-align': 'center'})
                    ],
                    style={'display': 'inline-block', 'text-align': 'center', 'margin': '10px'}
                ),
                html.Div(
                    [
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
                                'border': '3px solid #4A8B4A',
                                'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'margin-bottom': '10px',
                                'transition': 'background-color 0.2s ease-in-out',
                            }
                        ),
                        html.P("Yes", style={'text-align': 'center'})
                    ],
                    style={'display': 'inline-block', 'text-align': 'center', 'margin': '10px'}
                ),
                html.Div(
                    [
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
                                'margin-bottom': '10px',
                                'transition': 'background-color 0.2s ease-in-out',
                            }
                        ),
                        html.P("No", style={'text-align': 'center'})
                    ],
                    style={'display': 'inline-block', 'text-align': 'center', 'margin': '10px'}
                ),
                html.Div(
                    [
                        dbc.Button(
                            [  # Icon only, no text
                                html.I(className="fas fa-stop-circle", style={'font-size': qq})  # Font Awesome Stop Circle Icon
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
                                'margin-bottom': '10px',
                            }
                        ),
                        html.P("End", style={'text-align': 'center'})
                    ],
                    style={'display': 'inline-block', 'text-align': 'center', 'margin': '10px'}
                ),
            ],
            style={
                'text-align': 'center',
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',  # Center the entire set of buttons
                'justify-content': 'center',  # Center vertically
            }
        ),
    ],
    style={
        'padding': '20px',
        'border-radius': '40px',  # Rounded for pill shape
        'background-color': 'rgba(255, 255, 255, 0.2)',  # Semi-transparent white background
        'backdrop-filter': 'blur(10px)',  # Frosted glass effect
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.3)',  # Stronger shadow for glassy effect
        'width': '80px',  # Adjust width to fit the circular buttons with labels
        'position': 'absolute',
        'top': '200px',
        'right': '20px',
        'zIndex': 3,
        'text-align': 'center',
        'color': '#000',  # Text color for contrast
        'font-family': '"San Francisco", "Segoe UI", sans-serif',  # Apple-like font family
    }
)


reset=html.Div([dbc.Button("Reset", id="Reset", color="primary",  style={'margin': 10, 'width': '150px'})])
start=html.Div([dbc.Button("Start", id="Start", color="primary", style={'margin': 10, 'width': '150px'})])

text_output = html.Div([html.P("Output: ", id="Outy")])
text_output2 = html.Div([html.H1("Output: ", id="Outy2")])

header = html.H1(
    "The RA Precision Pathway", 
    style={
        'textAlign': 'center', 
        'color': 'black', 
        'font-size': '50px', 
        'font-weight': '300',  
        'position': 'absolute',  
        'top': '10px',  
        'left': '50%', 
        'transform': 'translateX(-50%)', 
        'zIndex': 10 
    }
)

sub_header = html.H2(
    "Find the optimal therapeutic match for each patient", 
    style={
        'textAlign': 'center', 
        'color': 'black',
        'width': '100%',
        'font-size': '20px',
        'font-weight': '200',  
        'position': 'absolute',  
        'top': '70px',  
        'left': '50%', 
        'transform': 'translateX(-50%)', 
        'zIndex': 10 
    }
)



positon3 = {
    'overflow': 'visible',
    'width': '100%',
    'height': '80vh',
    'top': '10vh',  # Use vh for vertical positioning
    'position': 'fixed',
    'zIndex': 2,
    'right': '0%',
    'display': 'flex',
    'margin': 'auto',
    'left': '0%'
}

positon4 = {
    'overflow': 'hidden',
    'width': '100%',
    'height': '80vh',
    'position': 'absolute',
    'bottom': '50%',
    'right': '50%',
    'transform': 'translate(50%, 50%)',
    'zIndex': 2
}




cyto1 = cyto.Cytoscape(
    id='cytoscape',
    elements=nodes + edges,
    style=positon3,
    layout=standart_layout,
    maxZoom=0.4,
    minZoom=0.01,
    stylesheet=stylesheet1	
   
    )





# %% Graph 2
icon_list=["healthicons:heart-organ-outline", "healthicons:virus-alt-outline", "wi:cloud", "healthicons:colon-outline", "healthicons:y-outline", "healthicons:syringe-outline", "healthicons:blood-vessel-outline"]

background_images = [f"https://api.iconify.design/{icon}.svg" for icon in icon_list]

node_labels = [
    "Heart failure?", "ASCVD, VTE, HZ?", "Malignancy?", "Diverticulitis?", 
    "Autoantibodies, DMD?", "HG, vaccination?", "RA-ILD?", "This is the end of the RA precision pathway"
]

angles = [30, 45, 60, 75, 90, 105, 120]


colors = [
    "rgba(214, 39, 40, 0.5)",  # Heart failure? (Red)
    "rgba(44, 160, 44, 0.5)",  # SCVD, VTE, HZ? (Green)
    "rgba(255, 215, 0, 0.5)",  # Malignancy? (Yellow)
    "rgba(148, 103, 189, 0.5)",  # Diverticulitis? (Purple)
    "rgba(31, 119, 180, 0.5)",  # Autoantibodies, DMD? (Blue)
    "rgba(128, 128, 128, 0.5)",  # HG, vaccination? (Gray)
    "rgba(140, 86, 75, 0.5)",  # RA-ILD? (Brown)
    "rgba(31, 119, 180, 0.5)"   # End of story (Blue)
]

def generate_icon_position(angle, i, setting, number):
    if setting == "Start":
        radius = 300
        horizontal_stretch = 2
        vertical_stretch = 2.1
        rotation = 195
    else:
        radius = 400
        horizontal_stretch = 2.0
        vertical_stretch = 1.2
        rotation = 110
        number = -1

    rotated_angle = angle + rotation

    x = radius * horizontal_stretch * math.cos(math.radians(rotated_angle))
    y = radius * vertical_stretch * math.sin(math.radians(rotated_angle))

    position = {
        'position': 'absolute',
        'top': f'calc(50% + {y}px)' if setting != "Start" else f'calc(70% + {y}px)',  # Center vertically
        'left': f'calc(50% + {x}px)' if setting == "Start" else f'calc(40% + {x}px)',  # Center horizontally
        "background-image": f"url({background_images[i]})",
        "background-color": colors[i] if i == number else "rgba(255, 255, 255, 0.5)",
        "background-size": "contain",
        "background-position": "center",
        'border-style': 'solid' if i == number else 'dashed',
        'border-radius': '50%',
        'width': f'{110 if i == number else 80}px',  
        'height': f'{110 if i == number else 80}px',
        'border-width': f'{3 if i == number else 1.5}px',
        'zIndex': 0, 
        'align-items': 'center',
        'justify-content': 'center',
        'font-size': f'{20 if i == number else 12}px',
        'transform': 'translate(-50%, -50%)'  # Center the icon
    }

    return position

def incon(Signal, level):
    icons = [
        html.Div(
            style=generate_icon_position(angles[i], i, Signal, level),     
            id=f'icon-{i}', 
            children=[
                html.P(node_labels[i], style={
                    'text-align': 'center', 
                    'color': 'black', 
                    'font-size': f'{20 if i == level else 12}px',
                    'position': 'absolute',
                    'top': '100%',  
                    'width': '100%',  
                    'left': '50%',
                    'transform': 'translateX(-50%)',  
                    'margin-top': '2px'  
                })
            ]
        ) for i in range(len(angles))
    ]

    icon_container = html.Div(
        icons,
        style={
           'position': 'fixed',
            'left': '5%',  # Adjusted to ensure visibility
            'top': '8%',  # Adjusted to ensure visibility
            'zIndex': 0,  # Ensure icons are on top
            'width': '90%',  # Adjusted to fit within the screen
            'height': '80vh',
            'display': 'flex',
            'flex-direction': 'row',
            'align-items': 'center',
            'justify-content': 'center',  # Center the icons horizontally
        },
        className="icon2",
        id="icon-container"
    )
    return icon_container



# %% Jumbotron
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
 
            html.Div(
                [
                    dbc.Button("Learn more", color="primary", className="mx-2 d-inline-block"),
                    dbc.Button("Yes", id="Yes1", color="success", className="mx-2 d-inline-block"),
                    dbc.Button("No", id="No1", color="danger", className="mx-2 d-inline-block"),
                ],
                style={'text-align': 'left'}
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

icon_container = incon("Start", 0)
# %%
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            html.Div([header,sub_header,jumbotron, controls, cyto1, icon_container],	
            style={

                    'flex-direction': 'row',
                    'display': 'flex' 

                }),
            width=12
        )
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Store(id='nodes_classes'),
            dcc.Store(id='Test'),
            dcc.Store(id='save'),
            dcc.Store(id="position")


        ])
    ])
], fluid=True, className='dashboard-container')





@app.callback(
    [   
        Output('cytoscape', 'layout'),
        Output('cytoscape', 'elements'),
        Output('cytoscape', 'stylesheet'),
        Output('nodes_classes', 'data'),
        Output('Outy', 'children'),
        Output('Test', 'data'),
        Output('Outy2', 'children'),
        Output('cytoscape', 'style'),
        Output('save', 'data'),
        Output('icon-container', 'children')
      

    ],
    [
        Input('Reset', 'n_clicks'),
        Input("Start", 'n_clicks'),
        Input('cytoscape', 'tapNodeData'),
        Input('Yes', 'n_clicks'),
        Input('No', 'n_clicks'),
        Input('End', 'n_clicks'),
        Input('Yes1', 'n_clicks'),
        Input('No1', 'n_clicks')
    ],
    [State('nodes_classes', 'data'),
     State('Test', 'data'),
     State('save', 'data')])

def update_branch(reset_clicks, start_clicks, nd, yes, no, end,yes1, no1, nodes_classes,Test, save):
    elements = []
    s2 = []
    e2 = []
    stylesheet3 = []
    outy = t2
    outy2 = t1
    icon_container = incon("off", 0)
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
        nodes_classes = []
        layout = standart_layout
        positon_g1=positon3
        save=[]
        icon_container = incon("off", 0)
  

    elif button_clicked == "Start":
        node_id = 'T/I/R/A/J-00'
        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id, "yes")
        number = node_id.split("-")[1]
        outy = logic(0)
        outy2 = logic2(0)
        layout = game_layout
        positon_g1=positon4
        save=[]
        Test=[]
        icon_container = incon("Start", 0)


        elements = nodes + edges

        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id']!= node_id]
        Test.append({'source':node_id,'target':node_id})
        

       
###
    elif button_clicked == 'Yes' or button_clicked == 'Yes1':


 
        if not nodes_classes:
            node_id = 'T/I/R/A/J-00'
            Test.append({'source':node_id,'target':node_id})
        else:
           node_id = [node for node in nodes_classes if node['class'] == 'yes'][0]["id"]
           Test.append({'source':Test[-1]['target'],'target':node_id})

   

        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id, "independend")
        elements = nodes + edges
   

     
        

        number = node_id.split("-")[1]
        n=number[0]
        outy = logic(int(n))
        outy2 = logic2(int(n))
        layout = game_layout
        positon_g1=positon4
        cube=(int(str(number)[0]))
        icon_container = incon("Start", cube)
     


        
        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]

        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0]])
        else:
            pass


     
        if id!=[]:
         if id[0]==id[1] or id[1]=="0" or id[1]==0:
                 elements= [[sa for sa in save ][-1]]

        else:
             elements= [[sa for sa in save ][-1]]

   
 ####   

    elif button_clicked == 'No' or button_clicked == 'No1':
        
        if not nodes_classes:
            node_id = 'T/I/R/A/J-00'
            Test.append({'source':node_id,'target':node_id})
        else:
           node_id = [node for node in nodes_classes if node['class'] == 'no'][0]["id"]
           Test.append({'source':Test[-1]['target'],'target':node_id})


        print(node_id)
        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id, "no")
        elements = nodes + edges
        number = node_id.split("-")[1]
        n=number[0]
        outy = logic(int(n))
        outy2 = logic2(int(n))  
        layout = game_layout
        positon_g1=positon4
        cube=(int(str(number)[0]))
        icon_container = incon("Start", cube)
     
   


        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]
        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0]])
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


        nodes, edges, stylesheet3 = process_nodes_and_edges(csd, node_id, "independend")
        elements = nodes + edges
        
        number = node_id.split("-")[1]
        outy = logic(int(number[0]))
        outy2 = logic2(int(number[0]))
        positon_g1=positon4
        cube=(int(str(number)[0]))
        icon_container = incon("Start", cube)


        nodes_classes = [{'id': node['data']['id'], 'class': node['classes']} for node in nodes if node['data']['id'] != node_id]
        id=[node['data']['id'].split("-")[0] for node in nodes if node['data']['id'] != node_id]
        if id!=[]:
            save.extend([node for node in nodes if node['data']['id'].split("-")[0]])
        else:
            pass

        layout = game_layout
       
   
        
    elif button_clicked == 'End':
        tasty = [f"source-{item['source']}_target-{item['target']}" for item in Test]
        save=[]
        Test=[]
        icon_container = incon("off", 0)
        return rebuild_and_highlight_graph(csd, tasty, nodes_classes, background_images, node_labels)
    

    else:
        nodes, edges,df, stylesheet3 = create_nodes_and_edges(csd)
        elements = nodes + edges
        layout = standart_layout
        positon_g1=positon3


        

    return layout,elements,stylesheet3,nodes_classes, outy, Test, outy2, positon_g1, save, icon_container




if __name__ == '__main__':
    app.run_server(debug=True)




    



