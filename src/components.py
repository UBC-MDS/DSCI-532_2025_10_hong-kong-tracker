from dash import Dash, html, dcc  # type: ignore
import dash_bootstrap_components as dbc  # type: ignore
import dash_vega_components as dvc  # type: ignore
import pandas as pd
from src.callbacks import register_callbacks  # Import the callback registration function
from datetime import timedelta

# Load data to get control point values
DATA_PATH = "data/processed/data.csv"
df = pd.read_csv(DATA_PATH)

# Ensure the date column is in datetime format
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")

# Extract unique control points for dropdown options
control_point_options = [
    {"label": cp, "value": cp} for cp in df["control_point"].unique()
]

# Get the last date in the dataset
last_date = df["date"].max().date() if not df["date"].isna().all() else None
DEFAULT_DATE_RANGE = {
    "start_date": last_date - timedelta(days=15) if last_date else None,
    "end_date": last_date,
}

# --- Sidebar ---
sidebar = html.Div(
    [
        html.H2("Hong Kong Passenger Traffic Tracker", className="display-6"),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.P("Total Passengers", className="text-center", style={"color": "#00008B", "fontSize": "18px"}),
                            html.H5(id="total_passengers", className="text-center", style={"color": "#00008B", "fontSize": "22px"}),
                        ])
                    ),
                    width=12,
                    className="mb-2",
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.P("Volume of Entries", className="text-center", style={"color": "#00008B", "fontSize": "18px"}),
                            html.H5(id="volume_entries", className="text-center", style={"color": "#00008B", "fontSize": "22px"}),
                        ])
                    ),
                    width=12,
                    className="mb-2",
                ),
            ],
            className="mb-3",
        ),
        html.Hr(style={"borderColor": "#00008B"}),
        html.P("Select time period:", style={"color": "#00008B", "fontSize": "16px"}),
        dcc.DatePickerRange(
            id="date_picker",
            start_date=DEFAULT_DATE_RANGE["start_date"],
            end_date=DEFAULT_DATE_RANGE["end_date"],
            max_date_allowed=last_date,
            style={"width": "100%", "color": "#00008B"},
        ),
        html.Br(),
        html.P("Select control point:", style={"color": "#00008B", "fontSize": "16px"}),
        dcc.Dropdown(
            id="control_point_dropdown",
            options=control_point_options,
            multi=True,
            placeholder="Select one or more control points",
            style={"color": "#00008B"},
        ),
        html.Br(),
        dbc.Row(
            [
                html.P("Select arrival or departure:", style={"color": "#00008B", "fontSize": "16px"}),
                dcc.Checklist(
                    id="arrival_departure",
                    options=[
                        {"label": "Arrival", "value": "Arrival"},
                        {"label": "Departure", "value": "Departure"},
                    ],
                    value=["Arrival", "Departure"],
                    inline=False,
                    style={"color": "#00008B"},
                ),
            ]
        ),
    ],
    className="p-3",
    style={
        "width": "20%",
        "position": "fixed",
        "height": "100vh",
        "overflowY": "auto",
        "borderRight": "2px solid #00008B",
    },
)

# --- Map Section ---
map_section = html.Div(
    [
        html.H3("Volume of Control Point Traffic", style={"color": "#00008B", "textAlign": "center"}),
        html.Div(
            id="map",
            style={
                "width": "500px",
                "height": "500px",
                "border": "2px solid #00008B",
                "overflow": "hidden",
            },
        ),
    ],
    style={
        "marginBottom": "50px",
        "paddingBottom": "20px",
        "width": "80%",
        "margin": "auto",
    },
)

# --- Graphs Section ---
graphs_section = dbc.Container([
    dbc.Row([
        # First column for the map
        dbc.Col(
            map_section, 
            width=6, 
            style={"height": "350px"}
        ),

        # Second column for the three graphs
        dbc.Col([
            dcc.Graph(id="passenger_origin", style={"flex": "1"}),
            dcc.Graph(id="travel_method", style={"flex": "1"}),
        ], width=6, style={
            "height": "500px",
            "display": "flex",
            "flexDirection": "column",
            "gap": "15px",
        })  
    ])
], style={"margin-bottom": "30px"})

# --- Separate Graph Section ---
separate_graph = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="passenger_count"), width=6),
                dbc.Col(dcc.Graph(id="net_passenger_inflow"), width=6),
            ]
        ),
    ],
    style={ "paddingTop": "20px"}
)

# --- Footer Section ---
footer = dbc.Container(
    html.Div(
        [
            html.Hr(style={"borderColor": "#00008B"}),
            html.P(
                [
                    "This interactive dashboard provides real-time insights into passenger traffic across various control points in Hong Kong.",
                    html.Br(),
                    "Users can explore travel trends based on arrivals, departures, and different travel methods.",
                    html.Br(),
                    "Developed by: Nelli Hovhannisyan, Paramveer Singh, Hankun Xiao, Yichun Liu",
                    html.Br(),
                    html.A("GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2025_10_hong-kong-tracker", target="_blank", style={"color": "#00008B"}),
                    html.Br(),
                    "Last Updated: 2025-MARCH-09",
                ],
                className="text-center",
                style={"color": "#00008B", "fontSize": "14px"},
            ),
        ],
    )
)

# --- Main Content Layout ---
content = html.Div(
    [
        graphs_section,
        separate_graph,
        footer,
    ],
    style={
        "marginLeft": "22%",
        "padding": "10px",
        "overflow": "hidden",
        "color": "#00008B",
        "fontSize": "16px",
    },
)

# Layout setup
layout = html.Div(
    [sidebar, content],
    style={
        "fontFamily": "Arial, sans-serif",
        "color": "#00008B",
    },
)
