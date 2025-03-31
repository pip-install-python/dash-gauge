# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Dash7SegmentDisplay(Component):
    """A Dash7SegmentDisplay component.
Dash7SegmentDisplay is a Dash component that wraps the react-7-segment-display library.
It renders numeric or hexadecimal values in a 7-segment display style.
REVERTED: Padding/truncating logic removed. Back to basic string conversion.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- backgroundColor (string; default undefined):
    Color of the display background.

- className (string; default ''):
    The CSS class name for the container component.

- color (string; default 'red'):
    Color of the display segments when turned on.

- count (number; default 2):
    Number of digits to display.

- height (number; default 50):
    Total height of the display digits in pixels.

- skew (boolean; default False):
    Whether the digits should be skewed (slanted).

- style (dict; optional):
    Inline styles for the container component.

- value (string | number; default ''):
    The value to display. Can be a number (decimal) or a string
    (decimal or hexadecimal like \"FF\"). Null or undefined will
    result in a blank display."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gauge'
    _type = 'Dash7SegmentDisplay'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, value=Component.UNDEFINED, color=Component.UNDEFINED, height=Component.UNDEFINED, count=Component.UNDEFINED, backgroundColor=Component.UNDEFINED, skew=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'backgroundColor', 'className', 'color', 'count', 'height', 'skew', 'style', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'backgroundColor', 'className', 'color', 'count', 'height', 'skew', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Dash7SegmentDisplay, self).__init__(**args)
