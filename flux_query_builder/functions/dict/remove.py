from flux_query_builder.functions.base import FluxQueryFunction

class Remove(FluxQueryFunction):
    """dict.remove() removes a key value pair from a dictionary and returns an updated
dictionary.(Required)
Dictionary to remove the key-value pair from.(Required)
Key to remove from the dictionary.
Must be the same type as existing keys in the dictionary.

    Params:
        
        dict 
        - (Required)
Dictionary to remove the key-value pair from.
        
        key 
        - (Required)
Key to remove from the dictionary.
Must be the same type as existing keys in the dictionary.
        
    """
    name = "remove"
    package="dict"

    def __init__(self, dict, key, ):
            super().__init__(dict=dict, key=key, )