from dash.dependencies import Input, Output
import plotly.express as px

def register_callbacks(app):
    @app.callback(
        Output("net_passenger_inflow", "figure"),
        [
            Input("date_picker", "start_date"),
            Input("date_picker", "end_date"),
            Input("control_point_dropdown", "value"),
        ],
    )
    def update_net_passenger_flow(start_date, end_date, selected_control_points):
        # Filter data based on date range and selected control points
        filtered_df = df[
            (df["date"] >= start_date) & 
            (df["date"] <= end_date)
        ]
        
        if selected_control_points:
            filtered_df = filtered_df[filtered_df["control_point"].isin(selected_control_points)]
        
        # Aggregate data
        grouped_df = filtered_df.groupby(["date"]).agg(
            inflow=("arrivals", "sum"),
            outflow=("departures", "sum")
        ).reset_index()

        # Plot stacked line chart
        fig = px.area(
            grouped_df, 
            x="date", 
            y=["inflow", "outflow"],
            labels={"value": "Passenger Count", "date": "Date"},
            title="Net Passenger Flow",
            color_discrete_map={"inflow": "blue", "outflow": "orange"}
        )

        return fig