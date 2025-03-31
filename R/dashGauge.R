# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashGauge <- function(id=NULL, arc=NULL, className=NULL, componentPath=NULL, labels=NULL, marginInPercent=NULL, maxValue=NULL, minValue=NULL, pointer=NULL, style=NULL, type=NULL, value=NULL) {
    
    props <- list(id=id, arc=arc, className=className, componentPath=componentPath, labels=labels, marginInPercent=marginInPercent, maxValue=maxValue, minValue=minValue, pointer=pointer, style=style, type=type, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashGauge',
        namespace = 'dash_gauge',
        propNames = c('id', 'arc', 'className', 'componentPath', 'labels', 'marginInPercent', 'maxValue', 'minValue', 'pointer', 'style', 'type', 'value'),
        package = 'dashGauge'
        )

    structure(component, class = c('dash_component', 'list'))
}
