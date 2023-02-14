from flux_query_builder.functions.base import FluxQueryFunction

class IsNumeric(FluxQueryFunction):
    """types.isNumeric() tests if a value is a numeric type (int, uint, or float).This is a helper function to test or filter for values that can be used in
arithmatic operations or aggregations.(Required)
Value to test.

    Params:
        
        v 
        - (Required)
Value to test.
        
    """
    name = "isNumeric"
    package="types"

    def __init__(self, v, ):
            super().__init__(v=v, )