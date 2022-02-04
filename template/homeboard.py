#from settings.common_ui    import *
from common.pkg_ui import *

# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))) )

###############################################################################
#                                MAIN                                         #
###############################################################################
from common      import config , contents, style

from template.mytest       import test_tab
from template.cards_basic  import cards_tab

# from template.cards_social import social_cards_tab
# from template.cards_tab    import tab_cards_tab
# from template.basic_boxes  import basic_boxes_tab
# from template.value_boxes  import value_boxes_tab

# from template.cards_tab    import text_1, text_2, text_3
# from contents.example_plots  import plot_scatter

# =============================================================================
# Dash App and Flask Server
# =============================================================================
#app = dash.Dash(__name__)
app = dash.Dash(name=__name__, 
    #routes_pathname_prefix='/dash/',
    requests_pathname_prefix="/dash/",
    assets_folder = config.root+"/template/assets", 
    external_stylesheets = [
        #dbc.themes.CYBORG, 
        config.fontawesome,
        config.external_stylesheets,
    ]
)
# app.title = config.name
# server = app.server 

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
top_right_ui = dac.NavbarDropdown(
	badge_label = "?",
    badge_color= "danger",
    src = "https://quantee.ai",
	header_text="2 Items",
    children= [
		dac.NavbarDropdownItem(
			children = "message 11",
			date = "today"
		),
		dac.NavbarDropdownItem(
			children = "message 2",
			date = "yesterday"
		),
	]
)

navbar = dac.Navbar(
    className="nav nav-pills", 
    color = "white", 
    text=" My 1 !", 
    children=top_right_ui
)

# Sidebar
sideMenu = dac.SidebarMenu([
    dac.SidebarHeader(children="Test"),
    dac.SidebarMenuItem(id='sidebar_test', label='test', icon='box'),

    dac.SidebarHeader(children="Cards"),
    dac.SidebarMenuItem(id='tab_cards',        label='Basic cards',  icon='box'),
    dac.SidebarMenuItem(id='tab_social_cards', label='Social cards', icon='id-card'),
    dac.SidebarMenuItem(id='tab_tab_cards',    label='Tab cards',    icon='image'),
    
    dac.SidebarHeader(children="Boxes", style=dict(padding='0.5rem')),
    dac.SidebarMenuItem(id='tab_basic_boxes', label='Basic boxes',      icon='desktop'),
    dac.SidebarMenuItem(id='tab_value_boxes', label='Value/Info boxes', icon='suitcase'),

    dac.SidebarHeader(children="Gallery", ), # style=dict(padding='0.5rem')),
    dac.SidebarMenuItem(label='Galleries', icon='cubes', 
        children = [ # subitems
            dac.SidebarMenuSubItem(id='tab_gallery_1', label='Gallery 1', icon='arrow-circle-right', 
                badge_label='Soon',
                badge_color='success'
            ), 
            dac.SidebarMenuSubItem(id='tab_gallery_2', label='Gallery 2', icon='arrow-circle-right', 
                badge_label='Soon', 
                badge_color='success'
            )
        ]
    ),
])

sidebar = dac.Sidebar( sideMenu,
    title='Alyx',
	skin="dark",
    color="primary",
	brand_color="primary",
    #url="#",
    src="assets/logo.png",
    elevation=3,
    opacity=0.8,
    #style=style.SIDEBAR,
)

# Body
body = dac.Body(
    dac.TabItems([
        test_tab,
        cards_tab,
        # social_cards_tab,
        # tab_cards_tab,
        # basic_boxes_tab,
        # value_boxes_tab,
        # dac.TabItem(id='content_gallery_1', 
        #     children=  html.P('Gallery 1 (You can add Dash Bootstrap Components!)'), 
        # ),
        # dac.TabItem(id='content_gallery_2',
        #     children=html.P('Gallery 2 (You can add Dash Bootstrap Components!)'), 
        # ),
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(id='controlbar-slider',
            value=20,
            min=10, max=50, step=1,
        )
    ],
    title = "My right sidebar",
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A("@skcc dash",
		href = "https://onesixx.com/category/py/dash/", 
		target = "_blank", 
	),
	right_text = "my admin"
)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id, 
             n_tests,
             n_cards, n_social_cards, n_tab_cards, 
             n_basic_boxes, n_value_boxes, 
             n_gallery_1, n_gallery_2):
    # Depending on tab which triggered a callback, show/hide contents of app
    n=8
    result = [False]*n
    if input_id == 'sidebar_test' and n_tests:
        result[0] = True
        return result
    elif input_id == 'tab_cards' and n_cards: 
        result[1] = True
        return result
    elif input_id == 'tab_social_cards' and n_social_cards:
        result[2] = True
        return result
    elif input_id == 'tab_tab_cards' and n_tab_cards:
        result[3] = True
        return result
    elif input_id == 'tab_basic_boxes' and n_basic_boxes:
        result[4] = True
        return result
    elif input_id == 'tab_value_boxes' and n_value_boxes:
        result[5] = True
        return result
    elif input_id == 'tab_gallery_1' and n_gallery_1:
        result[6] = True
        return result
    elif input_id == 'tab_gallery_2' and n_gallery_2:
        result[7] = True
        return result
    else:
        return True, False, False, False, False, False, False, False # App init

###### right content show/hide
@app.callback(
    [Output('content_tests',        'active'),
     Output('content_cards',        'active'),
     Output('content_social_cards', 'active'),
     Output('content_tab_cards',    'active'),
     Output('content_basic_boxes',  'active'),
     Output('content_value_boxes',  'active'),
     Output('content_gallery_1',    'active'),
     Output('content_gallery_2',    'active')],
    [Input('sidebar_test',        'n_clicks'),
     Input('tab_cards',        'n_clicks'),
     Input('tab_social_cards', 'n_clicks'),
     Input('tab_tab_cards',    'n_clicks'),
     Input('tab_basic_boxes',  'n_clicks'),
     Input('tab_value_boxes',  'n_clicks'),
     Input('tab_gallery_1',    'n_clicks'),
     Input('tab_gallery_2',    'n_clicks')])
def display_tab(
    n_tests,
    n_cards, n_social_cards, n_tab_cards, 
    n_basic_boxes, n_value_boxes,
    n_gallery_1, n_gallery_2):
    # Callback context to recognize which input has been triggered
    ctx = dash.callback_context 
    # Get id of input which triggered callback 
    if not ctx.triggered:
        raise PreventUpdate
    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]   
    return activate(input_id, 
        n_tests,
        n_cards, n_social_cards, n_tab_cards, 
        n_basic_boxes, n_value_boxes, 
        n_gallery_1, n_gallery_2)

# Sidebar color block
# @app.callback(
#     [Output('sidebar_test',        'active'),
#      Output('tab_cards',        'active'),
#      Output('tab_social_cards', 'active'),
#      Output('tab_tab_cards',    'active'),
#      Output('tab_basic_boxes',  'active'),
#      Output('tab_value_boxes',  'active'),
#      Output('tab_gallery_1',    'active'),
#      Output('tab_gallery_2',    'active')],
#     [Input('sidebar_test',        'n_clicks'),
#      Input('tab_cards',        'n_clicks'),
#      Input('tab_social_cards', 'n_clicks'),
#      Input('tab_tab_cards',    'n_clicks'),
#      Input('tab_basic_boxes',  'n_clicks'),
#      Input('tab_value_boxes',  'n_clicks'),
#      Input('tab_gallery_1',    'n_clicks'),
#      Input('tab_gallery_2',    'n_clicks')]
# )
# def activate_tab(n_tests,
#     n_cards, n_social_cards, n_tab_cards, 
#     n_basic_boxes, n_value_boxes,
#     n_gallery_1, n_gallery_2):    
#     ctx = dash.callback_context # Callback context to recognize which input has been triggered
#     # Get id of input which triggered callback  
#     if not ctx.triggered:
#         raise PreventUpdate
#     else:
#         input_id = ctx.triggered[0]['prop_id'].split('.')[0]   
#     return activate(input_id, 
#         n_tests,
#         n_cards, n_social_cards, n_tab_cards, 
#         n_basic_boxes, n_value_boxes, 
#         n_gallery_1, n_gallery_2)
    
# @app.callback(
#     Output('tab_box_1', 'children'),
#     [Input('tab_box_1_menu', 'active_tab')]
# )
# def display_tabbox1(active_tab):
#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_1_tab1':
#         return text_1
#     elif active_tab == 'tab_box_1_tab2':
#         return text_2
#     elif active_tab == 'tab_box_1_tab3':
#         return text_3

# @app.callback(Output('tab_box_2', 'children'),
#               [Input('tab_box_2_menu', 'active_tab')]
# )
# def display_tabbox2(active_tab):
#     # Depending on tab which triggered a callback, show/hide contents of app
#     if active_tab == 'tab_box_2_tab1':
#         return text_1
#     elif active_tab == 'tab_box_2_tab2':
#         return text_2
#     elif active_tab == 'tab_box_2_tab3':
#         return text_3
    
# # Update figure on slider change
# @app.callback(
#     Output('box-graph', 'figure'),
#     [Input('controlbar-slider', 'value')])
# def update_box_graph(value):
#     return plot_scatter(value)

# =============================================================================
# Run app    
# =============================================================================
# if __name__ == '__main__':
#     app.run_server(debug=False)
