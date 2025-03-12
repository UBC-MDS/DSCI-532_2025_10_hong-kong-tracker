from dash import Dash  # type: ignore
import dash_bootstrap_components as dbc  # type: ignore
import dash_vega_components as dvc # type: ignore
from callbacks import register_callbacks  # Import the callback registration function
from components import layout

# Initialize the Dash app with Bootstrap for styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for deployment

# Layout setup
app.layout = layout

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == "__main__":
    # app.run_server(debug=False, port=8080)
    app.run_server(debug=True)
