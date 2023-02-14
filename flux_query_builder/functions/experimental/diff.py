from flux_query_builder.functions.base import FluxQueryFunction

class Diff(FluxQueryFunction):
    """experimental.diff() takes two table streams as input and produces a diff.experimental.diff() compares tables with the same group key.
If compared tables are different, the function returns a table for that group key with one or more rows.
If there are no differences, the function does not return a table for that group key.Note: experimental.diff() cannot tell the difference between an empty table and a non-existent table.Important: The output format of the diff is not considered stable and the algorithm used to produce the diff may change.
The only guarantees are those mentioned above.(Required)
Input stream for the - side of the diff.Input stream for the + side of the diff.

    Params:
        
        want 
        - (Required)
Input stream for the - side of the diff.
        
        got 
        - Input stream for the + side of the diff.
        
    """
    name = "diff"
    package="experimental"

    def __init__(self, want, got=None, ):
            super().__init__(want=want, got=got, )