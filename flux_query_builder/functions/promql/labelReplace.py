from flux_query_builder.functions.base import FluxQueryFunction

class LabelReplace(FluxQueryFunction):
    """promql.labelReplace() implements functionality equivalent to
PromQL’s label_replace() function.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).(Required)
Input label.(Required)
Output label.(Required)
Pattern as a regex string.(Required)
Replacement value.

    Params:
        
        source 
        - (Required)
Input label.
        
        destination 
        - (Required)
Output label.
        
        regex 
        - (Required)
Pattern as a regex string.
        
        replacement 
        - (Required)
Replacement value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "labelReplace"
    package="promql"

    def __init__(self, source, destination, regex, replacement, tables=None, ):
            super().__init__(source=source, destination=destination, regex=regex, replacement=replacement, tables=tables, )