# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashRCJoystick(Component):
    """A DashRCJoystick component.
DashRCJoystick is a Dash component that wraps the rc-joystick library.
It provides an interactive joystick control.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- angle (number; default undefined):
    [Readonly] The current angle of the joystick controller (in
    degrees). Undefined when the direction is 'Center'.

- baseRadius (number; default 75):
    Joystick's base radius.

- className (string; optional):
    The CSS class name for the container component.

- controllerClassName (string; optional):
    Joystick controller's extra className.

- controllerRadius (number; default 35):
    Joystick controller's radius.

- direction (string; default 'Center'):
    [Readonly] The current direction of the joystick controller.
    Possible values depend on directionCountMode.

- directionCountMode (a value equal to: 'Five', 'Nine'; default 'Five'):
    Direction count mode: 'Five' or 'Nine'. 'Five': Center, Right,
    Top, Left, Bottom 'Nine': Center, Right, RightTop, Top, TopLeft,
    Left, LeftBottom, Bottom, BottomRight.

- distance (number; default 0):
    [Readonly] The current distance of the controller from the center.

- insideMode (boolean; default False):
    Controller will always be inside joystick's base if True.

- style (dict; optional):
    Inline styles for the container component.

- throttle (number; default 0):
    Throttle time for all change events (in milliseconds)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gauge'
    _type = 'DashRCJoystick'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, baseRadius=Component.UNDEFINED, controllerRadius=Component.UNDEFINED, controllerClassName=Component.UNDEFINED, insideMode=Component.UNDEFINED, throttle=Component.UNDEFINED, directionCountMode=Component.UNDEFINED, angle=Component.UNDEFINED, direction=Component.UNDEFINED, distance=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'angle', 'baseRadius', 'className', 'controllerClassName', 'controllerRadius', 'direction', 'directionCountMode', 'distance', 'insideMode', 'style', 'throttle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'angle', 'baseRadius', 'className', 'controllerClassName', 'controllerRadius', 'direction', 'directionCountMode', 'distance', 'insideMode', 'style', 'throttle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashRCJoystick, self).__init__(**args)
