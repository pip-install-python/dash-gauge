# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashRotaryKnob <- function(id=NULL, className=NULL, format=NULL, max=NULL, min=NULL, preciseMode=NULL, skinName=NULL, step=NULL, style=NULL, unlockDistance=NULL, value=NULL) {
    
    props <- list(id=id, className=className, format=format, max=max, min=min, preciseMode=preciseMode, skinName=skinName, step=step, style=style, unlockDistance=unlockDistance, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashRotaryKnob',
        namespace = 'dash_gauge',
        propNames = c('id', 'className', 'format', 'max', 'min', 'preciseMode', 'skinName', 'step', 'style', 'unlockDistance', 'value'),
        package = 'dashGauge'
        )

    structure(component, class = c('dash_component', 'list'))
}
