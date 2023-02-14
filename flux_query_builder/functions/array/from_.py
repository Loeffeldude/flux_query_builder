from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """array.from() constructs a table from an array of records.Each record in the array is converted into an output row or record. All
records must have the same keys and data types.Array of records to construct a table with.

    Params:
        
        rows 
        - Array of records to construct a table with.
        
    """
    name = "from"
    package="array"

    def __init__(self, rows=None, ):
            super().__init__(rows=rows, )