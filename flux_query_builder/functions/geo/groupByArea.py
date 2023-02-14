from flux_query_builder.functions.base import FluxQueryFunction

class GroupByArea(FluxQueryFunction):
    """geo.groupByArea() groups rows by geographic area.Area sizes are determined by the specified level.
Each geographic area is assigned a unique identifier (the S2 cell ID token)
which is stored in the newColumn.
Results are grouped by newColumn.(Required)
Name of the new column for the unique identifier for each geographic area.(Required)
S2 Cell level
used to determine the size of each geographic area.S2 Cell level
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the s2_cell_id tag).Input data. Default is piped-forward data (<-).

    Params:
        
        newColumn 
        - (Required)
Name of the new column for the unique identifier for each geographic area.
        
        level 
        - (Required)
S2 Cell level
used to determine the size of each geographic area.
        
        s2cellIDLevel 
        - S2 Cell level
used in the s2_cell_id tag. Default is -1 (detects S2 cell level from the s2_cell_id tag).
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "groupByArea"
    package="geo"

    def __init__(self, newColumn, level, s2cellIDLevel=None, tables=None, ):
            super().__init__(newColumn=newColumn, level=level, s2cellIDLevel=s2cellIDLevel, tables=tables, )