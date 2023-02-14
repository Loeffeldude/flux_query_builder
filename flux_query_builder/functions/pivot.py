from flux_query_builder.functions.base import FluxQueryFunction

class Pivot(FluxQueryFunction):
    """pivot() collects unique values stored vertically (column-wise) and aligns them
horizontally (row-wise) into logical sets.The group key of the resulting table is the same as the input tables,
excluding columns found in the columnKey and valueColumn parameters.
These columns are not part of the resulting output table and are dropped from
the group key.Every input row should have a 1:1 mapping to a particular row and column
combination in the output table. Row and column combinations are determined
by the rowKey and columnKey parameters. In cases where more than one
value is identified for the same row and column pair, the last value
encountered in the set of table rows is used as the result.The output is constructed as follows:(Required)
Columns to use to uniquely identify an output row.(Required)
Columns to use to identify new output columns.(Required)
Column to use to populate the value of pivoted columnKey columns.Input data. Default is piped-forward data (<-).

    Params:
        
        rowKey 
        - (Required)
Columns to use to uniquely identify an output row.
        
        columnKey 
        - (Required)
Columns to use to identify new output columns.
        
        valueColumn 
        - (Required)
Column to use to populate the value of pivoted columnKey columns.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "pivot"
    package=None

    def __init__(self, rowKey, columnKey, valueColumn, tables=None, ):
            super().__init__(rowKey=rowKey, columnKey=columnKey, valueColumn=valueColumn, tables=tables, )