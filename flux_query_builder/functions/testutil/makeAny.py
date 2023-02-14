from flux_query_builder.functions.base import FluxQueryFunction

class MakeAny(FluxQueryFunction):
    """testutil.makeAny() constructs any value based on a type description as a string.(Required)
Description of the type to create.

    Params:
        
        typ 
        - (Required)
Description of the type to create.
        
    """
    name = "makeAny"
    package="testutil"

    def __init__(self, typ, ):
            super().__init__(typ=typ, )