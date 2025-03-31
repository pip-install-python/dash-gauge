import dash
from dash import html, dcc, callback, Input, Output, State
import dash_gauge

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Rotary Knob Component Demo"),
    html.Div([
        html.H2("Interactive Knob"),
        html.Div([
            html.Div(id="knob-value-display", style={"margin": "10px", "fontSize": "18px"}),
            dash_gauge.DashRotaryKnob(
                id="interactive-knob",
                skinName="s10",
                value=50,
                min=0,
                max=100,
                format="{value}%",
                # style={"margin": "20px auto", "width": "100px", "height": "100px"}
            ),
        ], style={'width': '40%', 'display': 'inline-block', 'textAlign': 'center'}),
        html.Div([
            html.Label("Adjust with slider:"),
            dcc.Slider(
                id="knob-slider",
                min=0,
                max=100,
                step=1,
                value=50,
                marks={i: str(i) for i in range(0, 101, 10)},
            ),
            html.Br(),
            html.Label("Change skin:"),
            dcc.Dropdown(
                id="skin-selector",
                options=[
                    {"label": f"Skin {i}", "value": f"s{i}"} for i in range(1, 19)
                ],
                value="s1",
                clearable=False
            ),
            html.Br(),
            html.Label("Precision Mode:"),
            dcc.RadioItems(
                id="precision-mode",
                options=[
                    {"label": "On", "value": True},
                    {"label": "Off", "value": False}
                ],
                value=True,
                inline=True
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '20px'})
    ]),
])


@callback(
    Output("knob-value-display", "children"),
    Input("interactive-knob", "value")
)
def update_knob_value_display(value):
    return f"Current value: {value:.1f}"


@callback(
    Output("interactive-knob", "value"),
    Input("knob-slider", "value"),
)
def update_knob_from_slider(value):
    return value


@callback(
    Output("interactive-knob", "skinName"),
    Input("skin-selector", "value"),
)
def update_knob_skin(skin_name):
    return skin_name


@callback(
    Output("interactive-knob", "preciseMode"),
    Input("precision-mode", "value"),
)
def update_precision_mode(precision_mode):
    return precision_mode


if __name__ == "__main__":
    app.run_server(debug=True, port=8765)
