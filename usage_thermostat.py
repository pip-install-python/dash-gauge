import dash
from dash import html, dcc, callback, Input, Output, State
import dash_gauge
# import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                assets_folder="assets",)

# Define colors for different modes
heat_colors = ['#cfac48', '#cd5401']
cool_colors = ['#dae8eb', '#2c8e98']
dry_colors = ['#fff', '#ffc0bd']
off_colors = ['#848484', '#383838']

app.layout = html.Div([


    # Main container
    html.Div([
        html.Div([
            # Current temperature display
            html.Div([
                html.Div('28°', id='current-temp-display'),
                html.Span('CURRENT')
            ], className='current-temperature', id='current-temp-container'),

            # Left side buttons (fan control)
            html.Div([
                html.Button([
                    html.I(className='fas fa-fan fan-icon', id='fan-icon')
                ], id='fan-button', className='fab fab-fan', n_clicks=0),
            ], className='actions-left'),

            # Right side buttons (mode controls)
            html.Div([
                html.Button([
                    html.I(className='fas fa-fire')
                ], id='heat-button', className='fab fab-heat', n_clicks=0),

                html.Button([
                    html.I(className='fas fa-tint')
                ], id='dry-button', className='fab fab-dry', n_clicks=0),

                html.Button([
                    html.I(className='fas fa-snowflake')
                ], id='cool-button', className='fab fab-cool', n_clicks=0),
            ], className='actions'),

            # Thermostat component
            dash_gauge.DashThermostat(
                id='thermostat',
                value=28,
                min=6,
                max=36,
                valueSuffix='°C',
                track={
                    'colors': heat_colors
                },
                style={'width': '300px', 'height': '450px', 'marginBottom': '20px'},
            ),

            # Power button
            html.Button([
                html.I(className='fas fa-power-off')
            ], id='power-button', className='fab fab-large fab-heat fab-active', n_clicks=0),

            # Hidden value storage for state management
            dcc.Store(id='app-state', data={
                'mode': 'heat',
                'fan_mode': 'High',
                'temperature': 21,
                'power': True
            })
        ], className='container')
    ], className='area'),

    # Include Font Awesome for icons
    html.Link(
        rel='stylesheet',
        href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css'
    )
])


# Callback to handle mode button clicks (heat, cool, dry)
@callback(
    [Output('app-state', 'data', allow_duplicate=True),
     Output('thermostat', 'track'),
     Output('heat-button', 'className'),
     Output('cool-button', 'className'),
     Output('dry-button', 'className')],
    [Input('heat-button', 'n_clicks'),
     Input('cool-button', 'n_clicks'),
     Input('dry-button', 'n_clicks')],
    [State('app-state', 'data')],
    prevent_initial_call=True
)
def update_mode(heat_clicks, cool_clicks, dry_clicks, state):
    triggered_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    # Reset all button classes
    heat_class = 'fab fab-heat'
    cool_class = 'fab fab-cool'
    dry_class = 'fab fab-dry'

    if triggered_id == 'heat-button':
        state['mode'] = 'heat'
        track = {'colors': heat_colors}
        heat_class += ' fab-active'
    elif triggered_id == 'cool-button':
        state['mode'] = 'cool'
        track = {'colors': cool_colors}
        cool_class += ' fab-active'
    elif triggered_id == 'dry-button':
        state['mode'] = 'dry'
        track = {'colors': dry_colors}
        dry_class += ' fab-active'

    return state, track, heat_class, cool_class, dry_class


# Callback to handle fan button clicks
@callback(
    [Output('app-state', 'data', allow_duplicate=True),
     Output('fan-icon', 'className'),
     Output('fan-button', 'className')],
    [Input('fan-button', 'n_clicks')],
    [State('app-state', 'data')],
    prevent_initial_call=True
)
def update_fan_mode(n_clicks, state):
    fan_modes = ['Low', 'Mid', 'High']

    if n_clicks % 3 == 0:
        state['fan_mode'] = 'Low'
        icon_class = 'fas fa-fan fan-icon fan-low'
    elif n_clicks % 3 == 1:
        state['fan_mode'] = 'Mid'
        icon_class = 'fas fa-fan fan-icon fan-mid'
    else:
        state['fan_mode'] = 'High'
        icon_class = 'fas fa-fan fan-icon fan-high'

    button_class = 'fab fab-fan fab-active' if state['power'] else 'fab fab-fan'

    return state, icon_class, button_class


# Callback to handle power button
@callback(
    [Output('app-state', 'data'),
     Output('thermostat', 'disabled'),
     Output('thermostat', 'track', allow_duplicate=True),
     Output('power-button', 'className'),
     Output('current-temp-container', 'style'),
     Output('fan-button', 'className', allow_duplicate=True)],
    [Input('power-button', 'n_clicks')],
    [State('app-state', 'data')],
    prevent_initial_call=True
)
def toggle_power(n_clicks, state):
    state['power'] = not state['power']

    if state['power']:
        disabled = False
        track = {'colors': heat_colors if state['mode'] == 'heat' else
        cool_colors if state['mode'] == 'cool' else
        dry_colors}
        power_class = 'fab fab-large fab-heat fab-active'
        temp_style = {'color': heat_colors[1] if state['mode'] == 'heat' else
        cool_colors[1] if state['mode'] == 'cool' else
        dry_colors[1]}
        fan_class = 'fab fab-fan fab-active'
    else:
        disabled = True
        track = {'colors': off_colors}
        power_class = 'fab fab-large'
        temp_style = {'color': 'white'}
        fan_class = 'fab fab-fan'

    return state, disabled, track, power_class, temp_style, fan_class


# Callback to handle thermostat value changes
@callback(
    Output('app-state', 'data', allow_duplicate=True),
    [Input('thermostat', 'value')],
    [State('app-state', 'data')],
    prevent_initial_call=True
)
def update_temperature(value, state):
    state['temperature'] = value
    return state


# Initialize fan icon class
@callback(
    Output('fan-icon', 'className', allow_duplicate=True),
    Input('app-state', 'data'),
    prevent_initial_call=True
)
def initialize_fan_icon(state):
    if not state['power']:
        return 'fas fa-fan fan-icon'

    if state['fan_mode'] == 'Low':
        return 'fas fa-fan fan-icon fan-low'
    elif state['fan_mode'] == 'Mid':
        return 'fas fa-fan fan-icon fan-mid'
    else:
        return 'fas fa-fan fan-icon fan-high'


# Initialize current temperature style
@callback(
    Output('current-temp-container', 'style', allow_duplicate=True),
    Input('app-state', 'data'),
    prevent_initial_call=True
)
def initialize_temp_style(state):
    if not state['power']:
        return {'color': 'white'}

    if state['mode'] == 'heat':
        return {'color': heat_colors[1]}
    elif state['mode'] == 'cool':
        return {'color': cool_colors[1]}
    else:
        return {'color': dry_colors[1]}


if __name__ == "__main__":
    app.run_server(debug=True)