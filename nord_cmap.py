import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


colors = ["#5E81AC", "#81A1C1", "#88C0D0", "#8FBCBB","#A3BE8C", "#EBCB8B", "#D08770", "#BF616A"]
cmap1 = LinearSegmentedColormap.from_list("nord_cmap", colors)
mpl.colormaps.register(cmap = cmap1)


def color_list(num_color) : 
    
    """ return a list of norded prepared colors """
    
    return cmap1(np.linspace(0,1,num_color))