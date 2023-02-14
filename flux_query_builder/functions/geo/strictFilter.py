from flux_query_builder.functions.base import FluxQueryFunction

class StrictFilter(FluxQueryFunction):
    """geo.strictFilter() filters data by latitude and longitude in a specified region.This filter is more strict than geo.gridFilter(), but for the best performance,
use geo.strictFilter() after geo.gridFilter().
Input rows must have lat and lon columns.(Required)
Region containing the desired data points.Specify record properties for the shape.Input data. Default is piped-forward data (<-).

    Params:
        
        region 
        - (Required)
Region containing the desired data points.Specify record properties for the shape.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "strictFilter"
    package="geo"

    def __init__(self, region, tables=None, ):
            super().__init__(region=region, tables=tables, )