from dash import dash, html, dcc, Input, Output, State, MATCH, ALL, dash_table, ctx, callback_context
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from dash import dash_table
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import dash
import sys
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display, Image as IPImage
import base64
import io
import time




def icon(letter):
    size = (100, 100)
    colors = {
        "A": "green", "B": "blue", "C": "black", "D": "orange", "E": "purple", "F": "yellow", 
        "G": "pink", "H": "brown", "I": "pink", "J": "orange", "K": "cyan", "L": "magenta", 
        "M": "lime", "N": "teal", "O": "indigo", "P": "maroon", "Q": "navy", "R": "turquoise", 
        "S": "aqua", "T": "red", "U": "tan", "V": "turquoise", "W": "violet", "X": "gold", 
        "Y": "khaki", "Z": "lavender"
    }
    color = colors[letter]
    image = Image.new("RGBA", size, (255, 255, 255, 0))  
    draw = ImageDraw.Draw(image)
    corner_radius = 15
    
    draw.rounded_rectangle([(1, 1), (size[0]-1, size[1]-1)], radius=corner_radius, fill=color)
    font = ImageFont.truetype("arial.ttf", 60)
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    ascent, descent = font.getmetrics()
    text_position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2 - descent // 2)
    draw.text(text_position, letter, fill="white", font=font)
    return image


def create_combined_image(letters, i_con):
    combined_w = []
    combined_h = []
    list = []
    for i in letters:
        yy = i.split('-')[0]
        yy = yy.split('/')  
        num_icons = len(yy)
        icon_size = (100, 100)
        
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


def create_nodes_and_edges(Link):

    ed = pd.read_excel(Link)
    df = pd.DataFrame(ed)
    df["Level_R"] = df["Level"] - 1
    df["Level_R2"] = df["Level2"] * 0

    df["Roote"] = df["Roote"] + "-" + df["Level_R"].astype(str) + df["Level_R2"].astype(str)
    df["Connection"] = df["Connection"] + "-" + df["Level"].astype(str) + df["Level2"].astype(str)


    nodes1 = [i for i in df["Roote"]]
    nodes2 = [i for i in df["Connection"]]
    nodes = nodes1 + nodes2


    edges = [{'data': {'source': df["Roote"][i], 'target': df["Connection"][i]}} for i in range(len(df))]


    icon_base64, w, h = create_combined_image(nodes, icon)


    nodes = [
        {
            'data': {'id': nodes[i]},
            'style': {
                'background-image': f'data:image/png;base64,{icon_base64[nodes[i]]}',
                'background-clip': 'none',
                'background-opacity': 0,
                'width': w[i],
                'height': h[i],
                'shape': 'rounder-rectangle',
                'radius': 10,
                'lockAspect': True
            }
        }
        for i in range(len(nodes))
    ]
    return nodes, edges



def cut_nodes_and_edges(Link, cut):

    ed = pd.read_excel(Link)
    df = pd.DataFrame(ed)
    df=df.iloc[:cut]
    df["Level_R"] = df["Level"] - 1
    df["Level_R2"] = df["Level2"] * 0

    df["Roote"] = df["Roote"] + "-" + df["Level_R"].astype(str) + df["Level_R2"].astype(str)
    df["Connection"] = df["Connection"] + "-" + df["Level"].astype(str) + df["Level2"].astype(str)


    nodes1 = [i for i in df["Roote"]]
    nodes2 = [i for i in df["Connection"]]
    nodes = nodes1 + nodes2


    edges = [{'data': {'source': df["Roote"][i], 'target': df["Connection"][i]}} for i in range(len(df))]


    icon_base64, w, h = create_combined_image(nodes, icon)


    nodes = [
        {
            'data': {'id': nodes[i]},
            'style': {
                'background-image': f'data:image/png;base64,{icon_base64[nodes[i]]}',
                'background-clip': 'none',
                'background-opacity': 0,
                'width': w[i],
                'height': h[i],
                'shape': 'rounder-rectangle',
                'radius': 10,
                'lockAspect': True
            }
        }
        for i in range(len(nodes))
    ]
    return nodes, edges



def process_nodes_and_edges(Link, node_id):
    nodes, edges = create_nodes_and_edges(Link)

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

    matching_edges = [edge for edge in edges if edge['data']['source'] == nodes[x]['data']['id']]


    new_nodes = list(set([matching_edges[i]['data']['target'] for i in range(len(matching_edges))] + [nodes[x]['data']['id']]))

    icon_base64, w, h = create_combined_image(new_nodes, icon)

    

    new_nodes = [
        {
            'data': {'id': new_nodes[i]},
            'style': {
                'background-image': f'data:image/png;base64,{icon_base64[new_nodes[i]]}',
                'background-clip': 'none',
                'background-opacity': 0,
                'width': w[i],
                'height': h[i],
                'shape': 'rounder-rectangle',
                'radius': 10,
                'lockAspect': True
            }
        }
        for i in range(len(new_nodes))
    ]
    return new_nodes, matching_edges








edges = []
nodes = []

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
Link = "C:/Users/jrech/OneDrive/Desktop/Privat/Website/20240819_input.xlsx"

nodes, edges = create_nodes_and_edges(Link)

Cyto = cyto.Cytoscape(
    id='cytoscape',
    elements=nodes + edges,
    style={'width': '100%', 'height': '1000px'},
    layout={'name': 'cose', 'randomize': False, 'gravity': 2, 'idealEdgeLength': 200, 'refresh': 20,
            'nodeRepulsion': 40000000, 'edgeElasticity': 100, 'Temperature': 0, 'curved': 'straight', 'zoom':0.0001}
)

header = html.H1("Welcome to the Network Graph")

options1 = [
    {'label': 'Cose', 'value': 'cose'},
    {'label': 'Circle', 'value': 'circle'},
    {'label': 'Concentric', 'value': 'concentric'},
    {'label': 'Grid', 'value': 'grid'},
    {'label': 'Random', 'value': 'random'},
    {'label': 'Breadthfirst', 'value': 'breadthfirst'},
    {'label': 'Preset', 'value': 'preset'}
]

option2 = [{'label': 'Yes', 'value': 'True'}, {'label': 'No', 'value': 'False'}]

controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("layout"),
                dcc.Dropdown(
                    id="x-variable",
                    options=options1,
                    value='cose'
                )
            ]
        ),

        html.Div([dbc.Button("Reset", id="Reset", color="primary")]),
        
        html.Div([dbc.Button("Start", id="Start", color="primary")]),

        html.Div(
            [
                dbc.Label("Cardiac issues"),
                dcc.Dropdown(
                    id="level2",
                    options=[{'label': 'Yes', 'value': 'True'}, {'label': 'No', 'value': 'False'}],
                    value='True'
                )
            ]
        ),
        html.Div(
            [
                dbc.Label("Cardiac issues"),
                dcc.Dropdown(
                    id="level3",
                    options=[{'label': 'Yes', 'value': 'True'}, {'label': 'No', 'value': 'False'}],
                    value='True'
                )
            ]
        ),
        html.Div(
            [
                dbc.Label("Cardiac issues"),
                dcc.Dropdown(
                    id="level4",
                    options=[{'label': 'Yes', 'value': 'True'}, {'label': 'No', 'value': 'False'}],
                    value='True'
                )
            ]
        )
    ])

app.layout = dbc.Container([
    dbc.Row([dbc.Col([header], width=12, style={'textAlign': 'center'})]),
    dbc.Row([
        dbc.Col([controls], width=3, style={'padding': '20px'}),
        dbc.Col([Cyto], width=9),
    ])
], fluid=True, style={'height': '100vh', 'width': '100vw', 'padding': '0'})





@app.callback(
    Output('cytoscape', 'elements'),
    Input('Reset', 'n_clicks'),
    Input("Start", "n_clicks"),
    Input('level2', 'value'),
    Input('cytoscape', 'tapNodeData')

)
def update_branch(_1_, _2_, l1, nd):
    button_clicked = ctx.triggered_id
    if button_clicked == 'Reset':
            nodes, edges = create_nodes_and_edges(Link)
    elif button_clicked =="Start":
            node_id='T/I/R/A/J-00'
            nodes, edges = process_nodes_and_edges(Link, node_id)
            

    elif button_clicked == 'cytoscape':
            node_id = nd['id']
            nodes, edges = process_nodes_and_edges(Link, node_id)
   
    else:
            nodes, edges = create_nodes_and_edges(Link)
   

    return nodes + edges


@app.callback(
    Output('cytoscape', 'layout'),
    Input('x-variable', 'value'),
    Input('cytoscape', 'tapNodeData'),
    Input('Reset', 'n_clicks'),
    Input("Start", "n_clicks")
)


def update_layout(layout,nd, _1_, _2_):
    clicked = ctx.triggered_id

    if clicked == 'cytoscape':
        layout = {
            'name': 'breadthfirst',
            'randomize': False,
            'gravity': 2,
            'idealEdgeLength': 2,
            'refresh': 20,
            'nodeRepulsion': 400,
            'edgeElasticity': 10,
            'Temperature': 0,
            'curved': 'straight'
        }
    elif clicked == 'Start':
        layout = {
            'name': 'breadthfirst',
            'randomize': False,
            'gravity': 2,
            'idealEdgeLength': 20,
            'refresh': 20,
            'nodeRepulsion': 4000,
            'edgeElasticity': 10,
            'Temperature': 0,
            'curved': 'straight'
        }
    elif clicked == 'Reset':

        for i in range(100):

         
            layout = { 
            'name': 'cose',
            'randomize': False,
            'gravity': [i],
            'idealEdgeLength': 200,
            'refresh': 20,
            'nodeRepulsion': 40000000,
            'edgeElasticity': 100,
            'Temperature': 0,
            'curved': 'curved',
            'zoom': 0.0001,
            'animate': True}

    else:
        layout = {
            'name': layout,
            'randomize': False,
            'gravity': 2,
            'idealEdgeLength': 200,
            'refresh': 20,
            'nodeRepulsion': 40000000,
            'edgeElasticity': 100,
            'Temperature': 0,
            'curved': 'curved',
            'zoom': 0.0001,
            'animate': True
        }

    return layout


if __name__ == '__main__':
    app.run_server(debug=True)


