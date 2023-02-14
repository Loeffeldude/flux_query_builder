from flux_query_builder.functions.base import FluxQueryFunction

class Duration(FluxQueryFunction):
    """duration() converts a value to a duration type.duration() treats integers and unsigned integers as nanoseconds.
For a string to be converted to a duration type, the string must use
duration literal representation.(Required)
Value to convert.Flux does not support duration column types.
To store durations in a column, convert duration types to strings.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "duration"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )