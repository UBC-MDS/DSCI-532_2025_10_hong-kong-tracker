import pandas as pd
from dash import Input, Output # type: ignore
import plotly.express as px  # type: ignore
import dash_leaflet as dl  # type: ignore
import dash_leaflet.express as dlx  # type: ignore
from src.travel_method import travel_method
from src.passenger_origin import passenger_origin
from src.passenger_count import passenger_count

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
        Output("passenger_count", "figure"),
        [
            Input("date_picker", "start_date"),
            Input("date_picker", "end_date"),
            Input("control_point_dropdown", "value"),
        ]
    )
    def update_passenger_count(start_date, end_date, control_points):
        """
        Updates the net passenger count bar chart based on user-selected filters.

        Parameters
        ----------
        start_date : str
            The start date selected in the date picker
        end_date : str
            The end date selected in the date picker
        control_points : list 
            List of selected control points

        Returns
        -------
        plotly.graph_objects.Figure
            A Plotly figure showing the net passenger inflow over time

        """
        try:
            schema = passenger_count(df, start_date, end_date, control_points)
        except Exception:
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
    def update_passenger_origin(start_date, end_date, control_point, travel_types):
        return passenger_origin(start_date, end_date, control_point, travel_types)
    
    @app.callback(
    Output("net_passenger_inflow", "figure"),
    [
        Input("date_picker", "start_date"),
        Input("date_picker", "end_date"),
        Input("control_point_dropdown", "value"),
        Input("arrival_departure", "value"),
    ],
)
    def update_net_passenger_flow(start_date, end_date, control_point, travel_types):
        """
        Generates an area chart visualizing the net passenger flow over time, categorized by travel type
        (Arrivals and Departures). The function filters data based on the selected date range, control points,
        and travel types before aggregating passenger counts.

        Parameters:
        ----------
        start_date : str
            The start date selected in the date picker (ISO format: YYYY-MM-DD).
        end_date : str
            The end date selected in the date picker (ISO format: YYYY-MM-DD).
        control_point : list of str
            A list of selected control points where passengers enter or exit.
        travel_types : list of str
            A list specifying whether to include 'Arrival', 'Departure', or both.

        Returns:
        -------
        plotly.graph_objects.Figure
            A Plotly area chart displaying passenger inflow and outflow over time.
        """
        # Convert start_date and end_date to datetime, fallback to dataset range
        start_date = pd.to_datetime(start_date) if start_date else df["date"].min()
        end_date = pd.to_datetime(end_date) if end_date else df["date"].max()

        # Filter dataset based on date range
        filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        # Apply control point filtering if selected
        if control_point:
            filtered_df = filtered_df[filtered_df["control_point"].isin(control_point)]
        
        # Apply control point filtering if selected
        if travel_types:
            filtered_df = filtered_df[filtered_df["travel_type"].isin(travel_types)]

        # Ensure required columns exist
        required_columns = {"date", "travel_type", "passenger_count"}
        if not required_columns.issubset(df.columns):
            raise KeyError(f"Missing required columns: {required_columns - set(df.columns)}")

        # Aggregate passenger counts per date & travel_type
        grouped_df = filtered_df.groupby(["date", "travel_type"])["passenger_count"].sum().reset_index()

        # Create the area chart
        fig = px.area(
            grouped_df,
            x="date",
            y="passenger_count",
            color="travel_type",  # Separate Arrivals and Departures
            labels={"passenger_count": "Passenger Count", "date": "Date", "travel_type": "Travel Type"},
            title="Passenger Flow Over Time",
            color_discrete_map={"Arrival": "#ADD8E6", "Departure": "#00008B"},  # Changed to light&dark blue
        )

        fig.update_layout(
            showlegend=False,
            plot_bgcolor="white",  # Removes grey background
            paper_bgcolor="white"  # Ensures no grey on the outer area
        )


        return fig