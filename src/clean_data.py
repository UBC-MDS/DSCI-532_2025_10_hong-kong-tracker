import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw/data.csv')
    df = df.iloc[:, 1:6]
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
    
    # Engine Travel Method
    df['travel_method'] = df['control_point'].apply(lambda x: 
        'by air' if 'Airport' in x else 
        'by sea' if any(key_word in x for key_word in ['Terminal', 'Harbour']) else 
        'by land'
    )
    # Export dataframe as csv
    df.to_csv('data/processed/data.csv')
    return df
    
    
if __name__ == "__main__":
    clean_data()
