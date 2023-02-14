from flux_query_builder.functions.base import FluxQueryFunction

class SqlInterval(FluxQueryFunction):
    """iox.sqlInterval() converts a duration value to a SQL interval string.SQL interval strings support down to millisecond precision.
Any microsecond or nanosecond duration units are dropped from the duration value.
If the duration only consists of microseconds or nanosecond units,
iox.sqlInterval() returns 1 millisecond.
Duration values must be positive to work as a SQL interval string.(Required)
Duration value to convert to SQL interval string.

    Params:
        
        d 
        - (Required)
Duration value to convert to SQL interval string.
        
    """
    name = "sqlInterval"
    package="iox"

    def __init__(self, d, ):
            super().__init__(d=d, )