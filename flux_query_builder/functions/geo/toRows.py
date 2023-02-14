from flux_query_builder.functions.base import FluxQueryFunction

class ToRows(FluxQueryFunction):
    """geo.toRows() pivots fields into columns based on time.Latitude and longitude should be stored as fields in InfluxDB.
Because most geo package transformation functions require rows to have
lat and lon columns, lat and lot fields must be pivoted into columns.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toRows"
    package="geo"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )