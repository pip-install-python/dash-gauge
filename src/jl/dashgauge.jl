# AUTO GENERATED FILE - DO NOT EDIT

export dashgauge

"""
    dashgauge(;kwargs...)

A DashGauge component.
DashGauge is a Dash component that wraps the react-gauge-component library.
It creates customizable gauge charts for data visualization.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `arc` (optional): Configuration for the arc of the gauge. arc has the following type: lists containing elements 'cornerRadius', 'padding', 'width', 'nbSubArcs', 'gradient', 'colorArray', 'emptyColor', 'subArcs'.
Those elements have the following types:
  - `cornerRadius` (Real; optional)
  - `padding` (Real; optional)
  - `width` (Real; optional)
  - `nbSubArcs` (Real; optional)
  - `gradient` (Bool; optional)
  - `colorArray` (Array of Strings; optional)
  - `emptyColor` (String; optional)
  - `subArcs` (optional): . subArcs has the following type: Array of lists containing elements 'limit', 'color', 'length', 'showTick', 'tooltip'.
Those elements have the following types:
  - `limit` (Real; optional)
  - `color` (String; optional)
  - `length` (Real; optional)
  - `showTick` (Bool; optional)
  - `tooltip` (optional): . tooltip has the following type: lists containing elements 'text', 'style'.
Those elements have the following types:
  - `text` (String; optional)
  - `style` (Dict; optional)s
- `className` (String; optional): CSS class name for the component
- `componentPath` (String; optional): Component path for internal Dash handling
- `labels` (optional): Configuration for the labels of the gauge. labels has the following type: lists containing elements 'valueLabel', 'tickLabels'.
Those elements have the following types:
  - `valueLabel` (optional): . valueLabel has the following type: lists containing elements 'formatTextValue', 'matchColorWithArc', 'maxDecimalDigits', 'style', 'hide'.
Those elements have the following types:
  - `formatTextValue` (optional)
  - `matchColorWithArc` (Bool; optional)
  - `maxDecimalDigits` (Real; optional)
  - `style` (Dict; optional)
  - `hide` (Bool; optional)
  - `tickLabels` (optional): . tickLabels has the following type: lists containing elements 'hideMinMax', 'type', 'ticks', 'defaultTickValueConfig', 'defaultTickLineConfig'.
Those elements have the following types:
  - `hideMinMax` (Bool; optional)
  - `type` (a value equal to: "inner", "outer"; optional)
  - `ticks` (optional): . ticks has the following type: Array of lists containing elements 'value', 'valueConfig', 'lineConfig'.
Those elements have the following types:
  - `value` (Real; optional)
  - `valueConfig` (Dict; optional)
  - `lineConfig` (Dict; optional)s
  - `defaultTickValueConfig` (Dict; optional)
  - `defaultTickLineConfig` (Dict; optional)
- `marginInPercent` (optional): Sets the margin for the chart inside the containing SVG element. marginInPercent has the following type: Real | lists containing elements 'top', 'bottom', 'left', 'right'.
Those elements have the following types:
  - `top` (Real; optional)
  - `bottom` (Real; optional)
  - `left` (Real; optional)
  - `right` (Real; optional)
- `maxValue` (Real; optional): The maximum value of the gauge
- `minValue` (Real; optional): The minimum value of the gauge
- `pointer` (optional): Configuration for the pointer of the gauge. pointer has the following type: lists containing elements 'type', 'color', 'hide', 'baseColor', 'length', 'width', 'animate', 'elastic', 'animationDuration', 'animationDelay', 'strokeWidth'.
Those elements have the following types:
  - `type` (a value equal to: "needle", "blob", "arrow"; optional)
  - `color` (String; optional)
  - `hide` (Bool; optional)
  - `baseColor` (String; optional)
  - `length` (Real; optional)
  - `width` (Real; optional)
  - `animate` (Bool; optional)
  - `elastic` (Bool; optional)
  - `animationDuration` (Real; optional)
  - `animationDelay` (Real; optional)
  - `strokeWidth` (Real; optional)
- `style` (Dict; optional): Inline style for the component
- `type` (a value equal to: "grafana", "semicircle", "radial"; optional): The type of the gauge. Can be "grafana", "semicircle" or "radial"
- `value` (Real; optional): The value of the gauge
"""
function dashgauge(; kwargs...)
        available_props = Symbol[:id, :arc, :className, :componentPath, :labels, :marginInPercent, :maxValue, :minValue, :pointer, :style, :type, :value]
        wild_props = Symbol[]
        return Component("dashgauge", "DashGauge", "dash_gauge", available_props, wild_props; kwargs...)
end

