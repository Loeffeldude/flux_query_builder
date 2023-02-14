from flux_query_builder.functions.base import FluxQueryFunction

class Pearsonr(FluxQueryFunction):
    """pearsonr() returns the covariance of two streams of tables normalized to the
Pearson R coefficient.(Required)
First input stream.(Required)
Second input stream.(Required)
List of columns to join on.

    Params:
        
        x 
        - (Required)
First input stream.
        
        y 
        - (Required)
Second input stream.
        
        on 
        - (Required)
List of columns to join on.
        
    """
    name = "pearsonr"
    package=None

    def __init__(self, x, y, on, ):
            super().__init__(x=x, y=y, on=on, )