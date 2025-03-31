# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashRotaryKnob(Component):
    """A DashRotaryKnob component.


Keyword arguments:

- id (string; optional)

- className (string; optional)

- format (string; optional)

- max (number; optional)

- min (number; optional)

- preciseMode (boolean; optional)

- skinName (string; optional)

- step (number; optional)

- style (dict; optional)

- unlockDistance (number; optional)

- value (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gauge'
    _type = 'DashRotaryKnob'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, value=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, step=Component.UNDEFINED, skinName=Component.UNDEFINED, format=Component.UNDEFINED, preciseMode=Component.UNDEFINED, unlockDistance=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'format', 'max', 'min', 'preciseMode', 'skinName', 'step', 'style', 'unlockDistance', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'format', 'max', 'min', 'preciseMode', 'skinName', 'step', 'style', 'unlockDistance', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashRotaryKnob, self).__init__(**args)
