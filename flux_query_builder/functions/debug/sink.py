from flux_query_builder.functions.base import FluxQueryFunction

class Sink(FluxQueryFunction):
    """debug.sink() will discard all data that comes into it.Stream to discard.

    Params:
        
        tables 
        - Stream to discard.
        
    """
    name = "sink"
    package="debug"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )