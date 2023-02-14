from flux_query_builder.functions.base import FluxQueryFunction

class Increase(FluxQueryFunction):
    """increase() returns the cumulative sum of non-negative differences between subsequent values.The primary use case for increase() is tracking changes in counter values
which may wrap overtime when they hit a threshold or are reset. In the case
of a wrap/reset, increase() assumes that the absolute delta between two
points is at least their non-negative difference.List of columns to operate on. Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - List of columns to operate on. Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "increase"
    package=None

    def __init__(self, columns=None, tables=None, ):
            super().__init__(columns=columns, tables=tables, )