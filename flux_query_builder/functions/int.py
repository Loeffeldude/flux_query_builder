from flux_query_builder.functions.base import FluxQueryFunction

class Int(FluxQueryFunction):
    """int() converts a value to an integer type.int() behavior depends on the input data type:(Required)
Value to convert.If converting the _value column to integer types, use toInt().
If converting columns other than _value, use map() to iterate over each
row and int() to covert a column value to a integer type.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "int"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )