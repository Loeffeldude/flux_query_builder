from flux_query_builder.functions.base import FluxQueryFunction

class Distinct(FluxQueryFunction):
    """distinct() returns all unique values in a specified column.The _value of each output record is set to a distinct value in the specified column.
null is considered its own distinct value if present.Column to return unique values from. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to return unique values from. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "distinct"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )