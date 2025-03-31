% Auto-generated: do not edit by hand
\name{dashRCJoystick}

\alias{dashRCJoystick}

\title{DashRCJoystick component}

\description{
DashRCJoystick is a Dash component that wraps the rc-joystick library. It provides an interactive joystick control.
}

\usage{
dashRCJoystick(id=NULL, angle=NULL, baseRadius=NULL, className=NULL,
controllerClassName=NULL, controllerRadius=NULL,
direction=NULL, directionCountMode=NULL, distance=NULL,
insideMode=NULL, style=NULL, throttle=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{angle}{Numeric. [Readonly] The current angle of the joystick controller (in degrees).
Undefined when the direction is 'Center'.}

\item{baseRadius}{Numeric. Joystick's base radius.}

\item{className}{Character. The CSS class name for the container component.}

\item{controllerClassName}{Character. Joystick controller's extra className.}

\item{controllerRadius}{Numeric. Joystick controller's radius.}

\item{direction}{Character. [Readonly] The current direction of the joystick controller.
Possible values depend on directionCountMode.}

\item{directionCountMode}{A value equal to: 'five', 'nine'. Direction count mode: 'Five' or 'Nine'.
'Five': Center, Right, Top, Left, Bottom
'Nine': Center, Right, RightTop, Top, TopLeft, Left, LeftBottom, Bottom, BottomRight}

\item{distance}{Numeric. [Readonly] The current distance of the controller from the center.}

\item{insideMode}{Logical. Controller will always be inside joystick's base if true.}

\item{style}{Named list. Inline styles for the container component.}

\item{throttle}{Numeric. Throttle time for all change events (in milliseconds).}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

