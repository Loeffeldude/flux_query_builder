from flux_query_builder.functions.base import FluxQueryFunction

class Skew(FluxQueryFunction):
    """skew() returns the skew of non-null records in each input table as a float.Column to operate on. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "skew"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )