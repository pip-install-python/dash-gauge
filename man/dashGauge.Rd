% Auto-generated: do not edit by hand
\name{dashGauge}

\alias{dashGauge}

\title{DashGauge component}

\description{
DashGauge is a Dash component that wraps the react-gauge-component library. It creates customizable gauge charts for data visualization.
}

\usage{
dashGauge(id=NULL, arc=NULL, className=NULL, componentPath=NULL,
labels=NULL, marginInPercent=NULL, maxValue=NULL,
minValue=NULL, pointer=NULL, style=NULL, type=NULL,
value=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{arc}{Lists containing elements 'cornerradius', 'padding', 'width', 'nbsubarcs', 'gradient', 'colorarray', 'emptycolor', 'subarcs'.
those elements have the following types:
  - cornerradius (numeric; optional)
  - padding (numeric; optional)
  - width (numeric; optional)
  - nbsubarcs (numeric; optional)
  - gradient (logical; optional)
  - colorarray (list of characters; optional)
  - emptycolor (character; optional)
  - subarcs (optional): . subarcs has the following type: list of lists containing elements 'limit', 'color', 'length', 'showtick', 'tooltip'.
those elements have the following types:
  - limit (numeric; optional)
  - color (character; optional)
  - length (numeric; optional)
  - showtick (logical; optional)
  - tooltip (optional): . tooltip has the following type: lists containing elements 'text', 'style'.
those elements have the following types:
  - text (character; optional)
  - style (named list; optional)s. Configuration for the arc of the gauge}

\item{className}{Character. CSS class name for the component}

\item{componentPath}{Character. Component path for internal Dash handling}

\item{labels}{Lists containing elements 'valuelabel', 'ticklabels'.
those elements have the following types:
  - valuelabel (optional): . valuelabel has the following type: lists containing elements 'formattextvalue', 'matchcolorwitharc', 'maxdecimaldigits', 'style', 'hide'.
those elements have the following types:
  - formattextvalue (optional)
  - matchcolorwitharc (logical; optional)
  - maxdecimaldigits (numeric; optional)
  - style (named list; optional)
  - hide (logical; optional)
  - ticklabels (optional): . ticklabels has the following type: lists containing elements 'hideminmax', 'type', 'ticks', 'defaulttickvalueconfig', 'defaultticklineconfig'.
those elements have the following types:
  - hideminmax (logical; optional)
  - type (a value equal to: "inner", "outer"; optional)
  - ticks (optional): . ticks has the following type: list of lists containing elements 'value', 'valueconfig', 'lineconfig'.
those elements have the following types:
  - value (numeric; optional)
  - valueconfig (named list; optional)
  - lineconfig (named list; optional)s
  - defaulttickvalueconfig (named list; optional)
  - defaultticklineconfig (named list; optional). Configuration for the labels of the gauge}

\item{marginInPercent}{Numeric | lists containing elements 'top', 'bottom', 'left', 'right'.
those elements have the following types:
  - top (numeric; optional)
  - bottom (numeric; optional)
  - left (numeric; optional)
  - right (numeric; optional). Sets the margin for the chart inside the containing SVG element}

\item{maxValue}{Numeric. The maximum value of the gauge}

\item{minValue}{Numeric. The minimum value of the gauge}

\item{pointer}{Lists containing elements 'type', 'color', 'hide', 'basecolor', 'length', 'width', 'animate', 'elastic', 'animationduration', 'animationdelay', 'strokewidth'.
those elements have the following types:
  - type (a value equal to: "needle", "blob", "arrow"; optional)
  - color (character; optional)
  - hide (logical; optional)
  - basecolor (character; optional)
  - length (numeric; optional)
  - width (numeric; optional)
  - animate (logical; optional)
  - elastic (logical; optional)
  - animationduration (numeric; optional)
  - animationdelay (numeric; optional)
  - strokewidth (numeric; optional). Configuration for the pointer of the gauge}

\item{style}{Named list. Inline style for the component}

\item{type}{A value equal to: "grafana", "semicircle", "radial". The type of the gauge. Can be "grafana", "semicircle" or "radial"}

\item{value}{Numeric. The value of the gauge}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

