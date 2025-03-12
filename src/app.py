from dash import Dash  # type: ignore
import dash_bootstrap_components as dbc  # type: ignore
import dash_vega_components as dvc # type: ignore
from src.callbacks import register_callbacks  # Import the callback registration function
from src.components import layout

# Initialize the Dash app with Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for deployment

# Set tab title
app.title = "Hong Kong Passenger Traffic Tracker"

# Layout setup
app.layout = layout

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=False, port=8080)
