# passenger_count.py
# Author: Paramveer Singh
# 25 February 2025

import pandas as pd
import altair as alt

def passenger_count(start_date, end_date, control_point: list[str] = 'all') -> dict:
    """
    Function used with callback to return passenger count chart

    Parameters
    ----------
    start_date : Date
        Start date of the data to look at
    end_date : Date
        End date of the data to look at
    control_point : list[str], optional
        Control point to filter for. Defaults to 'all' for all control points

    Returns
    -------
        dict
    Altair chart dictionary schema to render

    Example
    -------
    >>> passenger_count('01-01-2025', '01-20-2025', ['Airport', 'China Ferry Terminal'])
    """
    # Load data and parse dates
    df = pd.read_csv('../data/raw/data.csv').drop(columns='Unnamed: 0')
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

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
    if control_point == 'all':
        diff_df = diff_df.groupby('date').agg('sum').reset_index()
    else:
        diff_df = diff_df[
            diff_df['control_point'].isin(control_point)
            ].groupby('date').agg('sum').reset_index()
