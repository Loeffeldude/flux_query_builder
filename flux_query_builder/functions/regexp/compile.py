from flux_query_builder.functions.base import FluxQueryFunction

class Compile(FluxQueryFunction):
    """regexp.compile() parses a string into a regular expression and returns a regexp type
that can be used to match against strings.(Required)
String value to parse into a regular expression.

    Params:
        
        v 
        - (Required)
String value to parse into a regular expression.
        
    """
    name = "compile"
    package="regexp"

    def __init__(self, v, ):
            super().__init__(v=v, )