from flux_query_builder.functions.base import FluxQueryFunction

class Cov(FluxQueryFunction):
    """cov() computes the covariance between two streams of tables.(Required)
First input stream.(Required)
Second input stream.(Required)
List of columns to join on.Normalize results to the Pearson R coefficient. Default is false.

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
        
        pearsonr 
        - Normalize results to the Pearson R coefficient. Default is false.
        
    """
    name = "cov"
    package=None

    def __init__(self, x, y, on, pearsonr=None, ):
            super().__init__(x=x, y=y, on=on, pearsonr=pearsonr, )