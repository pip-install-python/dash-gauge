const config = require('./webpack.config.js');
const path = require('path');

config.entry = {main: './src/demo/knob-skins.js'};
config.output = {
    filename: './output.js',
    path: path.resolve(__dirname),
};
config.mode = 'development';
config.externals = undefined; // eslint-disable-line
config.devtool = 'inline-source-map';
module.exports = config;
