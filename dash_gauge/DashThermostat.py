# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashThermostat(Component):
    """A DashThermostat component.
DashThermostat is a Dash component that wraps the react-thermostat library.
It provides an interactive thermostat control for temperature or other values.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    The CSS class name for the component.

- disabled (boolean; default False):
    Whether the thermostat is disabled.

- handle (dict; optional):
    Configuration for the handle.

    `handle` is a dict with keys:

    - size (number; optional)

    - colors (dict; optional)

        `colors` is a dict with keys:

        - handle (string; optional)

        - icon (string; optional)

        - pulse (string; optional)

- max (number; default 100):
    The maximum value of the thermostat.

- min (number; default 0):
    The minimum value of the thermostat.

- style (dict; optional):
    Inline styles for the component.

- track (dict; optional):
    Configuration for the track.

    `track` is a dict with keys:

    - colors (list of strings; optional)

    - thickness (number; optional)

    - markers (dict; optional)

        `markers` is a dict with keys:

        - enabled (boolean; optional)

        - every (number; optional)

        - count (number; optional)

        - main (dict; optional)

            `main` is a dict with keys:

            - color (string; optional)

            - length (number; optional)

            - thickness (number; optional)

        - sub (dict; optional)

            `sub` is a dict with keys:

            - color (string; optional)

            - length (number; optional)

            - thickness (number; optional)

- value (number; required):
    The current temperature value.

- valueSuffix (string; default '°'):
    The suffix to display after the value (like °C, °F, etc)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gauge'
    _type = 'DashThermostat'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, value=Component.REQUIRED, min=Component.UNDEFINED, max=Component.UNDEFINED, valueSuffix=Component.UNDEFINED, disabled=Component.UNDEFINED, handle=Component.UNDEFINED, track=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'disabled', 'handle', 'max', 'min', 'style', 'track', 'value', 'valueSuffix']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'disabled', 'handle', 'max', 'min', 'style', 'track', 'value', 'valueSuffix']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DashThermostat, self).__init__(**args)
