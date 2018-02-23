# Functions used in tutorials

import numpy as np
import matplotlib


def normalize_array(v):
    # Normalize v such that sum(v) = 3
    norm_factor = np.linalg.norm(v) / np.sqrt(3)
    return v / norm_factor

def hex2rgb(h):
    # Convert hex to RGB
    # https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    return np.array([int(h[i:i+2],16) for i in [0,2,4]])

def colorgrad(color1, color2, n):
    """
    Creates color gradient from `color1` to `color2` with RGB triplets in `n` intervals
    Input:
    | color{1,2} <list, array, str>: Colors can be entered as array-like, matplotlib color, or hex (uppercase)
    """

    # String -> #Hex
    c_dict_hex = matplotlib.colors.cnames
    cnames = c_dict_hex.keys()
    chex = c_dict_hex.values()
    # Dictionary for string -> RGB
    c_dict_rgb = {k: matplotlib.colors.to_rgb(v) for k, v in c_dict_hex.items()}

    # If list, convert to array
    if type(color1) == list or type(color1) == tuple:
        color1 = np.array(color1)
        if color1.sum() > 3:
            color1 = normalize_array(color1)
    if type(color2) == list or type(color2) == tuple:
        color2 = np.array(color2)
        if color2.sum() > 3:
            color2 = normalize_array(color2)

    # If string, convert to array
    if type(color1) == str:
        # If matplotlib color name
        if color1 in cnames:
            color1 = np.array(c_dict_rgb[color1])
        # If hex
        elif color1[0] == '#':
            color1 = color1.upper()
            if color1 in chex:
                color1 = hex2rgb(color1)
        else:
            print('"%s" is not an accepted color' % color1)
            return
    if type(color2) == str:
        if color2 in cnames:
            color2 = np.array(c_dict_rgb[color2])
        elif color2[0] == '#':
            color2 = color2.upper()
            if color2 in chex:
                color2 = hex2rgb(color2)
        else:
            print('"%s" is not an accepted color' % color2)
            return
    # Compute gradient
    diff = color2 - color1
    grad = diff * np.linspace(0, 1, n).reshape(-1, 1) + color1
    return grad