from flux_query_builder.functions.base import FluxQueryFunction

class GetString(FluxQueryFunction):
    """regexp.getString() returns the source string used to compile a regular expression.(Required)
Regular expression object to convert to a string.

    Params:
        
        r 
        - (Required)
Regular expression object to convert to a string.
        
    """
    name = "getString"
    package="regexp"

    def __init__(self, r, ):
            super().__init__(r=r, )