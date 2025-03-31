import dash
from dash import html, dcc, callback, Input, Output
import dash_gauge

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Gauge Component Demo"),
    html.Div([
        html.Div([
            html.H3("Basic Gauge"),
            dash_gauge.DashGauge(
                id="basic-gauge",
                value=50
            )
        ], style={'width': '33%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Temperature Gauge"),
            dash_gauge.DashGauge(
                id="temperature-gauge",
                type="semicircle",
                value=22.5,
                minValue=10,
                maxValue=35,
                arc={
                    "width": 0.2,
                    "padding": 0.005,
                    "cornerRadius": 1,
                    "subArcs": [
                        {
                            "limit": 15,
                            "color": "#EA4228",
                            "showTick": True,
                            "tooltip": {
                                "text": "Too low temperature!"
                            }
                        },
                        {
                            "limit": 17,
                            "color": "#F5CD19",
                            "showTick": True,
                            "tooltip": {
                                "text": "Low temperature!"
                            }
                        },
                        {
                            "limit": 28,
                            "color": "#5BE12C",
                            "showTick": True,
                            "tooltip": {
                                "text": "OK temperature!"
                            }
                        },
                        {
                            "limit": 30,
                            "color": "#F5CD19",
                            "showTick": True,
                            "tooltip": {
                                "text": "High temperature!"
                            }
                        },
                        {
                            "color": "#EA4228",
                            "tooltip": {
                                "text": "Too high temperature!"
                            }
                        }
                    ]
                },
                pointer={
                    "color": "#345243",
                    "length": 0.80,
                    "width": 15
                },
                labels={
                    "valueLabel": {
                        "hide": False,
                        "style": {
                            "fontSize": "35px",
                            "fill": "#fff",
                            "textShadow": "black 1px 0.5px 0px, black 0px 0px 0.03em, black 0px 0px 0.01em"
                        }
                    },
                    "tickLabels": {
                        "type": "outer",
                        "ticks": [
                            {"value": 13},
                            {"value": 22.5},
                            {"value": 32}
                        ]
                    }
                }
            )
        ], style={'width': '33%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Bandwidth Gauge"),
            dash_gauge.DashGauge(
                id="bandwidth-gauge",
                value=900,
                maxValue=3000,
                arc={
                    "nbSubArcs": 150,
                    "colorArray": ["#5BE12C", "#F5CD19", "#EA4228"],
                    "width": 0.2,
                    "padding": 0.003
                }
            )
        ], style={'width': '33%', 'display': 'inline-block'})
    ]),

    html.Div([
        html.H3("Interactive Gauge"),
        html.P("Use the slider to update the gauge value:"),
        dcc.Slider(
            id="gauge-slider",
            min=0,
            max=100,
            step=1,
            value=50,
            marks={i: str(i) for i in range(0, 101, 10)}
        ),
        dash_gauge.DashGauge(
            id="interactive-gauge",
            type="radial",
            arc={
                "colorArray": ["#5BE12C", "#EA4228"],
                "subArcs": [{"limit": 10}, {"limit": 30}, {}, {}, {}],
                "padding": 0.02,
                "width": 0.3
            },
            pointer={
                "elastic": True,
                "animationDelay": 0
            },
            labels={
                "tickLabels": {
                    "type": "inner",
                    "ticks": [
                        {"value": 20},
                        {"value": 40},
                        {"value": 60},
                        {"value": 80},
                        {"value": 100}
                    ]
                }
            }
        )
    ], style={'width': '50%', 'margin': '0 auto', 'padding': '20px'})
], style={ 'padding': '20px'})


@callback(
    Output("interactive-gauge", "value"),
    Input("gauge-slider", "value")
)
def update_gauge(value):
    return value


if __name__ == "__main__":
    app.run_server(debug=True, port=7655)
