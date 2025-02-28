# passenger_count.py
# Author: Paramveer Singh
# 25 February 2025

import pandas as pd
import altair as alt

def passenger_count(df, start_date, end_date, control_point: list[str] = None) -> dict:
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
        dict
    Altair chart dictionary schema to render

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
    return alt.Chart(
        diff_df[diff_df['date'].between(start_date, end_date)],
        title='Net Passenger Inflow Over Time'
        ).mark_bar().encode(
            alt.X('date', type='temporal', title='Date'),
            alt.Y('difference', title='Net passenger inflow'),
            alt.Tooltip(
                ['date', 'Arrival', 'Departure', 'difference'],
            ),
            color=alt.condition(
                alt.datum.difference > 0,
                alt.value('green'),
                alt.value('red')
            )
    ).interactive().to_dict()
