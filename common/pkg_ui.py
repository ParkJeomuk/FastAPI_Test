# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import dash
import dash_bootstrap_components as dbc
import dash_core_components      as dcc
import dash_html_components      as html

import dash_admin_components as dac

from dash.dependencies import Input, Output, State
from dash.exceptions   import PreventUpdate

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
import plotly.graph_objs as obj