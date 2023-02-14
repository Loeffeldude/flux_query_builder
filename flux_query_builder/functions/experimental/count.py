from flux_query_builder.functions.base import FluxQueryFunction

class Count(FluxQueryFunction):
    """experimental.count() returns the number of records in each input table.The count is returned in the _value column and counts both null and non-null records.experimental.count() returns 0 for empty tables.
To keep empty tables in your data, set the following parameters when using
the following functions:Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "count"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )