from flux_query_builder.functions.base import FluxQueryFunction

class Get(FluxQueryFunction):
    """dict.get() returns the value of a specified key in a dictionary or a default value
if the key does not exist.(Required)
Dictionary to return a value from.(Required)
Key to return from the dictionary.(Required)
Default value to return if the key does not exist in the
dictionary. Must be the same type as values in the dictionary.

    Params:
        
        dict 
        - (Required)
Dictionary to return a value from.
        
        key 
        - (Required)
Key to return from the dictionary.
        
        default 
        - (Required)
Default value to return if the key does not exist in the
dictionary. Must be the same type as values in the dictionary.
        
    """
    name = "get"
    package="dict"

    def __init__(self, dict, key, default, ):
            super().__init__(dict=dict, key=key, default=default, )