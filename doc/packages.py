# Pfad anpassen
import os

os.chdir(os.path.join(os.getcwd(), ".."))

# Packages
from engicalc import *
import engicalc.units as un
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from shapely.geometry import Polygon

# plotstyle
from config.style.plotstyle import set_engineering_style  # Plotstyle
from config.style.plotstyle import apply_scientific_notation

set_engineering_style()
