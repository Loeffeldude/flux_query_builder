from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """socket.from() returns data from a socket connection and outputs a stream of tables
given a specified decoder.The function produces a single table for everything that it receives from the
start to the end of the connection.(Required)
URL to return data from.Supported URL schemes:Decoder to use to parse returned data into a stream of tables.Supported decoders:

    Params:
        
        url 
        - (Required)
URL to return data from.Supported URL schemes:
        
        decoder 
        - Decoder to use to parse returned data into a stream of tables.Supported decoders:
        
    """
    name = "from"
    package="socket"

    def __init__(self, url, decoder=None, ):
            super().__init__(url=url, decoder=decoder, )