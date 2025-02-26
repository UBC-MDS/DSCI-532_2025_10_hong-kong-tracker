from dash import Dash, html, dcc  # type: ignore
import dash_bootstrap_components as dbc  # type: ignore
import pandas as pd
from callbacks import register_callbacks  # Import the callback registration function
from datetime import timedelta

# Load data to get control point values
DATA_PATH = "data/raw/data.csv"
df = pd.read_csv(DATA_PATH)

# Ensure the date column is in datetime format
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")

# Extract unique control points for dropdown options
control_point_options = [{"label": cp, "value": cp} for cp in df["control_point"].unique()]

# Get the last date in the dataset
last_date = df["date"].max().date() if not df["date"].isna().all() else None

# Initialize the Dash app with Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sidebar for filters
sidebar = html.Div(
    [
        html.H2("Filters", className="display-6"),
        html.Hr(),
        html.P("Select time period:"),
        dcc.DatePickerRange(id="date_picker", start_date=last_date - timedelta(days=5), end_date=last_date, max_date_allowed=last_date ), 
        html.Br(),
        html.P("Select control point:"),
        dcc.Dropdown(id="control_point_dropdown", options=control_point_options, multi=True),
        html.Br(),
        html.P("Select arrival or departure:"),
        dcc.Checklist(
            id="arrival_departure",
            options=[{"label": "Arrival", "value": "Arrival"}, {"label": "Departure", "value": "Departure"}],
            value=["Arrival", "Departure"],  # Default to both checked
            inline=False,
        ),
    ],
    className="bg-light p-3",
    style={"width": "20%", "position": "fixed", "height": "100vh", "overflowY": "auto"},
)

# Main content area
content = html.Div(
    [
        html.H1("Hong Kong Passenger Traffic Tracker", className="text-center"),

        # Circles for total passenger count and total data entries
        html.Div(
            [
                html.Div([html.P("Total Passengers"), html.H3(id="total_passengers")], className="circle"),
                html.Div([html.P("Volume Entries"), html.H3(id="volume_entries")], className="circle"),
            ],
            className="circle-container",
            style={
                "display": "flex",
                "justify-content": "center",
                "gap": "40px",
                "marginBottom": "20px",
            }
        ),

        html.Hr(),
        dbc.Row([
            dbc.Col(dcc.Graph(id="net_passenger_inflow"), width=6),
            dbc.Col(dcc.Graph(id="passenger_count"), width=6),  # Passenger count chart
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id="travel_type"), width=6),
            dbc.Col(dcc.Graph(id="passenger_origin"), width=6),
        ]),
        html.Hr(),
        html.H3("Volume of Control Point Traffic"),
        dbc.Row([
            dbc.Col(html.Div(id="map", style={"width": "100%", "height": "600px"}), width=12),  # Full-width map
]),
    ],
    style={"marginLeft": "22%", "padding": "20px"},
)

# Layout setup
app.layout = html.Div([sidebar, content])

# Register callbacks
register_callbacks(app)  # Ensure this is called!

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
