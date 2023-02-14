from flux_query_builder.functions.base import FluxQueryFunction

class Quantile(FluxQueryFunction):
    """quantile() returns rows from each input table with values that fall within a
specified quantile or returns the row with the value that represents the
specified quantile.quantile() supports columns with float values.quantile() acts as an aggregate or selector transformation depending on the
specified method.Column to use to compute the quantile. Default is _value.(Required)
Quantile to compute. Must be between 0.0 and 1.0.Computation method. Default is estimate_tdigest.Avaialable methods:Number of centroids to use when compressing the dataset.
Default is 1000.0.A larger number produces a more accurate result at the cost of increased
memory requirements.Input data. Default is piped-forward data (<-).

    Params:
        
        q 
        - (Required)
Quantile to compute. Must be between 0.0 and 1.0.
        
        column 
        - Column to use to compute the quantile. Default is _value.
        
        method 
        - Computation method. Default is estimate_tdigest.Avaialable methods:
        
        compression 
        - Number of centroids to use when compressing the dataset.
Default is 1000.0.A larger number produces a more accurate result at the cost of increased
memory requirements.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "quantile"
    package=None

    def __init__(self, q, column=None, method=None, compression=None, tables=None, ):
            super().__init__(q=q, column=column, method=method, compression=compression, tables=tables, )