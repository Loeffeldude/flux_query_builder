from flux_query_builder.functions.base import FluxQueryFunction

class Insert(FluxQueryFunction):
    """dict.insert() inserts a key-value pair into a dictionary and returns a new,
updated dictionary.If the key already exists in the dictionary, the function overwrites
the existing value.(Required)
Dictionary to update.(Required)
Key to insert into the dictionary.
Must be the same type as the existing keys in the dictionary.(Required)
Value to insert into the dictionary.
Must be the same type as the existing values in the dictionary.

    Params:
        
        dict 
        - (Required)
Dictionary to update.
        
        key 
        - (Required)
Key to insert into the dictionary.
Must be the same type as the existing keys in the dictionary.
        
        value 
        - (Required)
Value to insert into the dictionary.
Must be the same type as the existing values in the dictionary.
        
    """
    name = "insert"
    package="dict"

    def __init__(self, dict, key, value, ):
            super().__init__(dict=dict, key=key, value=value, )