import React from 'react';
import PropTypes from 'prop-types';
import { Knob } from 'react-rotary-knob';
import * as skinPack from './knob-skins-full';

const DashRotaryKnob = ({
    id,
    className,
    style,
    value,
    min,
    max,
    step,
    skinName,
    format,
    preciseMode,
    unlockDistance,
    setProps
}) => {
    const skin = skinPack.getSkin(skinName);

    const handleChange = (newValue) => {
        if (setProps) {
            setProps({ value: newValue });
        }
    };

    // Ensure the knob container is properly centered
    const containerStyle = {
        position: 'relative',
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
    };

    return (
        <div id={id} className={className} style={style}>
            <div style={containerStyle}>
                <Knob
                    value={value}
                    min={min}
                    max={max}
                    step={step}
                    skin={skin}
                    preciseMode={preciseMode}
                    unlockDistance={unlockDistance}
                    onChange={handleChange}
                />
            </div>
        </div>
    );
};

DashRotaryKnob.propTypes = {
    id: PropTypes.string,
    className: PropTypes.string,
    style: PropTypes.object,
    value: PropTypes.number,
    min: PropTypes.number,
    max: PropTypes.number,
    step: PropTypes.number,
    skinName: PropTypes.string,
    format: PropTypes.string,
    preciseMode: PropTypes.bool,
    unlockDistance: PropTypes.number,
    setProps: PropTypes.func
};

export default DashRotaryKnob;