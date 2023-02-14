from flux_query_builder.functions.base import FluxQueryFunction

class GetGrid(FluxQueryFunction):
    """geo.getGrid() calculates a grid or set of cell ID tokens for a specified region.Note: S2 grid cells may not perfectly align with the defined region,
so results include S2 grid cells fully and partially covered by the region.(Required)
Region used to return S2 cell ID tokens.
Specify record properties for the region shape.Minimum number of cells that cover the specified region.Minimum number of cells that cover the specified region.S2 cell level of grid cells.Maximumn S2 cell level of grid cells.(Required)
Record that defines the unit of measurement for distance.

    Params:
        
        region 
        - (Required)
Region used to return S2 cell ID tokens.
Specify record properties for the region shape.
        
        units 
        - (Required)
Record that defines the unit of measurement for distance.
        
        minSize 
        - Minimum number of cells that cover the specified region.
        
        maxSize 
        - Minimum number of cells that cover the specified region.
        
        level 
        - S2 cell level of grid cells.
        
        maxLevel 
        - Maximumn S2 cell level of grid cells.
        
    """
    name = "getGrid"
    package="geo"

    def __init__(self, region, units, minSize=None, maxSize=None, level=None, maxLevel=None, ):
            super().__init__(region=region, units=units, minSize=minSize, maxSize=maxSize, level=level, maxLevel=maxLevel, )