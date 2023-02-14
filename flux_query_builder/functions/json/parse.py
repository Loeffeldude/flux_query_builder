from flux_query_builder.functions.base import FluxQueryFunction

class Parse(FluxQueryFunction):
    """json.parse() takes JSON data as bytes and returns a value.JSON types are converted to Flux types as follows:(Required)
JSON data (as bytes) to parse.

    Params:
        
        data 
        - (Required)
JSON data (as bytes) to parse.
        
    """
    name = "parse"
    package="json"

    def __init__(self, data, ):
            super().__init__(data=data, )