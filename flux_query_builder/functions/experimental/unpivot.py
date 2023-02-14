from flux_query_builder.functions.base import FluxQueryFunction

class Unpivot(FluxQueryFunction):
    """experimental.unpivot() creates _field and _value columns pairs using all columns (other than _time)
not in the group key.
The _field column contains the original column label and the _value column
contains the original column value.The output stream retains the group key and all group key columns of the input stream.
_field is added to the output group key.Input data. Default is piped-forward data (<-).List of column names that are not in the group key but are also not field columns. Default is ["_time"].

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        otherColumns 
        - List of column names that are not in the group key but are also not field columns. Default is ["_time"].
        
    """
    name = "unpivot"
    package="experimental"

    def __init__(self, tables=None, otherColumns=None, ):
            super().__init__(tables=tables, otherColumns=otherColumns, )