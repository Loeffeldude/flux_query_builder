from flux_query_builder.functions.base import FluxQueryFunction

class Time(FluxQueryFunction):
    """time() converts a value to a time type.(Required)
Value to convert.Strings must be valid RFC3339 timestamps.
Integer and unsigned integer values are parsed as nanosecond epoch timestamps.If converting the _value column to time types, use toTime().
If converting columns other than _value, use map() to iterate over each
row and time() to covert a column value to a time type.

    Params:
        
        v 
        - (Required)
Value to convert.Strings must be valid RFC3339 timestamps.
Integer and unsigned integer values are parsed as nanosecond epoch timestamps.
        
    """
    name = "time"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )