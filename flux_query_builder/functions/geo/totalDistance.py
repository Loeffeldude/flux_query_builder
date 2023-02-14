from flux_query_builder.functions.base import FluxQueryFunction

class TotalDistance(FluxQueryFunction):
    """geo.totalDistance() calculates the total distance covered by subsequent points
in each input table.Each row must contain lat (latitude) and lon (longitude) columns that
represent the geographic coordinates of the point.
Row sort order determines the order in which distance between points is calculated.
Use the geo.units option to specify the unit of distance to return (default is km).Total distance output column. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        outputColumn 
        - Total distance output column. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "totalDistance"
    package="geo"

    def __init__(self, outputColumn=None, tables=None, ):
            super().__init__(outputColumn=outputColumn, tables=tables, )