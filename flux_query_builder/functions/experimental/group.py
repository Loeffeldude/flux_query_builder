from flux_query_builder.functions.base import FluxQueryFunction

class Group(FluxQueryFunction):
    """experimental.group() introduces an extend mode to the existing group() function.(Required)
List of columns to use in the grouping operation. Default is [].(Required)
Grouping mode. extend is the only mode available to experimental.group().Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - (Required)
List of columns to use in the grouping operation. Default is [].
        
        mode 
        - (Required)
Grouping mode. extend is the only mode available to experimental.group().
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "group"
    package="experimental"

    def __init__(self, columns, mode, tables=None, ):
            super().__init__(columns=columns, mode=mode, tables=tables, )