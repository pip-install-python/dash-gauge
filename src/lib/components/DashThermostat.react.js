import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
import { Thermostat } from 'react-thermostat';

/**
 * DashThermostat is a Dash component that wraps the react-thermostat library.
 * It provides an interactive thermostat control for temperature or other values.
 */
const DashThermostat = ({
    id,
    className,
    style,
    value,
    min,
    max,
    valueSuffix,
    disabled,
    handle,
    track,
    setProps
}) => {
    // Format the value to one decimal place for display
    const formattedValue = parseInt(value);
    const containerRef = useRef(null);

    const handleChange = (newValue) => {
        if (setProps) {
            // Round to one decimal place when updating value
            setProps({ value: parseFloat(parseFloat(newValue).toFixed(1)) });
        }
    };

    // Prevent negative SVG attributes by patching them after render
    useEffect(() => {
        const fixNegativeSVGAttributes = () => {
            if (!containerRef.current) return;

            // Find all SVG elements with potentially negative attributes
            const svgElements = containerRef.current.querySelectorAll('circle, rect');

            svgElements.forEach(el => {
                // Fix circle radius
                if (el.hasAttribute('r') && parseFloat(el.getAttribute('r')) < 0) {
                    el.setAttribute('r', '0');
                }

                // Fix rect width/height
                if (el.hasAttribute('width') && parseFloat(el.getAttribute('width')) < 0) {
                    el.setAttribute('width', '0');
                }

                if (el.hasAttribute('height') && parseFloat(el.getAttribute('height')) < 0) {
                    el.setAttribute('height', '0');
                }
            });
        };

        // Run the fix immediately after render and also set up a short timeout
        // to catch elements that might be rendered asynchronously
        fixNegativeSVGAttributes();
        const timeoutId = setTimeout(fixNegativeSVGAttributes, 100);

        // Cleanup
        return () => clearTimeout(timeoutId);
    });

    // Container style to ensure proper sizing and centering with minimum size constraints
    const containerStyle = {
        position: 'relative',
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        minWidth: '250px',  // Increased minimum width
        minHeight: '350px'  // Increased minimum height
    };

    return (
        <div
            id={id}
            className={className}
            style={{...style, minWidth: '250px', minHeight: '350px'}}
            ref={containerRef}
        >
            <div style={containerStyle}>
                <Thermostat
                    value={formattedValue}
                    min={min}
                    max={max}
                    valueSuffix={valueSuffix}
                    disabled={disabled}
                    handle={handle}
                    track={track}
                    onChange={handleChange}
                />
            </div>
        </div>
    );
};

DashThermostat.defaultProps = {
    min: 0,
    max: 100,
    valueSuffix: '°',
    disabled: false
};

DashThermostat.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The CSS class name for the component.
     */
    className: PropTypes.string,

    /**
     * Inline styles for the component.
     */
    style: PropTypes.object,

    /**
     * The current temperature value.
     */
    value: PropTypes.number.isRequired,

    /**
     * The minimum value of the thermostat.
     */
    min: PropTypes.number,

    /**
     * The maximum value of the thermostat.
     */
    max: PropTypes.number,

    /**
     * The suffix to display after the value (like °C, °F, etc).
     */
    valueSuffix: PropTypes.string,

    /**
     * Whether the thermostat is disabled.
     */
    disabled: PropTypes.bool,

    /**
     * Configuration for the handle.
     */
    handle: PropTypes.shape({
        size: PropTypes.number,
        colors: PropTypes.shape({
            handle: PropTypes.string,
            icon: PropTypes.string,
            pulse: PropTypes.string
        })
    }),

    /**
     * Configuration for the track.
     */
    track: PropTypes.shape({
        colors: PropTypes.arrayOf(PropTypes.string),
        thickness: PropTypes.number,
        markers: PropTypes.shape({
            enabled: PropTypes.bool,
            every: PropTypes.number,
            count: PropTypes.number,
            main: PropTypes.shape({
                color: PropTypes.string,
                length: PropTypes.number,
                thickness: PropTypes.number
            }),
            sub: PropTypes.shape({
                color: PropTypes.string,
                length: PropTypes.number,
                thickness: PropTypes.number
            })
        })
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashThermostat;