from flux_query_builder.functions.base import FluxQueryFunction

class Get(FluxQueryFunction):
    """secrets.get() retrieves a secret from the InfluxDB secret store.(Required)
Secret key to retrieve.

    Params:
        
        key 
        - (Required)
Secret key to retrieve.
        
    """
    name = "get"
    package="secrets"

    def __init__(self, key, ):
            super().__init__(key=key, )