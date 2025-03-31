# AUTO GENERATED FILE - DO NOT EDIT

export dash7segmentdisplay

"""
    dash7segmentdisplay(;kwargs...)

A Dash7SegmentDisplay component.
Dash7SegmentDisplay is a Dash component that wraps the react-7-segment-display library.
It renders numeric or hexadecimal values in a 7-segment display style.
REVERTED: Padding/truncating logic removed. Back to basic string conversion.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `backgroundColor` (String; optional): Color of the display background.
- `className` (String; optional): The CSS class name for the container component.
- `color` (String; optional): Color of the display segments when turned on.
- `count` (Real; optional): Number of digits to display.
- `height` (Real; optional): Total height of the display digits in pixels.
- `skew` (Bool; optional): Whether the digits should be skewed (slanted).
- `style` (Dict; optional): Inline styles for the container component.
- `value` (String | Real; optional): The value to display. Can be a number (decimal) or a string (decimal or hexadecimal like "FF"). Null or undefined will result in a blank display.
"""
function dash7segmentdisplay(; kwargs...)
        available_props = Symbol[:id, :backgroundColor, :className, :color, :count, :height, :skew, :style, :value]
        wild_props = Symbol[]
        return Component("dash7segmentdisplay", "Dash7SegmentDisplay", "dash_gauge", available_props, wild_props; kwargs...)
end

