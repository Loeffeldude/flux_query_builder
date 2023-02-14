from flux_query_builder.functions.base import FluxQueryFunction

class Chain(FluxQueryFunction):
    """experimental.chain() runs two queries in a single Flux script sequentially and outputs the
results of the second query.Flux typically executes multiple queries in a single script in parallel.
Running the queries sequentially ensures any dependencies the second query
has on the results of the first query are met.(Required)
First query to execute.(Required)
Second query to execute.

    Params:
        
        first 
        - (Required)
First query to execute.
        
        second 
        - (Required)
Second query to execute.
        
    """
    name = "chain"
    package="experimental"

    def __init__(self, first, second, ):
            super().__init__(first=first, second=second, )