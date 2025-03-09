import pandas as pd
import plotly.express as px # type: ignore

def travel_method(start_date, end_date, control_point=None, arrival_departure=None):
    """
    Generates a bar chart visualizing the total number of passengers by travel method 
    (by sea, by air, by land) over a specified date range, filtered by control points 
    and arrival/departure types.

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
        A Plotly bar chart displaying the passenger count categorized by travel method.
    """
    # Load data
    df = pd.read_csv('data/processed/data.csv').drop(columns='Unnamed: 0')
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

    # Filter by control points (if specified)
    if control_point:  # Ensure it's not empty or "all"
        df = df[df['control_point'].isin(control_point)]

    # Filter by travel type (arrival/departure) if specified
    if arrival_departure:
        df = df[df['travel_type'].isin(arrival_departure)]

    # Filter by date range
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = df[df['date'].between(start_date, end_date)]

    # Aggregate data by travel method
    grouped_df = df.groupby('travel_method', as_index=False)['passenger_count'].sum()

    # Define the custom order for travel methods
    category_order = ["by land", "by air", "by sea"]

    # Create a Plotly Express bar chart
    fig = px.bar(
        grouped_df,
        x='passenger_count',
        y='travel_method',
        title="Passenger Count by Travel Method",
        labels={'travel_method': 'Travel Method', 'passenger_count': 'Total Passengers'},
        barmode='group',
        category_orders={"travel_method": category_order}  # Enforces the desired order
    )

    # Add labels on top of bars
    #fig.update_traces(text=grouped_df['passenger_count'], textposition='outside')

    # Set bar color
    fig.update_traces(marker_color='#5297C7')

    # Customize layout
    fig.update_layout(
        xaxis_title="Total Passengers",
        yaxis_title="Travel Method",
        plot_bgcolor='white',  # Remove background color
        paper_bgcolor='white',  # Remove outer background color
        xaxis=dict(showgrid=False),  # Remove x-axis grid
        yaxis=dict(showgrid=False),   # Remove y-axis grid
        showlegend=False
    )

    return fig