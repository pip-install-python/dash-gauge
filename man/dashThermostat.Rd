% Auto-generated: do not edit by hand
\name{dashThermostat}

\alias{dashThermostat}

\title{DashThermostat component}

\description{
DashThermostat is a Dash component that wraps the react-thermostat library. It provides an interactive thermostat control for temperature or other values.
}

\usage{
dashThermostat(id=NULL, className=NULL, disabled=NULL, handle=NULL,
max=NULL, min=NULL, style=NULL, track=NULL, value=NULL,
valueSuffix=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. The CSS class name for the component.}

\item{disabled}{Logical. Whether the thermostat is disabled.}

\item{handle}{Lists containing elements 'size', 'colors'.
those elements have the following types:
  - size (numeric; optional)
  - colors (optional): . colors has the following type: lists containing elements 'handle', 'icon', 'pulse'.
those elements have the following types:
  - handle (character; optional)
  - icon (character; optional)
  - pulse (character; optional). Configuration for the handle.}

\item{max}{Numeric. The maximum value of the thermostat.}

\item{min}{Numeric. The minimum value of the thermostat.}

\item{style}{Named list. Inline styles for the component.}

\item{track}{Lists containing elements 'colors', 'thickness', 'markers'.
those elements have the following types:
  - colors (list of characters; optional)
  - thickness (numeric; optional)
  - markers (optional): . markers has the following type: lists containing elements 'enabled', 'every', 'count', 'main', 'sub'.
those elements have the following types:
  - enabled (logical; optional)
  - every (numeric; optional)
  - count (numeric; optional)
  - main (optional): . main has the following type: lists containing elements 'color', 'length', 'thickness'.
those elements have the following types:
  - color (character; optional)
  - length (numeric; optional)
  - thickness (numeric; optional)
  - sub (optional): . sub has the following type: lists containing elements 'color', 'length', 'thickness'.
those elements have the following types:
  - color (character; optional)
  - length (numeric; optional)
  - thickness (numeric; optional). Configuration for the track.}

\item{value}{Numeric. The current temperature value.}

\item{valueSuffix}{Character. The suffix to display after the value (like °C, °F, etc).}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

