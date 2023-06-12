import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

from pyvis.network import Network
from IPython.core.display import display, HTML

import streamlit as st
import streamlit.components.v1 as components

df = pd.read_csv("data/hero-network.csv", usecols = [ "hero" , "hero_connection"])
df = df.sort_values(by="hero", ascending=False).head(3000) 
print(df)

g1 = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", notebook=True, cdn_resources='remote',directed = True, select_menu=True)
g1.barnes_hut()

sources = df['hero']
targets = df['hero_connection']

edge_data = zip(sources, targets)

for e in edge_data:
                src = e[0]
                dst = e[1]

                g1.add_node(src, src, title=src)
                g1.add_node(dst, dst, title=dst)
                g1.add_edge(src, dst, value=1)

neighbor_map = g1.get_adj_list()
for node in g1.nodes:
                node["value"] = len(neighbor_map[node["id"]])

g1.show_buttons(filter_=['physics'])
g1.show('hero_network.html')
display(HTML('hero_network.html'))


st.title("Atividade Pyvis e Streamlit")
st.subheader("Network referente dataset de encontros entre personagens da Marvel nas HQS")
st.text("")

HtmlFile = open("hero_network.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 1200,width=1000)

G=nx.Graph()
for index,edge in df.iterrows():
  G.add_edge(edge['hero'], edge['hero_connection'])

print(nx.degree_centrality(G))