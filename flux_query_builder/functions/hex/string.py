from flux_query_builder.functions.base import FluxQueryFunction

class String(FluxQueryFunction):
    """hex.string() converts a Flux basic type to a hexadecimal string.The function is similar to string(), but encodes int, uint, and bytes
types to hexadecimal lowercase characters.(Required)
Value to convert.Use map() to iterate over and update all input rows.
Use hex.string() to update the value of a column.
The following example uses data provided by the sampledata package.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "string"
    package="hex"

    def __init__(self, v, ):
            super().__init__(v=v, )