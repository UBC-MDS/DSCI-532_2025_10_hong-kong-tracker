import pandas as pd

def load_data():
    """
    Loads and cleans daily passenger traffic data into a DataFrame.
    Data Source: 
    https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic
    """
    data_source_link = "https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/statistics_on_daily_passenger_traffic.csv"
    df = pd.read_csv(data_source_link)
    df = df.iloc[:, :6]
    df = df.melt(
        id_vars=df.columns[:3],
        var_name="passenger_origin",
        value_name="passenger_count",
    )
    # Rename columns
    df = df.rename(
        columns={
            "Date": "date",
            "Control Point": "control_point",
            "Arrival / Departure": "travel_type",
        }
    )
    
    # Export dataframe as csv
    df.to_csv('../data/raw/data.csv')
    
    return df
    
    
if __name__ == "__main__":
    load_data()
