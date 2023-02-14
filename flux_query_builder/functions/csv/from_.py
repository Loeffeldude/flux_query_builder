from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """csv.from() retrieves annotated CSV from a URL.Note: Experimental csv.from() is an alternative to the standard
csv.from() function.(Required)
URL to retrieve annotated CSV from.

    Params:
        
        url 
        - (Required)
URL to retrieve annotated CSV from.
        
    """
    name = "from"
    package="csv"

    def __init__(self, url, ):
            super().__init__(url=url, )