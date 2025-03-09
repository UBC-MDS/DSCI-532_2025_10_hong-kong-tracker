# passenger_count.py
# Author: Paramveer Singh
# 25 February 2025

import pandas as pd
import plotly.graph_objects
import plotly.express as px

def passenger_count(df, start_date, end_date, control_point: list[str] = None) -> plotly.graph_objects.Figure:
    """
    Function used with callback to return passenger count chart

    Parameters
    ----------
    df : pd.DataFrame
        Loaded Hong Kong traffic dataframe
    start_date : Date
        Start date of the data to look at
    end_date : Date
        End date of the data to look at
    control_point : list[str], optional
        Control point to filter for. Defaults to None for all control points

    Returns
    -------
    plotly.graph_objects.Figure
            A Plotly figure showing the net passenger inflow over time

    Example
    -------
    >>> passenger_count('01-01-2025', '01-20-2025', ['Airport', 'China Ferry Terminal'])
    """
    # Drop unnamed column
    df = df.drop(columns='Unnamed: 0')

    # Convert dates to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Pivot dataframe to calculate difference for all passenger types
    diff_df = df.pivot(index=['date', 'control_point', 'passenger_origin'],
                       columns=['travel_type'],
                       values='passenger_count'
                       ).reset_index(

    ).drop(
        columns='passenger_origin'
    ).groupby(['date', 'control_point']).agg('sum').reset_index()

    diff_df['difference'] = diff_df['Arrival'] - diff_df['Departure']

    # Filter for specific control points or merge all control points
    if control_point is None or len(control_point) == 0:
        diff_df = diff_df.groupby('date').agg('sum').reset_index()
    else:
        diff_df = diff_df[
            diff_df['control_point'].isin(control_point)
            ].groupby('date').agg('sum').reset_index()

    # Plot with filtered range and return
    filtered_df = diff_df[diff_df['date'].between(start_date, end_date)]

    # Define colorblind-friendly colors
    # Derived from "Coloring for Colorblindness" by David Nichols
    # https://davidmathlogic.com/colorblind/
    positive_color = '#00008B'
    negative_color = '#DC3220'

    # Color list
    colors = [positive_color if diff > 0 else negative_color for diff in filtered_df['difference']]

    # Create plotly chart object
    fig = px.bar(
        filtered_df,
        x='date',
        y='difference',
        title='Net Passenger Inflow Over Time',
        labels={'date': 'Date', 'difference': 'Net passenger inflow (count)'},
        hover_data=['date', 'Arrival', 'Departure', 'difference'],
        template=None
    )

    # Update the bar colors
    fig.update_traces(marker_color=colors,
                      marker_line_width=0)

    # Update the background to be white
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=False
    )

    # Make gridlines black in color
    fig.update_yaxes(gridcolor='black')
    fig.update_xaxes(gridcolor='lightgrey')

    return fig
