import React from 'react';
import PropTypes from 'prop-types';
import { Display } from 'react-7-segment-display';

/**
 * Dash7SegmentDisplay is a Dash component that wraps the react-7-segment-display library.
 * It renders numeric or hexadecimal values in a 7-segment display style.
 * REVERTED: Padding/truncating logic removed. Back to basic string conversion.
 */
const Dash7SegmentDisplay = ({
    id,
    className,
    style,
    value, // This can be string or number from Dash
    color,
    height,
    count,
    backgroundColor,
    skew,
    setProps
}) => {

    // Ensure the value passed to the underlying component is always a string.
    // Handle null, undefined, and explicitly convert numbers to strings.
    let displayValue = ''; // Default to empty string if value is null or undefined
    if (value !== null && value !== undefined) {
        displayValue = String(value); // Explicitly convert number or string input to string
    }

    // Basic container style
    const containerStyle = {
        display: 'inline-block',
        lineHeight: 0,
        ...style
    };

    // Defensive check: Don't render if count is zero or negative
    if (count <= 0) {
        return <div id={id} className={className} style={containerStyle}></div>;
    }

    // Render the component using the basic string-converted value.
    // Acknowledge that the underlying library might still throw internal errors (like the .map error)
    // if it doesn't handle certain values (like empty string '') gracefully internally.
    return (
        <div id={id} className={className} style={containerStyle}>
            <Display
                value={displayValue}
                color={color}
                height={height}
                count={count}
                backgroundColor={backgroundColor}
                skew={skew}
            />
        </div>
    );
};

Dash7SegmentDisplay.defaultProps = {
    value: '', // Default Dash value can be empty string
    color: 'red',
    height: 50,
    count: 2,
    backgroundColor: undefined,
    skew: false,
    className: '',
    style: {}
};

Dash7SegmentDisplay.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The CSS class name for the container component.
     */
    className: PropTypes.string,

    /**
     * Inline styles for the container component.
     */
    style: PropTypes.object,

    /**
     * The value to display. Can be a number (decimal) or a string (decimal or hexadecimal like "FF"). Null or undefined will result in a blank display.
     */
    value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]), // Keep accepting both from Dash

    /**
     * Color of the display segments when turned on.
     */
    color: PropTypes.string,

    /**
     * Total height of the display digits in pixels.
     */
    height: PropTypes.number,

    /**
     * Number of digits to display.
     */
    count: PropTypes.number,

    /**
     * Color of the display background.
     */
    backgroundColor: PropTypes.string,

    /**
     * Whether the digits should be skewed (slanted).
     */
    skew: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks. (Not typically used by this component).
     */
    setProps: PropTypes.func
};

export default Dash7SegmentDisplay;

