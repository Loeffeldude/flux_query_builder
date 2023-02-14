from flux_query_builder.functions.base import FluxQueryFunction

class Opaque(FluxQueryFunction):
    """debug.opaque() works like pass in that it passes any incoming tables directly to the
following transformation, save for its type signature does not indicate that the
input type has any correlation with the output type.Stream to pass unmodified to next transformation.

    Params:
        
        tables 
        - Stream to pass unmodified to next transformation.
        
    """
    name = "opaque"
    package="debug"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )