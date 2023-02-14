from flux_query_builder.functions.base import FluxQueryFunction

class Columns(FluxQueryFunction):
    """columns() returns the column labels in each input table.For each input table, columns outputs a table with the same group key
columns and a new column containing the column labels in the input table.
Each row in an output table contains the group key value and the label of one
column of the input table.
Each output table has the same number of rows as the number of columns of the
input table.Name of the output column to store column labels in.
Default is “_value”.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Name of the output column to store column labels in.
Default is “_value”.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "columns"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )