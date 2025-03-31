// --- START OF FILE DashRCJoystick.react.js ---

import React from 'react';
import PropTypes from 'prop-types';
import Joystick, { DirectionCount, Direction } from 'rc-joystick'; // Import necessary items

/**
 * DashRCJoystick is a Dash component that wraps the rc-joystick library.
 * It provides an interactive joystick control.
 */
const DashRCJoystick = ({
    id,
    className,
    style,
    baseRadius,
    controllerRadius,
    controllerClassName,
    insideMode,
    throttle,
    directionCountMode, // Use a string prop for Dash compatibility
    // Output props updated via setProps
    angle,
    direction,
    distance,
    setProps
}) => {

    // Map the string prop 'directionCountMode' to the actual DirectionCount enum
    const getDirectionCountEnum = (mode) => {
        switch (mode) {
            case 'Nine':
                return DirectionCount.Nine;
            case 'Five':
            default:
                return DirectionCount.Five;
        }
    };

    const currentDirectionCount = getDirectionCountEnum(directionCountMode);

    const handleChange = (value) => {
        if (setProps) {
            // Map the Direction enum/string back to a simple string for Dash
            let directionString = value.direction;
            // Check if it's one of the Direction enum values (assuming they are strings)
            // Or handle potential numerical enums if necessary (less common in JS)
            if (typeof directionString !== 'string') {
                 // Attempt to convert common enum patterns or default
                 directionString = Direction[directionString] || String(directionString);
            }

            setProps({
                angle: value.angle,
                direction: directionString, // Send direction as a string
                distance: value.distance
            });
        }
    };

    // Basic container style for positioning if needed
    const containerStyle = {
        display: 'inline-block', // Or 'flex' with centering if desired
        position: 'relative', // Needed for joystick positioning
        ...style // Allow overriding with user style
    };

    return (
        <div id={id} className={className} style={containerStyle}>
            <Joystick
                baseRadius={baseRadius}
                controllerRadius={controllerRadius}
                controllerClassName={controllerClassName}
                insideMode={insideMode}
                throttle={throttle}
                directionCount={currentDirectionCount}
                onChange={handleChange}
                // renderController and renderArrows are omitted for simplicity
            />
        </div>
    );
};

DashRCJoystick.defaultProps = {
    baseRadius: 75,
    controllerRadius: 35,
    insideMode: false,
    throttle: 0,
    directionCountMode: 'Five', // Default to 'Five' as a string
    // Default values for output props (initial state)
    angle: undefined,
    direction: 'Center',
    distance: 0,
};

DashRCJoystick.propTypes = {
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
     * Joystick's base radius.
     */
    baseRadius: PropTypes.number,

    /**
     * Joystick controller's radius.
     */
    controllerRadius: PropTypes.number,

    /**
     * Joystick controller's extra className.
     */
    controllerClassName: PropTypes.string,

    /**
     * Controller will always be inside joystick's base if true.
     */
    insideMode: PropTypes.bool,

    /**
     * Throttle time for all change events (in milliseconds).
     */
    throttle: PropTypes.number,

    /**
     * Direction count mode: 'Five' or 'Nine'.
     * 'Five': Center, Right, Top, Left, Bottom
     * 'Nine': Center, Right, RightTop, Top, TopLeft, Left, LeftBottom, Bottom, BottomRight
     */
    directionCountMode: PropTypes.oneOf(['Five', 'Nine']),

    // Read-only props updated by the component

    /**
     * [Readonly] The current angle of the joystick controller (in degrees).
     * Undefined when the direction is 'Center'.
     */
    angle: PropTypes.number,

    /**
     * [Readonly] The current direction of the joystick controller.
     * Possible values depend on directionCountMode.
     */
    direction: PropTypes.string,

    /**
     * [Readonly] The current distance of the controller from the center.
     */
    distance: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashRCJoystick;

// --- END OF FILE DashRCJoystick.react.js ---