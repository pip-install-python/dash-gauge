# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashThermostat <- function(id=NULL, className=NULL, disabled=NULL, handle=NULL, max=NULL, min=NULL, style=NULL, track=NULL, value=NULL, valueSuffix=NULL) {
    
    props <- list(id=id, className=className, disabled=disabled, handle=handle, max=max, min=min, style=style, track=track, value=value, valueSuffix=valueSuffix)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashThermostat',
        namespace = 'dash_gauge',
        propNames = c('id', 'className', 'disabled', 'handle', 'max', 'min', 'style', 'track', 'value', 'valueSuffix'),
        package = 'dashGauge'
        )

    structure(component, class = c('dash_component', 'list'))
}
