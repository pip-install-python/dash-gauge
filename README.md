# Dash Component Suite: Gauges, Knobs, Thermostat, Joystick & Display

[![PyPI version](https://badge.fury.io/py/dash-gauge.svg)](https://badge.fury.io/py/dash-gauge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A collection of interactive and visually appealing components for Plotly Dash. Enhance your dashboards with gauges, knobs, thermostats, joysticks, and 7-segment displays.

Explore demos & the interactive documentation:

https://pip-install-python.com/pip/dash_gauge

This library currently includes:

*   **`DashGauge`**: Customizable gauge charts (Grafana, Semicircle, Radial styles).
*   **`DashRotaryKnob`**: Interactive rotary knob controls with various skins.
*   **`DashThermostat`**: A thermostat-like input component.
*   **`DashRCJoystick`**: A virtual joystick component for directional input.
*   **`Dash7SegmentDisplay`**: A classic 7-segment display for numbers and hex values.

## Installation

1. **Install this library:**
    ```bash
    pip install dash-gauge
    ```

## Quick Start

Here's a minimal example using the `DashGauge`:

```python
import dash
from dash import html
import dash_gauge as dg # Use an alias like 'dcs' (Dash Component Suite) or similar

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Component Suite - Quick Start"),
    dg.DashGauge(
        id='quick-gauge',
        value=75,
        label="Speed",
        max=100,
        min=0,
        color={"gradient": True, "ranges": {"#5BE12C": [0, 50], "#F5CD19": [50, 80], "#EA4228": [80, 100]}},
        style={'width': '300px'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Component Documentation
Below are details and basic usage examples for each component. For full interactive examples, please refer to the `usage_*.py` files included in this repository.

---

### `DashGauge`

Displays a value on a customizable gauge. Supports different styles, color ranges, sub-arcs, custom labels, and pointers.

**Key Props:**

*   `id` (string): Component ID.
*   `value` (number): The value the gauge should indicate.
*   `type` (string): 'grafana', 'semicircle', or 'radial'. Default: 'grafana'.
*   `min`, `max` (number): Range of the gauge.
*   `arc` (dict): Configuration for the main arc (width, padding, colors, subArcs, tooltips etc.).
*   `pointer` (dict): Configuration for the needle/pointer (type, color, length, width, animation).
*   `labels` (dict): Configuration for value and tick labels.

**Basic Usage:**

```python
import dash_gauge as dg

# Inside your Dash layout:
dg.DashGauge(
    id="basic-gauge",
    value=50,
    label="Progress",
    minValue=0,
    maxValue=100
)
```

**-> See `usage_gauge.py` for detailed examples of customization.**

---

### `DashRotaryKnob`

An interactive knob component, useful for selecting values within a range. Comes with multiple visual skins.

**Key Props:**

*   `id` (string): Component ID.
*   `value` (number): The current value of the knob.
*   `min`, `max` (number): Range of the knob.
*   `step` (number): Increment/decrement step size.
*   `skinName` (string): Selects the visual appearance (e.g., 's1', 's5', 's10', up to 's18'). See `knob-skins-full.js` for options. Default: 's1'.
*   `preciseMode` (bool): If true, requires Shift key for fine adjustments.
*   `unlockDistance` (number): Degrees the mouse must move to unlock the knob.

**Basic Usage:**

```python
import dash_gauge as dg

# Inside your Dash layout:
dg.DashRotaryKnob(
    id="my-knob",
    value=25,
    min=0,
    max=100,
    skinName="s5" # Try different skins!
)

# Use callbacks to read the 'value' prop.
```

**-> See `usage_rotary_knob.py` for an interactive example with controls.**

---

### `DashThermostat`

A component mimicking a thermostat interface for setting a target value (like temperature).

**Key Props:**

*   `id` (string): Component ID.
*   `value` (number): The current set value.
*   `min`, `max` (number): Range of the thermostat.
*   `valueSuffix` (string): Text to display after the value (e.g., '°C', '%').
*   `disabled` (bool): Disable interaction.
*   `track` (dict): Configuration for the background track (colors, thickness, markers).
*   `handle` (dict): Configuration for the draggable handle.

**Basic Usage:**

```python
import dash_gauge as dg

# Inside your Dash layout:
dg.DashThermostat(
    id='thermo1',
    value=22,
    min=10,
    max=30,
    valueSuffix='°C',
    track={'colors': ['#2c8e98', '#dae8eb']} # Example cool colors
)

# Use callbacks to read the 'value' prop.
```

**-> See `usage_thermostat.py` for a complex example with mode switching and styling.**
**Note:** The `usage_thermostat.py` example may require CSS from an `assets` folder. Ensure you include the necessary CSS file if you adapt that example.

---

### `DashRCJoystick`

A virtual joystick component that reports direction, angle, and distance. Useful for controlling robotics, games, or simulations within Dash.

**Key Props:**

*   `id` (string): Component ID.
*   `baseRadius` (number): Radius of the joystick base.
*   `controllerRadius` (number): Radius of the movable controller knob.
*   `directionCountMode` (string): 'Five' (N,S,E,W,Center) or 'Nine' (includes diagonals). Default: 'Five'.
*   `throttle` (number): Milliseconds to throttle update events.
*   `angle` (number, read-only): Current angle in degrees.
*   `direction` (string, read-only): Current direction (e.g., 'Top', 'BottomLeft', 'Center').
*   `distance` (number, read-only): Current distance from center (normalized).

**Basic Usage:**

```python
import dash_gauge as dg
from dash import html, callback, Input, Output

# Inside your Dash layout:
dg.DashRCJoystick(
    id='joystick1',
    directionCountMode='Nine' # Use 9 directions
),
html.Div(id='joystick-output')

# Example callback:
@callback(
    Output('joystick-output', 'children'),
    Input('joystick1', 'direction'),
    Input('joystick1', 'angle'),
    Input('joystick1', 'distance')
)
def display_joystick_state(direction, angle, distance):
    return f"Dir: {direction}, Angle: {angle:.1f}, Dist: {distance:.2f}"

```

**-> See `usage_rc_joystick.py` for an example with controls to modify the joystick's appearance and behavior.**

---

### `Dash7SegmentDisplay` ⁉️ Doesn't currently Work has a map bug ⁉️

Renders numbers or hexadecimal strings using a classic 7-segment display style.

**Key Props:**

*   `id` (string): Component ID.
*   `value` (string | number): The value to display. Can be numeric or a hex string (e.g., "FF0A").
*   `count` (number): The number of digits to display.
*   `height` (number): The height of each digit in pixels.
*   `color` (string): Color of the lit segments.
*   `backgroundColor` (string): Background color behind the segments.
*   `skew` (bool): Apply a slight slant to the digits.

**Basic Usage:**

```python
import dash_gauge as dg

# Inside your Dash layout:
dg.Dash7SegmentDisplay(
    id='display-1',
    value="1234", # Can only display numbers
    count=4,      # Total characters including dot
    height=60,
    color='lime',
    backgroundColor='#222'
)
```

**-> See `usage_7_segment_display.py` for an interactive example allowing control over all properties.**

---

## Development

To contribute to this project or run the examples locally:

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [YOUR_PROJECT_DIRECTORY]
    ```

2.  **Set up a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Install Python dependencies, including development tools and Dash:
    ```bash
    pip install -r requirements.txt # Or setup.py equivalent
    pip install -e . # Install the package in editable mode
    ```

4.  **Install JavaScript dependencies:**
    ```bash
    npm install
    ```

5.  **Build the JavaScript components:**
    ```bash
    npm run build
    ```
    *(This command might differ based on your `package.json` scripts)*

6.  **Run an example app:**
    ```bash
    python usage_gauge.py # Or any other usage_*.py file
    ```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

This library wraps the following excellent React components:

*   [react-gauge-component](https://github.com/antoniolago/react-gauge-component)
*   [react-rotary-knob](https://github.com/hugozap/react-rotary-knob) & [react-rotary-knob-skin-pack](https://github.com/hugozap/react-rotary-knob-skin-pack)
*   [react-thermostat](https://github.com/shannonhochkins/react-thermostat)
*   [rc-joystick](https://github.com/rockyfrank/rc-joystick)
*   [react-7-segment-display](https://github.com/nachovigilante/react-7-segment-display)

Thanks to the original authors for their work.
