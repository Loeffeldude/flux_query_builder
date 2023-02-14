from flux_query_builder.functions.base import FluxQueryFunction

class GridFilter(FluxQueryFunction):
    """geo.gridFilter() filters data by a specified geographic region.The function compares input data to a set of S2 cell ID tokens located in the specified region.
Input data must include an s2_cell_id column that is part of the group key.Note: S2 Grid cells may not perfectly align with the defined region,
so results may include data with coordinates outside the region, but inside
S2 grid cells partially covered by the region.
Use geo.toRows() and geo.strictFilter() after geo.gridFilter() to precisely filter points.(Required)
Region containing the desired data points.Specify record properties for the shape.Minimum number of cells that cover the specified region.
Default is 24.Maximum number of cells that cover the specified region.
Default is -1 (unlimited).S2 cell level
of grid cells. Default is -1.Note: level is mutually exclusive with minSize and maxSize and
must be less than or equal to s2cellIDLevel.S2 cell level
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the S2 cell ID token).Record that defines the unit of measurement for distance.
Default is the geo.units option.Input data. Default is piped-forward data (<-).

    Params:
        
        region 
        - (Required)
Region containing the desired data points.Specify record properties for the shape.
        
        minSize 
        - Minimum number of cells that cover the specified region.
Default is 24.
        
        maxSize 
        - Maximum number of cells that cover the specified region.
Default is -1 (unlimited).
        
        level 
        - S2 cell level
of grid cells. Default is -1.Note: level is mutually exclusive with minSize and maxSize and
must be less than or equal to s2cellIDLevel.
        
        s2cellIDLevel 
        - S2 cell level
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the S2 cell ID token).
        
        units 
        - Record that defines the unit of measurement for distance.
Default is the geo.units option.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "gridFilter"
    package="geo"

    def __init__(self, region, minSize=None, maxSize=None, level=None, s2cellIDLevel=None, units=None, tables=None, ):
            super().__init__(region=region, minSize=minSize, maxSize=maxSize, level=level, s2cellIDLevel=s2cellIDLevel, units=units, tables=tables, )