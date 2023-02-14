from flux_query_builder.functions.base import FluxQueryFunction

class Quantile(FluxQueryFunction):
    """experimental.quantile() returns non-null records with values in the _value column that
fall within the specified quantile or represent the specified quantile.The _value column must contain float values.experimental.quantile() behaves like an aggregate function or a
selector function depending on the method parameter.
The following computation methods are available:An aggregate method that uses a t-digest data structure
to compute an accurate quantile estimate on large data sources.
When used, experimental.quantile() outputs non-null records with values
that fall within the specified quantile.An aggregate method that takes the average of the two points closest to the quantile value.
When used, experimental.quantile() outputs non-null records with values
that fall within the specified quantile.A selector method that returns the data point for which at least q points are less than.
When used, experimental.quantile() outputs the non-null record with the
value that represents the specified quantile.(Required)
Quantile to compute ([0 - 1]).Computation method. Default is estimate_tdigest.Supported methods:Number of centroids to use when compressing the dataset.
Default is 1000.0.A larger number produces a more accurate result at the cost of increased
memory requirements.Input data. Default is piped-forward data (<-).

    Params:
        
        q 
        - (Required)
Quantile to compute ([0 - 1]).
        
        method 
        - Computation method. Default is estimate_tdigest.Supported methods:
        
        compression 
        - Number of centroids to use when compressing the dataset.
Default is 1000.0.A larger number produces a more accurate result at the cost of increased
memory requirements.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "quantile"
    package="experimental"

    def __init__(self, q, method=None, compression=None, tables=None, ):
            super().__init__(q=q, method=method, compression=compression, tables=tables, )