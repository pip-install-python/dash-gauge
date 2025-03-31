# AUTO GENERATED FILE - DO NOT EDIT

export dashrcjoystick

"""
    dashrcjoystick(;kwargs...)

A DashRCJoystick component.
DashRCJoystick is a Dash component that wraps the rc-joystick library.
It provides an interactive joystick control.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `angle` (Real; optional): [Readonly] The current angle of the joystick controller (in degrees).
Undefined when the direction is 'Center'.
- `baseRadius` (Real; optional): Joystick's base radius.
- `className` (String; optional): The CSS class name for the container component.
- `controllerClassName` (String; optional): Joystick controller's extra className.
- `controllerRadius` (Real; optional): Joystick controller's radius.
- `direction` (String; optional): [Readonly] The current direction of the joystick controller.
Possible values depend on directionCountMode.
- `directionCountMode` (a value equal to: 'Five', 'Nine'; optional): Direction count mode: 'Five' or 'Nine'.
'Five': Center, Right, Top, Left, Bottom
'Nine': Center, Right, RightTop, Top, TopLeft, Left, LeftBottom, Bottom, BottomRight
- `distance` (Real; optional): [Readonly] The current distance of the controller from the center.
- `insideMode` (Bool; optional): Controller will always be inside joystick's base if true.
- `style` (Dict; optional): Inline styles for the container component.
- `throttle` (Real; optional): Throttle time for all change events (in milliseconds).
"""
function dashrcjoystick(; kwargs...)
        available_props = Symbol[:id, :angle, :baseRadius, :className, :controllerClassName, :controllerRadius, :direction, :directionCountMode, :distance, :insideMode, :style, :throttle]
        wild_props = Symbol[]
        return Component("dashrcjoystick", "DashRCJoystick", "dash_gauge", available_props, wild_props; kwargs...)
end

