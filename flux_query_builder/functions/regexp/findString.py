from flux_query_builder.functions.base import FluxQueryFunction

class FindString(FluxQueryFunction):
    """regexp.findString() returns the left-most regular expression match in a string.(Required)
Regular expression used to search v.(Required)
String value to search.

    Params:
        
        r 
        - (Required)
Regular expression used to search v.
        
        v 
        - (Required)
String value to search.
        
    """
    name = "findString"
    package="regexp"

    def __init__(self, r, v, ):
            super().__init__(r=r, v=v, )