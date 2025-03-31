# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dash7SegmentDisplay <- function(id=NULL, backgroundColor=NULL, className=NULL, color=NULL, count=NULL, height=NULL, skew=NULL, style=NULL, value=NULL) {
    
    props <- list(id=id, backgroundColor=backgroundColor, className=className, color=color, count=count, height=height, skew=skew, style=style, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Dash7SegmentDisplay',
        namespace = 'dash_gauge',
        propNames = c('id', 'backgroundColor', 'className', 'color', 'count', 'height', 'skew', 'style', 'value'),
        package = 'dashGauge'
        )

    structure(component, class = c('dash_component', 'list'))
}
