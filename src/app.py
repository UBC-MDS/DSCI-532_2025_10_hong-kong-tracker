from dash import Dash, html, dcc # type: ignore
import dash_bootstrap_components as dbc # type: ignore

# Initialize the Dash app with Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sidebar for filters
sidebar = html.Div(
    [
        html.H2("Filters", className="display-6"),
        html.Hr(),
        html.P("Select time period:"),
        dcc.DatePickerRange(id="date_picker"),
        html.Br(),
        html.P("Select control point:"),
        dcc.Dropdown(id="control_point_dropdown", options=["Point A", "Point B", "Point C"], multi=True),
        html.Br(),
        html.P("Select arrival or departure:"),
        dcc.Checklist(id="arrival_departure", options=["Arrival", "Departure"], inline=False),
    ],
    className="bg-light p-3",
    style={"width": "20%", "position": "fixed", "height": "100vh", "overflowY": "auto"},
)

# Main content area
content = html.Div(
    [
        html.H1("Hong Kong Passenger Traffic Tracker", className="text-center"),
        html.Hr(),
        dbc.Row([
            dbc.Col(dcc.Graph(id="net_passenger_inflow"), width=6),
            dbc.Col(dcc.Graph(id="passenger_count"), width=6),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id="travel_type"), width=6),
            dbc.Col(dcc.Graph(id="passenger_origin"), width=6),
        ]),
        html.Hr(),
        html.H3("Volume of Control Point Traffic"),
        dcc.Graph(id="control_point_traffic"),
    ],
    style={"marginLeft": "22%", "padding": "20px"},
)

# Layout setup
app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    app.run_server(debug=False, port=8080)
