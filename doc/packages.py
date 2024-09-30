# Pfad anpassen
import os

os.chdir(os.path.join(os.getcwd(), ".."))

# Packages
from engicalc import *
from engicalc.units import *
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# plotstyle
from config.style.plotstyle import set_engineering_style  # Plotstyle

set_engineering_style()
