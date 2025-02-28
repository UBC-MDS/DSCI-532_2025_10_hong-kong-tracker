from src.passenger_count import passenger_count

import pandas as pd
from dash import Input, Output, dcc, html  # type: ignore
import plotly.express as px  # type: ignore
import dash_leaflet as dl  # type: ignore
import dash_leaflet.express as dlx  # type: ignore
from src.travel_method import travel_method
from src.passenger_origin import passenger_origin

# Load data
DATA_PATH = "data/processed/data.csv"
df = pd.read_csv(DATA_PATH)

# Ensure the date column is in datetime format
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")  # Adjust format if necessary

def compute_totals(filtered_df):
    """
    Computes total passenger counts and volume entries based on the filtered dataset.

    Parameters:
        filtered_df (pd.DataFrame): Filtered DataFrame based on user selections.

    Returns:
        tuple: Total passenger count as a formatted string and volume entries rounded to 8 decimal places.
    """
    if filtered_df.empty:
        return "0", "0"

    total_passengers = filtered_df["passenger_count"].sum()
    tourist_df = filtered_df[(filtered_df['travel_type'] == 'Arrival') & (filtered_df['passenger_origin'] != 'Hong Kong Residents')]
    volume_entries = round(len(tourist_df) / 7.54e6, 8)

    return f"{total_passengers:,}", f"{volume_entries:.8f}"

def register_callbacks(app):
    """
    Registers Dash callbacks for updating total passenger counts, passenger count graphs, and the map.

    Parameters:
        app (dash.Dash): The Dash application instance.
    """

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
        """
        Updates the total passenger count and volume entries based on user-selected filters.

        Parameters:
            start_date (str): The start date selected in the date picker.
            end_date (str): The end date selected in the date picker.
            control_points (list): List of selected control points.
            travel_types (list): List of selected travel types (arrival/departure).

        Returns:
            tuple: Updated total passenger count and volume entries.
        """
        if not start_date or not end_date:
            return "0", "0"

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        if control_points:
            filtered_df = filtered_df[filtered_df["control_point"].isin(control_points)]
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].isin(travel_types)]

        return compute_totals(filtered_df)

    @app.callback(
        Output("passenger_count", "spec"),
        [
            Input("date_picker", "start_date"),
            Input("date_picker", "end_date"),
            Input("control_point_dropdown", "value"),
        ]
    )
    def update_passenger_count(start_date, end_date, control_points):
        """
        Updates the passenger count bar chart based on user-selected filters.

        Parameters
        ----------
        start_date : str
            The start date selected in the date picker.
        end_date : str
            The end date selected in the date picker.
        control_points : list 
            List of selected control points.

        Returns
        -------
        dict
            alt.Chart object as a dict

        """
        schema = passenger_count(df, start_date, end_date, control_points)

        return schema

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
        """
        Updates the map visualization based on user-selected filters.

        Parameters:
            start_date (str): The start date selected in the date picker.
            end_date (str): The end date selected in the date picker.
            control_points (list): List of selected control points.
            travel_types (list): List of selected travel types (arrival/departure).

        Returns:
            dash_leaflet.Map: A map with CircleMarkers representing passenger counts at control points.
        """
        control_points_df = pd.read_csv("data/processed/control_points_hk.csv")

        start_date = pd.to_datetime(start_date) if start_date else df["date"].min()
        end_date = pd.to_datetime(end_date) if end_date else df["date"].max()

        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        if control_points:
            filtered_df = filtered_df[filtered_df["control_point"].str.strip().isin(control_points)]
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].str.strip().isin(travel_types)]

        if filtered_df.empty:
            return dl.Map(
                [dl.TileLayer()],
                center=[22.3193, 114.1694],  # Centering on Hong Kong
                zoom=11,
                style={"height": "500px", "width": "100%"}
            )

        passenger_counts = filtered_df.groupby("control_point")["passenger_count"].sum().reset_index()
        control_points_df = control_points_df.merge(passenger_counts, on="control_point", how="right").fillna(0)

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
    @app.callback(
    Output("travel_method", "figure"),
    [
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date"),
        Input("control_point_dropdown", "value"),
        Input("arrival_departure", "value"),
    ]
    )
    def update_travel_method(start_date, end_date, control_point, arrival_departure):
        return travel_method(start_date, end_date, control_point, arrival_departure)
    
    @app.callback(
    Output("passenger_origin", "figure"),
    [
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date"),
        Input("control_point_dropdown", "value"),
        Input("arrival_departure", "value"),
    ]
    )
    def update_passenger_origin(start_date, end_date, control_point, arrival_departure):
        return passenger_origin(start_date, end_date, control_point, arrival_departure)
