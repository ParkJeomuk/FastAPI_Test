from common.pkg_ui    import *

from contents.example_plots import plot_pie, plot_surface, plot_scatter

# test_tab = dac.TabItem(id='content_tests',
# )
import dash_table 
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# test_tab = dash_table.DataTable(
#             id='content_tests',
#             columns=[{"name": i, "id": i} for i in df.columns],
#             data=df.to_dict('records'),
#         )
test_tab = dac.TabItem(id='content_tests',
    children=[
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
        )
    ]
)