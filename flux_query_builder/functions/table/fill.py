from flux_query_builder.functions.base import FluxQueryFunction

class Fill(FluxQueryFunction):
    """table.fill() adds a single row to empty tables in a stream of tables.Columns that are in the group key are filled with the column value defined in the group key.
Columns not in the group key are filled with a null value.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "fill"
    package="table"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )