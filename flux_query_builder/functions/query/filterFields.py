from flux_query_builder.functions.base import FluxQueryFunction

class FilterFields(FluxQueryFunction):
    """query.filterFields() filters input data by field.Fields to filter by. Default is [].Input data. Default is piped-forward data (<-).

    Params:
        
        fields 
        - Fields to filter by. Default is [].
        
        table 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "filterFields"
    package="query"

    def __init__(self, fields=None, table=None, ):
            super().__init__(fields=fields, table=table, )