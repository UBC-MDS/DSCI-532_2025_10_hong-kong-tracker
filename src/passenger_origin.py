import pandas as pd
import plotly.express as px # type: ignore

def passenger_origin(start_date, end_date, control_point=None, arrival_departure=None):
    """
    Generates a horizontal bar chart visualizing the total number of passengers 
    categorized by their country of origin over a specified date range, 
    optionally filtered by control points and arrival/departure types.

    Parameters:
    ----------
    start_date : str or pd.Timestamp
        The start date for filtering the dataset (format: YYYY-MM-DD).
    end_date : str or pd.Timestamp
        The end date for filtering the dataset (format: YYYY-MM-DD).
    control_point : list of str, optional
        A list of selected control points to filter passenger data. 
        If None or ["all"], no filtering is applied.
    arrival_departure : list of str, optional
        A list specifying whether to include 'Arrival', 'Departure', or both. 
        If None or ["all"], no filtering is applied.

    Returns:
    -------
    plotly.graph_objects.Figure
        A Plotly horizontal bar chart displaying passenger counts by country of origin.
    """
    # Load data
    df = pd.read_csv('data/processed/data.csv').drop(columns='Unnamed: 0')
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

    # Filter by control points (if specified)
    if control_point and control_point != ['all']:  # Ensure it's not empty or "all"
        df = df[df['control_point'].isin(control_point)]

    # Filter by travel type (arrival/departure) if specified
    if arrival_departure and arrival_departure != ['all']:
        df = df[df['travel_type'].isin(arrival_departure)]

    # Filter by date range
    df = df[df['date'].between(start_date, end_date)]

    # Aggregate data by travel passenger_origin
    grouped_df = df.groupby('passenger_origin', as_index=False)['passenger_count'].sum()

    # Sort data by the custom order
    grouped_df = grouped_df.sort_values('passenger_origin')

    # Create a Plotly Express bar chart
    fig = px.bar(
        grouped_df,
        x='passenger_count',
        y='passenger_origin',
        color='passenger_origin',
        orientation='h',
        title="Passenger Count by Passenger Origin",
        labels={'passenger_origin': 'Passenger Origin', 'passenger_count': 'Total Passengers'},
        barmode='group',
    )

    # Add labels on top of bars
    #fig.update_traces(text=grouped_df['passenger_count'], textposition='outside')

    # Customize layout
    fig.update_layout(
        xaxis_title="Total Passengers",
        yaxis_title="Passenger Origin",
        showlegend=False
    )

    return fig