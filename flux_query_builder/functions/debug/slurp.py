from flux_query_builder.functions.base import FluxQueryFunction

class Slurp(FluxQueryFunction):
    """debug.slurp() will read the incoming tables and concatenate buffers with the same group key
into a single in memory table buffer. This is useful for testing the performance impact of multiple
buffers versus a single buffer.Stream to consume into single buffers per table.

    Params:
        
        tables 
        - Stream to consume into single buffers per table.
        
    """
    name = "slurp"
    package="debug"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )