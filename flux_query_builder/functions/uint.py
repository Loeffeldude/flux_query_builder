from flux_query_builder.functions.base import FluxQueryFunction

class Uint(FluxQueryFunction):
    """uint() converts a value to an unsigned integer type.uint() behavior depends on the input data type:(Required)
Value to convert.If converting the _value column to uint types, use toUInt().
If converting columns other than _value, use map() to iterate over each
row and uint() to covert a column value to a uint type.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "uint"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )