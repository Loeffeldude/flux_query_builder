from flux_query_builder.functions.base import FluxQueryFunction

class Diff(FluxQueryFunction):
    """testing.diff() produces a diff between two streams.The function matches tables from each stream based on group keys.
For each matched table, it produces a diff.
Any added or removed rows are added to the table as a row.
An additional string column with the name diff is created and contains a
- if the row was present in the got table and not in the want table or
+ if the opposite is true.diff() function emits at least one row if the tables are
different and no rows if the tables are the same.
The exact diff produced may change.
diff() can be used to perform in-line diffs in a query.Stream containing data to test. Default is piped-forward data (<-).(Required)
Stream that contains data to test against.Specify how far apart two float values can be, but still considered equal. Defaults to 0.000000001.Include detailed differences in output. Default is false.Consider NaN float values equal. Default is false.

    Params:
        
        want 
        - (Required)
Stream that contains data to test against.
        
        got 
        - Stream containing data to test. Default is piped-forward data (<-).
        
        epsilon 
        - Specify how far apart two float values can be, but still considered equal. Defaults to 0.000000001.
        
        verbose 
        - Include detailed differences in output. Default is false.
        
        nansEqual 
        - Consider NaN float values equal. Default is false.
        
    """
    name = "diff"
    package="testing"

    def __init__(self, want, got=None, epsilon=None, verbose=None, nansEqual=None, ):
            super().__init__(want=want, got=got, epsilon=epsilon, verbose=verbose, nansEqual=nansEqual, )