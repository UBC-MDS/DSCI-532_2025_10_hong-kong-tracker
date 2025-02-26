import pandas as pd

# Create a DataFrame with latitude and longitude information
data = pd.DataFrame({
    "control_point": [
        "Airport", "Express Rail Link West Kowloon", "Hung Hom", "Lo Wu",
        "Lok Ma Chau Spur Line", "Heung Yuen Wai", "Hong Kong-Zhuhai-Macao Bridge", "Lok Ma Chau",
        "Man Kam To", "Sha Tau Kok", "Shenzhen Bay", "China Ferry Terminal", "Harbour Control",
        "Kai Tak Cruise Terminal", "Macau Ferry Terminal", "Tuen Mun Ferry Terminal"
    ], # from EDA
    "Latitude": [
        22.3080, 22.3033, 22.3032, 22.5285,
        22.5016, 22.5567, 22.3193, 22.5117,
        22.5370, 22.5483, 22.4929, 22.2961, 22.2936,
        22.3076, 22.2877, 22.3881
    ],
    "Longitude": [
        113.9185, 114.1608, 114.1821, 114.1204,
        114.0731, 114.1768, 113.9462, 114.0708,
        114.1294, 114.2100, 113.9184, 114.1682, 114.1751,
        114.2166, 114.1510, 113.9621
    ]
})

# source is from https://www.immd.gov.hk/eng/contactus/control_points.html

# Save DataFrame as a CSV file in the 'data' folder
csv_path = "data/processed/control_points_hk.csv"
data.to_csv(csv_path, index=False)
