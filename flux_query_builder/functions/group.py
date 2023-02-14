from flux_query_builder.functions.base import FluxQueryFunction

class Group(FluxQueryFunction):
    """group() regroups input data by modifying group key of input tables.Note: Group does not gaurantee sort order.
To ensure data is sorted correctly, use sort() after group().List of columns to use in the grouping operation. Default is [].Note: When columns is set to an empty array, group() ungroups
all data merges it into a single output table.Grouping mode. Default is by.Avaliable modes:Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - List of columns to use in the grouping operation. Default is [].Note: When columns is set to an empty array, group() ungroups
all data merges it into a single output table.
        
        mode 
        - Grouping mode. Default is by.Avaliable modes:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "group"
    package=None

    def __init__(self, columns=None, mode=None, tables=None, ):
            super().__init__(columns=columns, mode=mode, tables=tables, )