import pandas as pd

def load_data():
    """
    Loads daily passenger traffic data into a DataFrame.
    Data Source: 
    https://data.gov.hk/en-data/dataset/hk-immd-set5-statistics-daily-passenger-traffic
    """
    data_source_link = "https://www.immd.gov.hk/opendata/eng/transport/immigration_clearance/statistics_on_daily_passenger_traffic.csv"
    df = pd.read_csv(data_source_link)
    df.to_csv('data/raw/data.csv')
    return df
    
    
if __name__ == "__main__":
    load_data()
