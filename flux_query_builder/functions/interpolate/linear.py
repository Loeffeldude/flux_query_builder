from flux_query_builder.functions.base import FluxQueryFunction

class Linear(FluxQueryFunction):
    """interpolate.linear() inserts rows at regular intervals using linear interpolation to
determine values for inserted rows.(Required)
Duration of time between interpolated points.Input data. Default is piped-forward data (<-).

    Params:
        
        every 
        - (Required)
Duration of time between interpolated points.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "linear"
    package="interpolate"

    def __init__(self, every, tables=None, ):
            super().__init__(every=every, tables=tables, )