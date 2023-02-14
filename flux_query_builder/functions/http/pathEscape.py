from flux_query_builder.functions.base import FluxQueryFunction

class PathEscape(FluxQueryFunction):
    """http.pathEscape() escapes special characters in a string (including /)
and replaces non-ASCII characters with hexadecimal representations (%XX).(Required)
String to escape.

    Params:
        
        inputString 
        - (Required)
String to escape.
        
    """
    name = "pathEscape"
    package="http"

    def __init__(self, inputString, ):
            super().__init__(inputString=inputString, )