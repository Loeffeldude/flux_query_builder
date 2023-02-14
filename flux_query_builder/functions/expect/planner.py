from flux_query_builder.functions.base import FluxQueryFunction

class Planner(FluxQueryFunction):
    """expect.planner() will cause the present testcase to
expect the given planner rules will be invoked
exactly as many times as the number given.The key is the name of the planner rule.(Required)
Mapping of rules names to expected counts.

    Params:
        
        rules 
        - (Required)
Mapping of rules names to expected counts.
        
    """
    name = "planner"
    package="expect"

    def __init__(self, rules, ):
            super().__init__(rules=rules, )