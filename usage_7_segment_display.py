# Bug causing a lot of `map` error logs in console, am aware of it. Waiting for an upstream update
import dash
from dash import html, dcc, callback, Input, Output
import dash_gauge  # Assuming your components are exported under this name

app = dash.Dash(__name__)

# Common colors for dropdown
color_options = [
    {"label": "Red", "value": "red"},
    {"label": "Blue", "value": "blue"},
    {"label": "Green", "value": "lime"},
    {"label": "Yellow", "value": "yellow"},
    {"label": "Cyan", "value": "cyan"},
    {"label": "Orange", "value": "orange"},
    {"label": "Black", "value": "black"},
    {"label": "White", "value": "white"},
]

app.layout = html.Div([
    html.H1("Dash 7-Segment Display Component Demo"),

    html.Div([
        # Left side: Display Component
        html.Div([
            html.H3("Display Output"),
            dash_gauge.Dash7SegmentDisplay(
                id='my-display',
                value="123",  # Initial value
                count=5,      # Display 5 digits
                height=80,    # Set initial height
                color='cyan',
                backgroundColor='#222222', # Dark background
                skew=True,
                style={'marginBottom': '20px'}
            ),
             # Another example
            dash_gauge.Dash7SegmentDisplay(
                id='my-display-hex',
                value="F0A9",  # Initial hex value
                count=4,
                height=60,
                color='orange',
                backgroundColor='#111111',
            ),
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top', 'textAlign': 'center'}),

        # Right side: Controls
        html.Div([
            html.H3("Controls"),

            html.Label("Value (Number or Hex String):"),
            dcc.Input(id='display-value-input', type='text', value='1235', style={'width': '90%', 'marginBottom': '10px'}),

            html.Label("Number of Digits (count):"),
            dcc.Slider(id='display-count-slider', min=1, max=10, step=1, value=5, marks={i: str(i) for i in range(1, 11)}, tooltip={"placement": "bottom", "always_visible": True}),

            html.Label("Digit Height (pixels):"),
            dcc.Slider(id='display-height-slider', min=20, max=200, step=10, value=80, marks={i: str(i) for i in range(20, 201, 30)}, tooltip={"placement": "bottom", "always_visible": True}),

            html.Label("Segment Color:"),
            dcc.Dropdown(id='display-color-dropdown', options=color_options, value='cyan', clearable=False, style={'marginBottom': '10px', 'color': 'black'}),

            html.Label("Background Color:"),
            dcc.Dropdown(id='display-bgcolor-dropdown', options=[{'label': 'Dark Gray', 'value': '#222222'}, {'label': 'Black', 'value': '#111111'}, {'label': 'None', 'value': ''}] + color_options, value='#222222', style={'marginBottom': '10px', 'color': 'black'}),

            dcc.Checklist(
                id='display-skew-checklist',
                options=[{'label': ' Skew Digits', 'value': 'skew_on'}],
                value=['skew_on'], # Initially checked
                inline=True
            ),

        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '20px'})

    ], style={'padding': '20px'}), # End of main row Div
])

# Callback to update the main display based on controls
@callback(
    Output('my-display', 'value'),
    Output('my-display', 'count'),
    Output('my-display', 'height'),
    Output('my-display', 'color'),
    Output('my-display', 'backgroundColor'),
    Output('my-display', 'skew'),
    Input('display-value-input', 'value'),
    Input('display-count-slider', 'value'),
    Input('display-height-slider', 'value'),
    Input('display-color-dropdown', 'value'),
    Input('display-bgcolor-dropdown', 'value'),
    Input('display-skew-checklist', 'value') # Input is a list
)
def update_display_output(val_input, count, height, color, bgcolor, skew_checklist):
    skew_bool = 'skew_on' in skew_checklist # Convert checklist value to boolean
    # Handle empty background color string
    final_bgcolor = bgcolor if bgcolor else None # Pass None if empty string selected

    # You might want add validation for the value input here if needed
    # e.g., check if hex is valid, limit length based on count, etc.
    # For simplicity, passing it directly for now.

    return val_input, count, height, color, final_bgcolor, skew_bool


if __name__ == "__main__":
    app.run_server(debug=True, port=8889)
