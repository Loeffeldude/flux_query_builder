from flux_query_builder.functions.base import FluxQueryFunction

class Fill(FluxQueryFunction):
    """experimental.fill() replaces all null values in the _value column with a non-null value.Value to replace null values with.
Data type must match the type of the _value column.Replace null values with the value of the previous non-null row.Input data. Default is piped-forward data (<-).

    Params:
        
        value 
        - Value to replace null values with.
Data type must match the type of the _value column.
        
        usePrevious 
        - Replace null values with the value of the previous non-null row.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "fill"
    package="experimental"

    def __init__(self, value=None, usePrevious=None, tables=None, ):
            super().__init__(value=value, usePrevious=usePrevious, tables=tables, )