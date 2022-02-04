# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

### Required libraries ------------------------------------------
import numpy as np
import os
import pandas as pd
from pandas import Series
# column 다 보이기
pd.set_option('display.max_columns', None)
#(참고) warning 제거를 위한 코드
#np.seterr(divide='ignore', invalid='ignore')

### Visualization libraries -------------------------------------
import plotly.express as px

import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')

import matplotlib.pyplot as plt
# % matplotlib inline
plt.rcParams["figure.figsize"] = (7,6)  # 크기 (inch)
plt.rcParams['axes.grid'] = True        # 격자선 여부
plt.rcParams['lines.linewidth'] = 2     # 선의 두께
plt.rcParams['lines.color'] = 'red'     # 선의 색깔

### Etc. libraries ----------------------------------------------
import imp
import math
from datetime import datetime    # To access datetime
# To print multiple output in a cell --------------------------
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

### *************************************************************
import sklearn


### for test
def xxx(var='good'):
    print(var+"dumb dumb!!!")