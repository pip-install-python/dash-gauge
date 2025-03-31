% Auto-generated: do not edit by hand
\name{dash7SegmentDisplay}

\alias{dash7SegmentDisplay}

\title{Dash7SegmentDisplay component}

\description{
Dash7SegmentDisplay is a Dash component that wraps the react-7-segment-display library. It renders numeric or hexadecimal values in a 7-segment display style. REVERTED: Padding/truncating logic removed. Back to basic string conversion.
}

\usage{
dash7SegmentDisplay(id=NULL, backgroundColor=NULL, className=NULL, color=NULL,
count=NULL, height=NULL, skew=NULL, style=NULL, value=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{backgroundColor}{Character. Color of the display background.}

\item{className}{Character. The CSS class name for the container component.}

\item{color}{Character. Color of the display segments when turned on.}

\item{count}{Numeric. Number of digits to display.}

\item{height}{Numeric. Total height of the display digits in pixels.}

\item{skew}{Logical. Whether the digits should be skewed (slanted).}

\item{style}{Named list. Inline styles for the container component.}

\item{value}{Character | numeric. The value to display. Can be a number (decimal) or a string (decimal or hexadecimal like "FF"). Null or undefined will result in a blank display.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

