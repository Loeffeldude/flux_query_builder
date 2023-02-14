from flux_query_builder.functions.base import FluxQueryFunction

class BasicAuth(FluxQueryFunction):
    """http.basicAuth() returns a Base64-encoded basic authentication header
using a specified username and password combination.(Required)
Username to use in the basic authentication header.(Required)
Password to use in the basic authentication header.

    Params:
        
        u 
        - (Required)
Username to use in the basic authentication header.
        
        p 
        - (Required)
Password to use in the basic authentication header.
        
    """
    name = "basicAuth"
    package="http"

    def __init__(self, u, p, ):
            super().__init__(u=u, p=p, )