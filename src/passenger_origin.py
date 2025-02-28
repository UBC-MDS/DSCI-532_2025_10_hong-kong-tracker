import pandas as pd
import plotly.express as px

def passenger_origin(start_date, end_date, control_point: list[str] = None, arrival_departure: list[str] = None):
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
        x='passenger_origin',
        y='passenger_count',
        color='passenger_origin',
        title="Passenger Count by Passenger Origin",
        labels={'passenger_origin': 'Passenger Origin', 'passenger_count': 'Total Passengers'},
        barmode='group',
    )

    # Add labels on top of bars
    fig.update_traces(text=grouped_df['passenger_count'], textposition='outside')

    # Customize layout
    fig.update_layout(
        xaxis_title="Passenger Origin",
        yaxis_title="Total Passengers",
        showlegend=False
    )

    return fig