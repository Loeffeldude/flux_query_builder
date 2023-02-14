from flux_query_builder.functions.base import FluxQueryFunction

class ToTitle(FluxQueryFunction):
    """strings.toTitle() converts all characters in a string to title case.The results of toTitle() and toUpper() are often the same, however the
difference is visible when using special characters:(Required)
String value to convert.

    Params:
        
        v 
        - (Required)
String value to convert.
        
    """
    name = "toTitle"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )