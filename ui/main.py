from dash import html
from dash import dcc 
# https://docs-dash-admin-components.herokuapp.com/l/components
import dash_admin_components as dac

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ui.sidebar import sidebar
# Navbar
top_right_ui = dac.NavbarDropdown(
	badge_label = "!",
    badge_color= "danger",
    src = "https://quantee.ai",
	header_text="2 Items",
    children= [
		dac.NavbarDropdownItem(
			children = "message 1",
			date = "today"
		),
		dac.NavbarDropdownItem(
			children = "message 2",
			date = "yesterday"
		),
	]
)
navbar = dac.Navbar(id= "mybread",
                    color = "white", 
                    text = os.environ.get("WELCOME"), 
                    children = top_right_ui)



import pages.dash_pages.view
### Cards ----
import pages.basic_cards.view
import pages.social_cards.view
import pages.tab_cards.view
### Boxes ----
import pages.basic_boxes.view
import pages.value_boxes.view
### Gallery ----
import pages.gallery_1.view
import pages.gallery_2.view
# Body
body = dac.Body(
    dac.TabItems([
        #pages.home.view.content,
        pages.dash_pages.view.content,

        pages.basic_cards.view.content,
        pages.social_cards.view.content,
        pages.tab_cards.view.content,

        pages.basic_boxes.view.content,
        pages.value_boxes.view.content,

        pages.gallery_1.view.content,
        pages.gallery_2.view.content
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title = "My right sidebar",
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A("@DawidKopczyk, Quantee powered by sixx",
		href = "https://onesixx.com", 
		target = "_blank", 
	),
	right_text = "2022 SK"
)

# =============================================================================
# App Layout
# =============================================================================
layout = dac.Page([navbar, sidebar, body, controlbar, footer])
