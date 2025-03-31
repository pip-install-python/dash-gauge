# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashRCJoystick <- function(id=NULL, angle=NULL, baseRadius=NULL, className=NULL, controllerClassName=NULL, controllerRadius=NULL, direction=NULL, directionCountMode=NULL, distance=NULL, insideMode=NULL, style=NULL, throttle=NULL) {
    
    props <- list(id=id, angle=angle, baseRadius=baseRadius, className=className, controllerClassName=controllerClassName, controllerRadius=controllerRadius, direction=direction, directionCountMode=directionCountMode, distance=distance, insideMode=insideMode, style=style, throttle=throttle)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashRCJoystick',
        namespace = 'dash_gauge',
        propNames = c('id', 'angle', 'baseRadius', 'className', 'controllerClassName', 'controllerRadius', 'direction', 'directionCountMode', 'distance', 'insideMode', 'style', 'throttle'),
        package = 'dashGauge'
        )

    structure(component, class = c('dash_component', 'list'))
}
