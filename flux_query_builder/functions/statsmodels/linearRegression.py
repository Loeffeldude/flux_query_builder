from flux_query_builder.functions.base import FluxQueryFunction

class LinearRegression(FluxQueryFunction):
    """statsmodels.linearRegression() performs a linear regression.It calculates and returns ŷ (y_hat),
and residual sum of errors (rse).
Output data includes the following columns:Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "linearRegression"
    package="statsmodels"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )