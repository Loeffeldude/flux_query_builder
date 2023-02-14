from flux_query_builder.functions.base import FluxQueryFunction

class QuoteMeta(FluxQueryFunction):
    """regexp.quoteMeta() escapes all regular expression metacharacters in a string.(Required)
String that contains regular expression metacharacters to escape.

    Params:
        
        v 
        - (Required)
String that contains regular expression metacharacters to escape.
        
    """
    name = "quoteMeta"
    package="regexp"

    def __init__(self, v, ):
            super().__init__(v=v, )