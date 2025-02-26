import pandas as pd
import dash
from dash import Input, Output, dcc, html
import plotly.express as px
import dash_leaflet as dl
import dash_leaflet.express as dlx

# Load data
DATA_PATH = "data/raw/data.csv"
df = pd.read_csv(DATA_PATH)

# Ensure the date column is in datetime format
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")  # Adjust format if necessary

def compute_totals(filtered_df):
    if filtered_df.empty:
        return "0", "0"
    total_passengers = filtered_df["passenger_count"].sum()
    tourist_df = filtered_df[(filtered_df['travel_type'] == 'Arrival') & (filtered_df['passenger_origin'] != 'Hong Kong Residents')]
    volume_entries = round(len(tourist_df) / 7.54e6, 8)
    return f"{total_passengers:,}", f"{volume_entries:.8f}"

def register_callbacks(app):
    @app.callback(
        [Output("total_passengers", "children"),
         Output("volume_entries", "children")],
        [
            Input("date_picker", "start_date"),
            Input("date_picker", "end_date"),
            Input("control_point_dropdown", "value"),
            Input("arrival_departure", "value"),
        ]
    )
    def update_total_counts(start_date, end_date, control_points, travel_types):
        # Ensure the date filters are valid
        if not start_date or not end_date:
            return "0", "0"

        # Convert to datetime for filtering
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter dataset
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        # Handle control point filtering
        if control_points:
            filtered_df = filtered_df[filtered_df["control_point"].isin(control_points)]

        # Handle travel type filtering
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].isin(travel_types)]

        return compute_totals(filtered_df)

    @app.callback(
        Output("passenger_count", "figure"),
        [
            Input("date_picker", "start_date"),
            Input("date_picker", "end_date"),
            Input("control_point_dropdown", "value"),
            Input("arrival_departure", "value"),
        ]
    )
    def update_passenger_count(start_date, end_date, control_points, travel_types):
        # Ensure the date filters are valid
        if not start_date or not end_date:
            return px.bar(title="Select a valid date range")

        # Convert to datetime for filtering
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter dataset
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        # Handle control point filtering
        if control_points:
            filtered_df = filtered_df[filtered_df["control_point"].isin(control_points)]

        # Handle travel type filtering
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].isin(travel_types)]

        # Aggregate passenger count by date and travel type
        aggregated_df = filtered_df.groupby(["date", "travel_type"], as_index=False).sum()

        # If no data remains, return an empty plot
        if aggregated_df.empty:
            return px.bar(title="No data available for the selected filters")

        # Create bar chart with colors differentiating arrival and departure
        fig = px.bar(
            aggregated_df,
            x="date",
            y="passenger_count",
            color="travel_type",
            title="Passenger Count Over Time",
            labels={"passenger_count": "Number of Passengers", "date": "Date", "travel_type": "Travel Type"},
            barmode="group",
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Passenger Count",
            showlegend=True,  # Enable legends for travel type differentiation
            xaxis=dict(showticklabels=False)  # Hide labels on x-axis
        )

        return fig

    @app.callback(
    Output("map", "children"),
    [
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date"),
        Input("control_point_dropdown", "value"),
        Input("arrival_departure", "value")
    ]
    )
    def update_map(start_date, end_date, control_points, travel_types):
        control_points_df = pd.read_csv("data/processed/control_points_hk.csv")

        start_date = pd.to_datetime(start_date) if start_date else df["date"].min()
        end_date = pd.to_datetime(end_date) if end_date else df["date"].max()

        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        if control_points:
            filtered_df = filtered_df[filtered_df["control_point"].str.strip().isin(control_points)]
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].str.strip().isin(travel_types)]

    # If no data remains, return an empty Leaflet map
        if filtered_df.empty:
            return dl.Map(
                [dl.TileLayer()],
                center=[22.3193, 114.1694],  # Centering on Hong Kong
                zoom=11,
                style={"height": "500px", "width": "100%"}
         )

        passenger_counts = filtered_df.groupby("control_point")["passenger_count"].sum().reset_index()
        control_points_df = control_points_df.merge(passenger_counts, on="control_point", how="right").fillna(0)
        print(control_points_df)
        markers = [
            dl.CircleMarker(
                center=(row["Latitude"], row["Longitude"]),
                radius=max(5, min(row["passenger_count"] / 1000, 15)),  
                color="blue" if row["passenger_count"] < 50000 else "red",
                fill=True,
                fillOpacity=0.6,
                children=dl.Popup(f"{row['control_point']}: {int(row['passenger_count']):,} passengers")
            )
            for _, row in control_points_df.iterrows()
        ]

        return dl.Map(
            [dl.TileLayer()] + markers,
            center=[22.3193, 114.1694],  # Centering on Hong Kong
            zoom=11,
            style={"height": "500px", "width": "100%"}
        )