from flux_query_builder.functions.base import FluxQueryFunction

class Count(FluxQueryFunction):
    """count() returns the number of records in each input table.The function counts both null and non-null records.count() returns 0 for empty tables.
To keep empty tables in your data, set the following parameters for the
following functions:Column to count values in and store the total count.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to count values in and store the total count.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "count"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )