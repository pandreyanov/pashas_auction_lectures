import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

options_scatter = {'s':15, 'color':'white', 'edgecolor':'black'}
options_hist = {'color':'white', 'bins':25, 'edgecolor':'black'}

def publish(fig):
    fig.set_size_inches(5, 6)
    fig.set_dpi(150)
    plt.tight_layout()