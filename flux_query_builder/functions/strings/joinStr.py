from flux_query_builder.functions.base import FluxQueryFunction

class JoinStr(FluxQueryFunction):
    """strings.joinStr() concatenates elements of a string array into a single string using a specified separator.(Required)
Array of strings to concatenate.(Required)
Separator to use in the concatenated value.

    Params:
        
        arr 
        - (Required)
Array of strings to concatenate.
        
        v 
        - (Required)
Separator to use in the concatenated value.
        
    """
    name = "joinStr"
    package="strings"

    def __init__(self, arr, v, ):
            super().__init__(arr=arr, v=v, )