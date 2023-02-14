from flux_query_builder.functions.base import FluxQueryFunction

class FilterRows(FluxQueryFunction):
    """geo.filterRows() filters data by a specified geographic region with the option of strict filtering.This function is a combination of geo.gridFilter() and geo.strictFilter().
Input data must include an s2_cell_id column that is part of the group key.(Required)
Region containing the desired data points.Specify record properties for the shape.Minimum number of cells that cover the specified region.
Default is 24.Maximum number of cells that cover the specified region.
Default is -1 (unlimited).S2 cell level
of grid cells. Default is -1.Note: level is mutually exclusive with minSize and maxSize and
must be less than or equal to s2cellIDLevel.S2 cell level
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the s2_cell_id tag).Enable strict geographic data filtering. Default is true.Strict filtering returns only points with coordinates in the defined region.
Non-strict filtering returns all points from S2 grid cells that are partially
covered by the defined region.Input data. Default is piped-forward data (<-).

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
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the s2_cell_id tag).
        
        strict 
        - Enable strict geographic data filtering. Default is true.Strict filtering returns only points with coordinates in the defined region.
Non-strict filtering returns all points from S2 grid cells that are partially
covered by the defined region.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "filterRows"
    package="geo"

    def __init__(self, region, minSize=None, maxSize=None, level=None, s2cellIDLevel=None, strict=None, tables=None, ):
            super().__init__(region=region, minSize=minSize, maxSize=maxSize, level=level, s2cellIDLevel=s2cellIDLevel, strict=strict, tables=tables, )