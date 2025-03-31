# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashGauge(Component):
    """A DashGauge component.
DashGauge is a Dash component that wraps the react-gauge-component library.
It creates customizable gauge charts for data visualization.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- arc (dict; optional):
    Configuration for the arc of the gauge.

    `arc` is a dict with keys:

    - cornerRadius (number; optional)

    - padding (number; optional)

    - width (number; optional)

    - nbSubArcs (number; optional)

    - gradient (boolean; optional)

    - colorArray (list of strings; optional)

    - emptyColor (string; optional)

    - subArcs (list of dicts; optional)

        `subArcs` is a list of dicts with keys:

        - limit (number; optional)

        - color (string; optional)

        - length (number; optional)

        - showTick (boolean; optional)

        - tooltip (dict; optional)

            `tooltip` is a dict with keys:

            - text (string; optional)

            - style (dict; optional)

- className (string; default "dash-gauge-component"):
    CSS class name for the component.

- componentPath (string; optional):
    Component path for internal Dash handling.

- labels (dict; optional):
    Configuration for the labels of the gauge.

    `labels` is a dict with keys:

    - valueLabel (dict; optional)

        `valueLabel` is a dict with keys:

        - formatTextValue (optional)

        - matchColorWithArc (boolean; optional)

        - maxDecimalDigits (number; optional)

        - style (dict; optional)

        - hide (boolean; optional)

    - tickLabels (dict; optional)

        `tickLabels` is a dict with keys:

        - hideMinMax (boolean; optional)

        - type (a value equal to: "inner", "outer"; optional)

        - ticks (list of dicts; optional)

            `ticks` is a list of dicts with keys:

    - value (number; optional)

    - valueConfig (dict; optional)

    - lineConfig (dict; optional)

        - defaultTickValueConfig (dict; optional)

        - defaultTickLineConfig (dict; optional)

- marginInPercent (dict; optional):
    Sets the margin for the chart inside the containing SVG element.

    `marginInPercent` is a number | dict with keys:

    - top (number; optional)

    - bottom (number; optional)

    - left (number; optional)

    - right (number; optional)

- maxValue (number; default 100):
    The maximum value of the gauge.

- minValue (number; default 0):
    The minimum value of the gauge.

- pointer (dict; optional):
    Configuration for the pointer of the gauge.

    `pointer` is a dict with keys:

    - type (a value equal to: "needle", "blob", "arrow"; optional)

    - color (string; optional)

    - hide (boolean; optional)

    - baseColor (string; optional)

    - length (number; optional)

    - width (number; optional)

    - animate (boolean; optional)

    - elastic (boolean; optional)

    - animationDuration (number; optional)

    - animationDelay (number; optional)

    - strokeWidth (number; optional)

- style (dict; optional):
    Inline style for the component.

- type (a value equal to: "grafana", "semicircle", "radial"; default "grafana"):
    The type of the gauge. Can be \"grafana\", \"semicircle\" or
    \"radial\".

- value (number; default 33):
    The value of the gauge."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gauge'
    _type = 'DashGauge'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, componentPath=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, type=Component.UNDEFINED, marginInPercent=Component.UNDEFINED, value=Component.UNDEFINED, minValue=Component.UNDEFINED, maxValue=Component.UNDEFINED, arc=Component.UNDEFINED, pointer=Component.UNDEFINED, labels=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'arc', 'className', 'componentPath', 'labels', 'marginInPercent', 'maxValue', 'minValue', 'pointer', 'style', 'type', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'arc', 'className', 'componentPath', 'labels', 'marginInPercent', 'maxValue', 'minValue', 'pointer', 'style', 'type', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashGauge, self).__init__(**args)
