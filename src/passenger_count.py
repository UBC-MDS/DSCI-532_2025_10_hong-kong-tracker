# passenger_count.py
# Author: Paramveer Singh
# 25 February 2025

import pandas as pd
import altair as alt

def passenger_count(start_date, end_date, control_point: str = 'all') -> dict:
    """
    Function used with callback to return passenger count chart

    Parameters
    ----------
    start_date : Date
        Start date of the data to look at
    end_date : Date
        End date of the data to look at
    control_point : str, optional
        Control point to filter for. Defaults to 'all' for all control points

    Returns
    -------
        dict
    Altair chart dictionary schema to render
    """
    # Load data and parse dates
    df = pd.read_csv('../data/raw/data.csv').drop(columns='Unnamed: 0')
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
