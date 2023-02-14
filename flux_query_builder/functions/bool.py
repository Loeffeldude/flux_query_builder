from flux_query_builder.functions.base import FluxQueryFunction

class Bool(FluxQueryFunction):
    """bool() converts a value to a boolean type.(Required)
Value to convert.If converting the _value column to boolean types, use toBool().
If converting columns other than _value, use map() to iterate over each
row and bool() to covert a column value to a boolean type.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "bool"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )