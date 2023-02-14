from flux_query_builder.functions.base import FluxQueryFunction

class NaN(FluxQueryFunction):
    """math.NaN() returns a IEEE 754 “not-a-number” value.

    Params:
        
    """
    name = "NaN"
    package="math"

    def __init__(self, ):
            super().__init__()