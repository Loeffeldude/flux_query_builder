from flux_query_builder.functions.base import FluxQueryFunction

class Title(FluxQueryFunction):
    """strings.title() converts a string to title case.(Required)
String value to convert.

    Params:
        
        v 
        - (Required)
String value to convert.
        
    """
    name = "title"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )