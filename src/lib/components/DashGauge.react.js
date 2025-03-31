import React from 'react';
import PropTypes from 'prop-types';
import GaugeComponent from 'react-gauge-component';

/**
 * DashGauge is a Dash component that wraps the react-gauge-component library.
 * It creates customizable gauge charts for data visualization.
 */
const DashGauge = ({
    id,
    className = "dash-gauge-component",
    style = {},
    type = "grafana",
    marginInPercent,
    value = 33,
    minValue = 0,
    maxValue = 100,
    arc = {},
    pointer = {},
    labels = {},
    setProps,
    componentPath
}) => {
    // Handle value changes if it's intended to be interactive
    const handleValueChange = (newValue) => {
        if (setProps) {
            setProps({ value: newValue });
        }
    };

    // Merging default props with user-provided props
    const gaugeProps = {
        id,
        className,
        style,
        type,
        marginInPercent,
        value,
        minValue,
        maxValue,
        arc,
        pointer,
        labels
    };

    // Filter out undefined props
    Object.keys(gaugeProps).forEach(key => {
        if (gaugeProps[key] === undefined) {
            delete gaugeProps[key];
        }
    });

    return (
        <GaugeComponent
            {...gaugeProps}
        />
    );
};

DashGauge.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

    /**
     * Component path for internal Dash handling
     */
    componentPath: PropTypes.string,

    /**
     * CSS class name for the component
     */
    className: PropTypes.string,

    /**
     * Inline style for the component
     */
    style: PropTypes.object,

    /**
     * The type of the gauge. Can be "grafana", "semicircle" or "radial"
     */
    type: PropTypes.oneOf(["grafana", "semicircle", "radial"]),

    /**
     * Sets the margin for the chart inside the containing SVG element
     */
    marginInPercent: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.shape({
            top: PropTypes.number,
            bottom: PropTypes.number,
            left: PropTypes.number,
            right: PropTypes.number
        })
    ]),

    /**
     * The value of the gauge
     */
    value: PropTypes.number,

    /**
     * The minimum value of the gauge
     */
    minValue: PropTypes.number,

    /**
     * The maximum value of the gauge
     */
    maxValue: PropTypes.number,

    /**
     * Configuration for the arc of the gauge
     */
    arc: PropTypes.shape({
        cornerRadius: PropTypes.number,
        padding: PropTypes.number,
        width: PropTypes.number,
        nbSubArcs: PropTypes.number,
        gradient: PropTypes.bool,
        colorArray: PropTypes.arrayOf(PropTypes.string),
        emptyColor: PropTypes.string,
        subArcs: PropTypes.arrayOf(PropTypes.shape({
            limit: PropTypes.number,
            color: PropTypes.string,
            length: PropTypes.number,
            showTick: PropTypes.bool,
            tooltip: PropTypes.shape({
                text: PropTypes.string,
                style: PropTypes.object
            })
        }))
    }),

    /**
     * Configuration for the pointer of the gauge
     */
    pointer: PropTypes.shape({
        type: PropTypes.oneOf(["needle", "blob", "arrow"]),
        color: PropTypes.string,
        hide: PropTypes.bool,
        baseColor: PropTypes.string,
        length: PropTypes.number,
        width: PropTypes.number,
        animate: PropTypes.bool,
        elastic: PropTypes.bool,
        animationDuration: PropTypes.number,
        animationDelay: PropTypes.number,
        strokeWidth: PropTypes.number
    }),

    /**
     * Configuration for the labels of the gauge
     */
    labels: PropTypes.shape({
        valueLabel: PropTypes.shape({
            formatTextValue: PropTypes.func,
            matchColorWithArc: PropTypes.bool,
            maxDecimalDigits: PropTypes.number,
            style: PropTypes.object,
            hide: PropTypes.bool
        }),
        tickLabels: PropTypes.shape({
            hideMinMax: PropTypes.bool,
            type: PropTypes.oneOf(["inner", "outer"]),
            ticks: PropTypes.arrayOf(PropTypes.shape({
                value: PropTypes.number,
                valueConfig: PropTypes.object,
                lineConfig: PropTypes.object
            })),
            defaultTickValueConfig: PropTypes.object,
            defaultTickLineConfig: PropTypes.object
        })
    })
};

export default DashGauge;
