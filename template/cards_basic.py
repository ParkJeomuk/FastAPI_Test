from common.pkg_ui    import *

from contents.example_plots import plot_pie, plot_surface, plot_scatter

dropdown_items = [
	dac.BoxDropdownItem(children="Link to google",
        url="https://www.google.com" ),
	dac.BoxDropdownItem(children="item 2",
        url="#" ),
	dac.BoxDropdownDivider(),
	dac.BoxDropdownItem(children="item 3",
        url="#" )
]

cards_tab = dac.TabItem(id='content_cards',
    children=[
        html.Div(
            [
                dac.Box(
                    [
                        dac.BoxHeader(title="Closable box with dropdown",
        					children = dac.BoxDropdown(dropdown_items),
                            collapsible = True, closable = True,),
                    	dac.BoxBody(
                            dcc.Graph(
                                figure = plot_pie(),
                                config = dict(displayModeBar=False),
                                style = {'width': '38vw'}
                            )
                        )		
                    ],
                    color = 'warning',
                    width = 6
                ),
                        
                dac.Box(
                    [
                        dac.BoxHeader( title="Closable box with gradient",
                            collapsible = True, closable = True, ),
                    	dac.BoxBody(
                            dcc.Graph(
                                figure = plot_surface(),
                                config = dict(displayModeBar=False),
                                style = {'width': '38vw'}
                            )
                        )		
                    ],
                    gradient_color = "success",
                    #color="danger",
                    width=6
                )
            ], 
            className='row'
        ),
                        
        html.Div(    
            dac.Box(
                [
                    dac.BoxHeader(title="Card with solidHeader and elevation",
                        collapsible = True, closable = True, ),
                	dac.BoxBody(
                        dcc.Graph(
                            figure = plot_scatter(),
                            config = dict(displayModeBar=False),
                            style = {'width': '38vw'}
                        )
                    )		
                ],
                color='primary',
                solid_header=True,
                elevation=4,
                width=12 
            ),
            className='row'
        )
            
    ]
)