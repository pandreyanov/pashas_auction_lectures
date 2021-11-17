import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl

options_scatter = {'s':15, 'color':'white', 'edgecolor':'black'}
options_hist = {'color':'white', 'bins':25, 'edgecolor':'black'}

plt.style.use('ggplot')
sb.set_style('white')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

def publish(entry):
    if type(entry) == mpl.figure.Figure:
        entry.set_size_inches(8, 8)
        entry.set_dpi(600)
        plt.tight_layout()
        
    if type(entry) == pd.core.frame.DataFrame:
        print(entry.to_markdown(tablefmt="grid"))