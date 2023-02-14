from flux_query_builder.functions.base import FluxQueryFunction

class ToUpper(FluxQueryFunction):
    """strings.toUpper() converts a string to uppercase.The results of toUpper() and toTitle() are often the same, however the
difference is visible when using special characters:(Required)
String value to convert.

    Params:
        
        v 
        - (Required)
String value to convert.
        
    """
    name = "toUpper"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )