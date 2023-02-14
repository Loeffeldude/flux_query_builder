from flux_query_builder.functions.base import FluxQueryFunction

class Tables(FluxQueryFunction):
    """gen.tables() generates a stream of table data.(Required)
Number of rows to generate.Percentage chance that a null value will be used in the input. Valid value range is [0.0 - 1.0].Set of tags with their cardinality to generate.Pass seed to tables generator to get the very same sequence each time.

    Params:
        
        n 
        - (Required)
Number of rows to generate.
        
        nulls 
        - Percentage chance that a null value will be used in the input. Valid value range is [0.0 - 1.0].
        
        tags 
        - Set of tags with their cardinality to generate.
        
        seed 
        - Pass seed to tables generator to get the very same sequence each time.
        
    """
    name = "tables"
    package="gen"

    def __init__(self, n, nulls=None, tags=None, seed=None, ):
            super().__init__(n=n, nulls=nulls, tags=tags, seed=seed, )