import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib as mpl

options_scatter = {'s':15, 'color':'white', 'edgecolor':'black'}
options_hist = {'color':'white', 'bins':25, 'edgecolor':'black'}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

def publish(entry):
    if type(entry) == mpl.figure.Figure:
        entry.set_size_inches(5, 6)
        entry.set_dpi(150)
        plt.tight_layout()
        
    if type(entry) == pd.core.frame.DataFrame:
        print(entry.to_markdown(tablefmt="grid"))