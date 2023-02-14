from flux_query_builder.functions.base import FluxQueryFunction

class Yield(FluxQueryFunction):
    """yield() delivers input data as a result of the query.A query may have multiple yields, each identified by unique name specified in
the name parameter.Note: yield() is implicit for queries that output a single stream of
tables and is only necessary when yielding multiple results from a query.Unique name for the yielded results. Default is _results.Input data. Default is piped-forward data (<-).

    Params:
        
        name 
        - Unique name for the yielded results. Default is _results.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "yield"
    package=None

    def __init__(self, name=None, tables=None, ):
            super().__init__(name=name, tables=tables, )