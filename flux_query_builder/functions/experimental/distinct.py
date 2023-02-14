from flux_query_builder.functions.base import FluxQueryFunction

class Distinct(FluxQueryFunction):
    """experimental.distinct() returns unique values from the _value column.The _value of each output record is set to a distinct value in the specified column.
null is considered a distinct value.experimental.distinct() drops all columns not in the group key and
drops empty tables.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "distinct"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )