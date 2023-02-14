from flux_query_builder.functions.base import FluxQueryFunction

class AsTracks(FluxQueryFunction):
    """geo.asTracks() groups rows into tracks (sequential, related data points).Columns to group by. These columns should uniquely identify each track.
Default is ["id","tid"].Columns to order results by. Default is ["_time"].Sort precedence is determined by list order (left to right).Input data. Default is piped-forward data (<-).

    Params:
        
        groupBy 
        - Columns to group by. These columns should uniquely identify each track.
Default is ["id","tid"].
        
        orderBy 
        - Columns to order results by. Default is ["_time"].Sort precedence is determined by list order (left to right).
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "asTracks"
    package="geo"

    def __init__(self, groupBy=None, orderBy=None, tables=None, ):
            super().__init__(groupBy=groupBy, orderBy=orderBy, tables=tables, )