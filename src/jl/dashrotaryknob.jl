# AUTO GENERATED FILE - DO NOT EDIT

export dashrotaryknob

"""
    dashrotaryknob(;kwargs...)

A DashRotaryKnob component.

Keyword arguments:
- `id` (String; optional)
- `className` (String; optional)
- `format` (String; optional)
- `max` (Real; optional)
- `min` (Real; optional)
- `preciseMode` (Bool; optional)
- `skinName` (String; optional)
- `step` (Real; optional)
- `style` (Dict; optional)
- `unlockDistance` (Real; optional)
- `value` (Real; optional)
"""
function dashrotaryknob(; kwargs...)
        available_props = Symbol[:id, :className, :format, :max, :min, :preciseMode, :skinName, :step, :style, :unlockDistance, :value]
        wild_props = Symbol[]
        return Component("dashrotaryknob", "DashRotaryKnob", "dash_gauge", available_props, wild_props; kwargs...)
end

