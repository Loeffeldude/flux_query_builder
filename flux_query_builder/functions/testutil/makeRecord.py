from flux_query_builder.functions.base import FluxQueryFunction

class MakeRecord(FluxQueryFunction):
    """testutil.makeRecord() is the identity function, but breaks the type connection from input to output.(Required)
Record value.

    Params:
        
        o 
        - (Required)
Record value.
        
    """
    name = "makeRecord"
    package="testutil"

    def __init__(self, o, ):
            super().__init__(o=o, )