from flux_query_builder.functions.base import FluxQueryFunction

class Median(FluxQueryFunction):
    """median() returns the median _value of an input table or all non-null records
in the input table with values that fall within the 0.5 quantile (50th percentile).median() acts as an aggregate or selector transformation depending on the
specified method.Column to use to compute the median. Default is _value.Computation method. Default is estimate_tdigest.Avaialable methods:Number of centroids to use when compressing the dataset.
Default is 0.0.A larger number produces a more accurate result at the cost of increased
memory requirements.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to use to compute the median. Default is _value.
        
        method 
        - Computation method. Default is estimate_tdigest.Avaialable methods:
        
        compression 
        - Number of centroids to use when compressing the dataset.
Default is 0.0.A larger number produces a more accurate result at the cost of increased
memory requirements.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "median"
    package=None

    def __init__(self, column=None, method=None, compression=None, tables=None, ):
            super().__init__(column=column, method=method, compression=compression, tables=tables, )