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
t2= "To find the optimal therapeutic match for each patient press 'Start'"

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

controls = html.Div(
    [
        html.Div(
            [
                # Start Button
                html.Div(
                    [
                        dbc.Button(
                            html.I(className="fas fa-play-circle", style={'font-size': '32px'}),
                            id="Start",
                            color="primary",
                            style={
                                'width': '70px',
                                'height': '70px',
                                'border-radius': '15px',
                                'background': 'linear-gradient(135deg, #5BC0BE, #0B4F6C)',  # Teal to dark blue
                                'color': 'white',
                                'border': '1px solid #0B4F6C',
                                'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'transition': 'transform 0.2s, box-shadow 0.2s',
                            },
                            n_clicks=0
                        ),
                        html.P("Start", style={
                            'text-align': 'center',
                            'margin-top': '8px',
                            'color': '#0B4F6C',
                            'font-weight': 'bold'
                        })
                    ],
                    style={'text-align': 'center', 'margin': '10px'}
                ),
                # Reset Button
                html.Div(
                    [
                        dbc.Button(
                            html.I(className="fas fa-sync-alt", style={'font-size': '32px'}),
                            id="Reset",
                            color="secondary",
                            style={
                                'width': '70px',
                                'height': '70px',
                                'border-radius': '15px',
                                'background': 'linear-gradient(135deg, #A9BCD0, #6C7A89)',  # Light to medium gray
                                'color': 'white',
                                'border': '1px solid #6C7A89',
                                'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'transition': 'transform 0.2s, box-shadow 0.2s',
                            },
                            n_clicks=0
                        ),
                        html.P("Reset", style={
                            'text-align': 'center',
                            'margin-top': '8px',
                            'color': '#6C7A89',
                            'font-weight': 'bold'
                        })
                    ],
                    style={'text-align': 'center', 'margin': '10px'}
                ),
                # Yes Button
                html.Div(
                    [
                        dbc.Button(
                            html.I(className="fas fa-check-circle", style={'font-size': '32px'}),
                            id="Yes",
                            color="success",
                            style={
                                'width': '70px',
                                'height': '70px',
                                'border-radius': '15px',
                                'background': 'linear-gradient(135deg, #90BE6D, #43AA8B)',  # Light to medium green
                                'color': 'white',
                                'border': '1px solid #43AA8B',
                                'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'transition': 'transform 0.2s, box-shadow 0.2s',
                            },
                            n_clicks=0
                        ),
                        html.P("Yes", style={
                            'text-align': 'center',
                            'margin-top': '8px',
                            'color': '#43AA8B',
                            'font-weight': 'bold'
                        })
                    ],
                    style={'text-align': 'center', 'margin': '10px'}
                ),
                # No Button
                html.Div(
                    [
                        dbc.Button(
                            html.I(className="fas fa-times-circle", style={'font-size': '32px'}),
                            id="No",
                            color="danger",
                            style={
                                'width': '70px',
                                'height': '70px',
                                'border-radius': '15px',
                                'background': 'linear-gradient(135deg, #F94144, #9B2226)',  # Light to dark red
                                'color': 'white',
                                'border': '1px solid #9B2226',
                                'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'transition': 'transform 0.2s, box-shadow 0.2s',
                            },
                            n_clicks=0
                        ),
                        html.P("No", style={
                            'text-align': 'center',
                            'margin-top': '8px',
                            'color': '#9B2226',
                            'font-weight': 'bold'
                        })
                    ],
                    style={'text-align': 'center', 'margin': '10px'}
                ),
                # End Button
                html.Div(
                    [
                        dbc.Button(
                            html.I(className="fas fa-stop-circle", style={'font-size': '32px'}),
                            id="End",
                            color="dark",
                            style={
                                'width': '70px',
                                'height': '70px',
                                'border-radius': '15px',
                                'background': 'linear-gradient(135deg, #577590, #0B4F6C)',  # Medium to dark blue
                                'color': 'white',
                                'border': '1px solid #0B4F6C',
                                'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'transition': 'transform 0.2s, box-shadow 0.2s',
                            },
                            n_clicks=0
                        ),
                        html.P("End", style={
                            'text-align': 'center',
                            'margin-top': '8px',
                            'color': '#0B4F6C',
                            'font-weight': 'bold'
                        })
                    ],
                    style={'text-align': 'center', 'margin': '10px'}
                ),
            ],
            style={
                'display': 'flex',
                'flex-direction': 'row',
                'justify-content': 'center',
                'align-items': 'center',
                'flex-wrap': 'wrap',
            }
        ),
    ],
    style={
        'background-color': '#F0F4F8',
        'padding': '20px',
        'border-radius': '15px',
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.1)',
        'margin-top': '20px',
        'margin-bottom': '20px',
        'width': '100%',
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
        'width': '100%',
        'color': 'black', 
        'font-size': '50px', 
        'font-weight': '300',
        'margin-top': '10px',  # Added margin for spacing
    }
)

# Updated Sub-Header Component
sub_header = html.H2(
    "Find the optimal therapeutic match for each patient", 
    style={
        'textAlign': 'center', 
        'color': 'black',
        'width': '100%',
        'font-size': '20px',
        'font-weight': '200',
        'margin-top': '5px',  # Added margin for spacing
    }
)

# Updated Style for cyto1
positon3 = {
    'width': '100%',
    'height': '60vh',
    'zIndex': 1,
    'margin-top': '20px',
    'margin-bottom': '20px',
    'maxZoom': 0.25,
    'minZoom': 0.01
}

# Cytoscape Component
cyto1 = cyto.Cytoscape(
    id='cytoscape',
    elements=nodes + edges,
    style=positon3,
    layout=standart_layout,
    maxZoom=0.4,
    minZoom=0.01,
    stylesheet=stylesheet1
)



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
        # Removed "position": "absolute" to keep the jumbotron in the normal flow
        'width': '100%',
        'max-width': '800px',
        'margin': '20px auto',  # Centers the jumbotron and adds vertical spacing
        'border': '1px solid #e0e0e0',
        'border-radius': '12px',
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.15)',
        'padding': '40px',
        'background-color': '#f7f7f7',
    },
    className="p-3 bg-body-secondary rounded-3"
)







# %% Graph 2
icon_list = [
    "healthicons:heart-organ-outline", "healthicons:virus-alt-outline", "wi:cloud", 
    "healthicons:colon-outline", "healthicons:y-outline", "healthicons:syringe-outline", 
    "healthicons:blood-vessel-outline"
]

background_images = [f"https://api.iconify.design/{icon}.svg" for icon in icon_list]

node_labels = [
    "Heart failure?", "ASCVD, VTE, HZ?", "Malignancy?", "Diverticulitis?", 
    "Autoantibodies, DMD?", "HG, vaccination?", "RA-ILD?"
]

colors = [
    "#5BC0BE",  # Teal
    "#90BE6D",  # Light Green
    "#F9C74F",  # Yellow
    "#F94144",  # Red
    "#577590",  # Dark Blue
    "#F3722C",  # Orange
    "#43AA8B",  # Green
]

def generate_icon_position(i, is_active):
    return {
        "background-image": f"url({background_images[i]})",
        "background-color": colors[i] if is_active else "#FFFFFF",
        "background-size": "contain",
        "background-position": "center",
        'border-radius': '15px',  
        'width': '50px',  
        'height': '50px',
        'border-width': '1px',
        'border-style': 'solid',
        'border-color': colors[i],
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'center',
        'margin-right': '15px',  
        'transition': 'background-color 0.2s ease', 
    }

def generate_menu_item(i, is_active):
    return html.Div(
        id=f'icon-item-{i}',  
        n_clicks=0, 
        style={
            'display': 'flex', 
            'align-items': 'center',  
            'padding': '10px',  
            'cursor': 'pointer',
            'width': '100%',
            'margin-bottom': '10px',
            'background-color': '#F0F4F8' if is_active else '#FFFFFF',  
            'border-radius': '15px',
            'border': f'1px solid {colors[i]}',  # Border color matches the icon color
            'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
            'transition': 'background-color 0.2s ease, border 0.2s ease',  
            'outline': 'none',  
        },
        children=[
            html.Div(
                style=generate_icon_position(i, is_active),
                id=f'icon-{i}'
            ),
            html.P(
                node_labels[i], 
                style={
                    'font-size': '16px',
                    'color': '#0B4F6C',  # Dark blue text for consistency
                    'margin': '0',
                    'text-align': 'left',
                    'flex-grow': '1',
                    'font-weight': 'bold',
                }
            )
        ]
    )

def incon(Signal, level):
    assert len(background_images) == len(node_labels), "background_images and node_labels must be of the same length."

    icons = [
        generate_menu_item(i, is_active=(i == level)) for i in range(len(node_labels))
    ]

    icon_container = html.Div(
        icons,

        className="menu-container",
        id="icon-container"
    )
    return icon_container







# %% Jumbotron
# Updated Jumbotron Component aligned in the same column
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
        'width': '100%',
        'max-width': '800px',


        "position": "relative",
        'margin': '20px auto',  # Center the jumbotron horizontally
        'border': '1px solid #e0e0e0',
        'border-radius': '12px',
        'box-shadow': '0 6px 12px rgba(0, 0, 0, 0.15)',
        'padding': '20px',
        'background-color': '#f7f7f7',
        "bottom":"10px"
    },
    className="p-3 bg-body-secondary rounded-3"
)


icon_container = incon("Start", 0)
# %%

app.layout = dbc.Container([
    dbc.Row([
        # Sidebar Column
        dbc.Col(
            html.Div(
                [
                    icon_container,
                    controls
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'height': '100vh',
                    'overflow-y': 'auto',
                }
            ),
            width=2,
            className="icon-column",
            style={
                'padding': '10px',
                'background-color': '#f8f9fa',
            }
        ),
        # Main Content Column
        dbc.Col(
            [
                dbc.Row(
                    dbc.Col(
                        header,
                        width=12,
                        style={
                            'textAlign': 'center',
                            'margin-bottom': '10px',
                        }
                    )
                ),
                # Second Row: Sub-header (H2)
                dbc.Row(
                    dbc.Col(
                        sub_header,
                        width=12,
                        style={
                            'textAlign': 'center',
                            'margin-bottom': '10px',
                        }
                    )
                ),
                # Third Row: Cytoscape Component
                dbc.Row(
                    dbc.Col(
                        cyto1,
                        width=12,
                        style={
                            'margin-bottom': '10px',
                        }
                    )
                ),
                # Fourth Row: Jumbotron
                dbc.Row(
                    dbc.Col(
                        jumbotron,
                        width=12,
                        style={
                            'margin-bottom': '10px',
                        }
                    )
                ),
            ],
            width=10,
            style={
                'overflow-y': 'auto',
                'padding': '20px',
                'background-color': '#ffffff',
                'border-radius': '8px',
                'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.1)',
            }
        ),
    ], style={
        'height': '100vh',
        'margin': '0',
    }),
    # Second Row: Hidden Stores for Data
    dbc.Row([
        dbc.Col([
            dcc.Store(id='nodes_classes'),
            dcc.Store(id='Test'),
            dcc.Store(id='save'),
            dcc.Store(id="position")
        ])
    ])
], fluid=True, className='dashboard-container', style={'border-radius': '8px', 'overflow': 'hidden'})






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




    



