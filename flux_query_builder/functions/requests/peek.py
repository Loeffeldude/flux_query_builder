from flux_query_builder.functions.base import FluxQueryFunction

class Peek(FluxQueryFunction):
    """requests.peek() converts an HTTP response into a table for easy inspection.The output table includes the following columns:To customize how the response data is structured in a table, use array.from()
with a function like json.parse(). Parse the response body into a set of values
and then use array.from() to construct a table from those values.(Required)
Response data from an HTTP request.

    Params:
        
        response 
        - (Required)
Response data from an HTTP request.
        
    """
    name = "peek"
    package="requests"

    def __init__(self, response, ):
            super().__init__(response=response, )