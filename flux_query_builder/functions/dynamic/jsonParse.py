from flux_query_builder.functions.base import FluxQueryFunction

class JsonParse(FluxQueryFunction):
    """dynamic.jsonParse() takes JSON data as bytes and returns dynamic values.JSON input is converted to dynamic-typed values which may be converted to
a statically typed value with dynamic.asArray() or casting functions in the dynamic package.(Required)
JSON data (as bytes) to parse.

    Params:
        
        data 
        - (Required)
JSON data (as bytes) to parse.
        
    """
    name = "jsonParse"
    package="dynamic"

    def __init__(self, data, ):
            super().__init__(data=data, )