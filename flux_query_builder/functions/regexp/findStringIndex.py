from flux_query_builder.functions.base import FluxQueryFunction

class FindStringIndex(FluxQueryFunction):
    """regexp.findStringIndex() returns a two-element array of integers that represent the
beginning and ending indexes of the first regular expression match in a string.(Required)
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
    name = "findStringIndex"
    package="regexp"

    def __init__(self, r, v, ):
            super().__init__(r=r, v=v, )