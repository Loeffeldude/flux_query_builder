from flux_query_builder.functions.base import FluxQueryFunction

class String(FluxQueryFunction):
    """string() converts a value to a string type.(Required)
Value to convert.If converting the _value column to string types, use toString().
If converting columns other than _value, use map() to iterate over each
row and string() to covert a column value to a string type.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "string"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )