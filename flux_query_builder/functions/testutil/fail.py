from flux_query_builder.functions.base import FluxQueryFunction

class Fail(FluxQueryFunction):
    """testutil.fail() causes the current script to fail.

    Params:
        
    """
    name = "fail"
    package="testutil"

    def __init__(self, ):
            super().__init__()