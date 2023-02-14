from flux_query_builder.functions.base import FluxQueryFunction

class LinearRegression(FluxQueryFunction):
    """promql.linearRegression() implements linear regression functionality required to implement
PromQL’s deriv()
and predict_linear() functions.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).Output should contain a prediction.Time as a floating point value.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        predict 
        - Output should contain a prediction.
        
        fromNow 
        - Time as a floating point value.
        
    """
    name = "linearRegression"
    package="promql"

    def __init__(self, tables=None, predict=None, fromNow=None, ):
            super().__init__(tables=tables, predict=predict, fromNow=fromNow, )