from flux_query_builder.functions.base import FluxQueryFunction

class Fill(FluxQueryFunction):
    """fill() replaces all null values in input tables with a non-null value.Output tables are the same as the input tables with all null values replaced
in the specified column.Column to replace null values in. Default is _value.Constant value to replace null values with.Value type must match the type of the specified column.Replace null values with the previous non-null value.
Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to replace null values in. Default is _value.
        
        value 
        - Constant value to replace null values with.Value type must match the type of the specified column.
        
        usePrevious 
        - Replace null values with the previous non-null value.
Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "fill"
    package=None

    def __init__(self, column=None, value=None, usePrevious=None, tables=None, ):
            super().__init__(column=column, value=value, usePrevious=usePrevious, tables=tables, )