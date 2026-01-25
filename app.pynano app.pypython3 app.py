import pandas as pd
from dash import Dash, html, dash_table

app = Dash(__name__)
app.title = "Project Aion — Pre-Race"

df = pd.DataFrame([
    {"#": 1, "Runner": "Fleet Street", "Tote": 5.50, "Fixed": 5.80, "BF Back": 5.90, "BF Lay": 6.00},
    {"#": 2, "Runner": "Solar Accent", "Tote": 3.20, "Fixed": 3.10, "BF Back": 3.15, "BF Lay": 3.25},
])

app.layout = html.Div(
    style={"fontFamily":"system-ui","padding":"20px"},
    children=[
        html.H1("AION — PRE-RACE (NEW SCREEN)"),
        html.P("If you see this headline, you're running app.py (not test_dash.py)."),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": c, "id": c} for c in df.columns],
            style_cell={"padding":"8px"},
            style_header={"fontWeight":"700"},
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

nano app.py

import pandas as pd
from dash import Dash, html, dash_table

app = Dash(__name__)
app.title = "Project Aion — Pre-Race"

df = pd.DataFrame([
    {"#": 1, "Runner": "Fleet Street", "Tote": 5.50, "Fixed": 5.80, "BF Back": 5.90, "BF Lay": 6.00},
    {"#": 2, "Runner": "Solar Accent", "Tote": 3.20, "Fixed": 3.10, "BF Back": 3.15, "BF Lay": 3.25},
])

app.layout = html.Div(
    style={"fontFamily":"system-ui","padding":"20px"},
    children=[
        html.H1("AION — PRE-RACE (NEW SCREEN)"),
        html.P("If you see this headline, you're running app.py (not test_dash.py)."),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": c, "id": c} for c in df.columns],
            style_cell={"padding":"8px"},
            style_header={"fontWeight":"700"},
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)



