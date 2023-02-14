from flux_query_builder.functions.base import FluxQueryFunction

class PassFunction(FluxQueryFunction):
    """debug.pass() will pass any incoming tables directly next to the following transformation.
It is best used to interrupt any planner rules that rely on a specific ordering.Stream to pass unmodified to next transformation.

    Params:
        
        tables 
        - Stream to pass unmodified to next transformation.
        
    """
    def __init__(self, tables=None, ):
            super().__init__("", tables=tables, )