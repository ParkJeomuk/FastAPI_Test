from dash.dependencies import Input, Output, State
from apps import app

import dash
from dash.exceptions import PreventUpdate

from utils.constants import MENU_ITEMS
import datetime
# =============================================================================
# Callbacks
# =============================================================================
# MENU_ITEMS = ("basic_cards", "social_cards", "tab_cards", "basic_boxes", "value_boxes",)# "gallery_1", "tab_gallery_2")
# MENU_ITEMS[1]
# MENU_ITEMS.index(input_id.split( '_', maxsplit=1)[1])

def activate(input_id, 
             dash_pages,basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, tab_gallery_2):
    menu_n = len(MENU_ITEMS)
    menu_status = [ False for i in range(menu_n)]
    try:    
        menu_idx = MENU_ITEMS.index(input_id.split( '_', maxsplit=1)[1])    
        menu_status[menu_idx]=True
    except:
        pass
    return menu_status

@app.callback(
    [Output(f"content_{menu}", "active") for menu in MENU_ITEMS],
    [ Input(f'menu_{menu}', 'n_clicks')  for menu in MENU_ITEMS] )
def activate_page_content(dash_pages, basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, tab_gallery_2):
    ctx = dash.callback_context # Callback context to recognize which input has been triggered
    # Get id of input which triggered callback  
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    return activate(input_id, 
                    dash_pages, basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, tab_gallery_2)

@app.callback(
    Output('mybread', 'text'),
    [ Input(f"menu_{menu}", "n_clicks") for menu in MENU_ITEMS],
    [ State(f"menu_{menu}", "label")    for menu in MENU_ITEMS] )
def update_breadcrumbs( nClick1, nClick2, nClick3, nClick4, nClick5, nClick6, nClick7,nClick8,
    dash_pages, basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, gallery_2): 
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0].split('_', maxsplit=1)[1]
    return eval(input_id)


