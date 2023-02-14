from flux_query_builder.functions.base import FluxQueryFunction

class DedupKey(FluxQueryFunction):
    """pagerduty.dedupKey() uses the group key of an input table to generate and store a
deduplication key in the _pagerdutyDedupKeycolumn.
The function sorts, newline-concatenates, SHA256-hashes, and hex-encodes the
group key to create a unique deduplication key for each input table.Group key columns to exclude when generating the deduplication key.
Default is ["_start", “_stop”, “_level”].Input data. Default is piped-forward data (<-).

    Params:
        
        exclude 
        - Group key columns to exclude when generating the deduplication key.
Default is ["_start", “_stop”, “_level”].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "dedupKey"
    package="pagerduty"

    def __init__(self, exclude=None, tables=None, ):
            super().__init__(exclude=exclude, tables=tables, )