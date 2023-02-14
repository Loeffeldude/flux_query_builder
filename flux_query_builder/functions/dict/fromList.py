from flux_query_builder.functions.base import FluxQueryFunction

class FromList(FluxQueryFunction):
    """dict.fromList() creates a dictionary from a list of records with key and value
properties.(Required)
List of records with key and value properties.

    Params:
        
        pairs 
        - (Required)
List of records with key and value properties.
        
    """
    name = "fromList"
    package="dict"

    def __init__(self, pairs, ):
            super().__init__(pairs=pairs, )