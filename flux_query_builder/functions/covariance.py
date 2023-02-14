from flux_query_builder.functions.base import FluxQueryFunction

class Covariance(FluxQueryFunction):
    """covariance() computes the covariance between two columns.(Required)
List of two columns to operate on.Normalize results to the Pearson R coefficient. Default is false.Column to store the result in. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - (Required)
List of two columns to operate on.
        
        pearsonr 
        - Normalize results to the Pearson R coefficient. Default is false.
        
        valueDst 
        - Column to store the result in. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "covariance"
    package=None

    def __init__(self, columns, pearsonr=None, valueDst=None, tables=None, ):
            super().__init__(columns=columns, pearsonr=pearsonr, valueDst=valueDst, tables=tables, )