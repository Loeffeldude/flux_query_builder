from flux_query_builder.functions.base import FluxQueryFunction

class ST_LineString(FluxQueryFunction):
    """geo.ST_LineString() converts a series of geographic points into linestring.Group data into meaningful, ordered paths to before converting to linestring.
Rows in each table must have lat and lon columns.
Output tables contain a single row with a st_linestring column containing
the resulting linestring.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "ST_LineString"
    package="geo"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )