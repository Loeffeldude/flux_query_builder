from flux_query_builder.functions.base import FluxQueryFunction

class Substring(FluxQueryFunction):
    """strings.substring() returns a substring based on start and end parameters. These parameters are represent indices of UTF code points in the string.When start or end are past the bounds of the string, respecitvely the start or end of the string
is assumed. When end is less than or equal to start an empty string is returned.(Required)
String value to search for.(Required)
Starting inclusive index of the substring.(Required)
Ending exclusive index of the substring.

    Params:
        
        v 
        - (Required)
String value to search for.
        
        start 
        - (Required)
Starting inclusive index of the substring.
        
        end 
        - (Required)
Ending exclusive index of the substring.
        
    """
    name = "substring"
    package="strings"

    def __init__(self, v, start, end, ):
            super().__init__(v=v, start=start, end=end, )