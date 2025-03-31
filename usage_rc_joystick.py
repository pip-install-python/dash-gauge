import dash
from dash import html, dcc, callback, Input, Output, State
import dash_gauge

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash RC Joystick Component Demo"),

    html.Div([
        # Left side: Joystick Component
        html.Div([
            html.H3("Interactive Joystick"),
            dash_gauge.DashRCJoystick(
                id='my-joystick',
                # Optional: Customize appearance
                # baseRadius=100,
                # controllerRadius=40,
                directionCountMode='Nine', # Use 'Five' or 'Nine'
                style={'margin': '50px'} # Add some margin around it
            ),
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top', 'textAlign': 'center'}),

        # Right side: Displaying Joystick State
        html.Div([
            html.H3("Joystick State"),
            html.Div(id='joystick-output-direction'),
            html.Div(id='joystick-output-angle'),
            html.Div(id='joystick-output-distance'),

            html.Hr(),
            html.Label("Change Direction Mode:"),
            dcc.RadioItems(
                id='direction-mode-selector',
                options=[
                    {'label': '5 Directions', 'value': 'Five'},
                    {'label': '9 Directions', 'value': 'Nine'},
                ],
                value='Nine', # Initial value matches component
                inline=True
            ),
             html.Hr(),
            html.Label("Base Radius:"),
             dcc.Slider(id='base-radius-slider', min=50, max=150, step=5, value=75, marks={i: str(i) for i in range(50, 151, 25)}),
             html.Label("Controller Radius:"),
             dcc.Slider(id='controller-radius-slider', min=20, max=70, step=5, value=35, marks={i: str(i) for i in range(20, 71, 10)}),

        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '20px'})

    ]), # End of main row Div
])

# Callback to display joystick state changes
@callback(
    Output('joystick-output-direction', 'children'),
    Output('joystick-output-angle', 'children'),
    Output('joystick-output-distance', 'children'),
    Input('my-joystick', 'direction'),
    Input('my-joystick', 'angle'),
    Input('my-joystick', 'distance')
)
def update_joystick_output(direction, angle, distance):
    angle_str = f"Angle: {angle:.2f}°" if angle is not None else "Angle: N/A (Center)"
    distance_str = f"Distance: {distance:.2f}"
    direction_str = f"Direction: {direction}"
    return direction_str, angle_str, distance_str

# Callback to update joystick configuration from controls
@callback(
    Output('my-joystick', 'directionCountMode'),
    Output('my-joystick', 'baseRadius'),
    Output('my-joystick', 'controllerRadius'),
    Input('direction-mode-selector', 'value'),
    Input('base-radius-slider', 'value'),
    Input('controller-radius-slider', 'value'),
)
def update_joystick_config(direction_mode, base_radius, controller_radius):
    return direction_mode, base_radius, controller_radius


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
