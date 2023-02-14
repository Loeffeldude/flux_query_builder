from flux_query_builder.functions.base import FluxQueryFunction

class Float(FluxQueryFunction):
    """float() converts a value to a float type.(Required)
Value to convert.If converting the _value column to float types, use toFloat().
If converting columns other than _value, use map() to iterate over each
row and float() to covert a column value to a float type.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "float"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )