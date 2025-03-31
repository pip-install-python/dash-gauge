# AUTO GENERATED FILE - DO NOT EDIT

export dashthermostat

"""
    dashthermostat(;kwargs...)

A DashThermostat component.
DashThermostat is a Dash component that wraps the react-thermostat library.
It provides an interactive thermostat control for temperature or other values.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): The CSS class name for the component.
- `disabled` (Bool; optional): Whether the thermostat is disabled.
- `handle` (optional): Configuration for the handle.. handle has the following type: lists containing elements 'size', 'colors'.
Those elements have the following types:
  - `size` (Real; optional)
  - `colors` (optional): . colors has the following type: lists containing elements 'handle', 'icon', 'pulse'.
Those elements have the following types:
  - `handle` (String; optional)
  - `icon` (String; optional)
  - `pulse` (String; optional)
- `max` (Real; optional): The maximum value of the thermostat.
- `min` (Real; optional): The minimum value of the thermostat.
- `style` (Dict; optional): Inline styles for the component.
- `track` (optional): Configuration for the track.. track has the following type: lists containing elements 'colors', 'thickness', 'markers'.
Those elements have the following types:
  - `colors` (Array of Strings; optional)
  - `thickness` (Real; optional)
  - `markers` (optional): . markers has the following type: lists containing elements 'enabled', 'every', 'count', 'main', 'sub'.
Those elements have the following types:
  - `enabled` (Bool; optional)
  - `every` (Real; optional)
  - `count` (Real; optional)
  - `main` (optional): . main has the following type: lists containing elements 'color', 'length', 'thickness'.
Those elements have the following types:
  - `color` (String; optional)
  - `length` (Real; optional)
  - `thickness` (Real; optional)
  - `sub` (optional): . sub has the following type: lists containing elements 'color', 'length', 'thickness'.
Those elements have the following types:
  - `color` (String; optional)
  - `length` (Real; optional)
  - `thickness` (Real; optional)
- `value` (Real; required): The current temperature value.
- `valueSuffix` (String; optional): The suffix to display after the value (like °C, °F, etc).
"""
function dashthermostat(; kwargs...)
        available_props = Symbol[:id, :className, :disabled, :handle, :max, :min, :style, :track, :value, :valueSuffix]
        wild_props = Symbol[]
        return Component("dashthermostat", "DashThermostat", "dash_gauge", available_props, wild_props; kwargs...)
end

