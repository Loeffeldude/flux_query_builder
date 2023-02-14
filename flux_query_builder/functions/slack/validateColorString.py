from flux_query_builder.functions.base import FluxQueryFunction

class ValidateColorString(FluxQueryFunction):
    """slack.validateColorString() ensures a string contains a valid hex color code.(Required)
Hex color code.

    Params:
        
        color 
        - (Required)
Hex color code.
        
    """
    name = "validateColorString"
    package="slack"

    def __init__(self, color, ):
            super().__init__(color=color, )