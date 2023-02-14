from flux_query_builder.functions.base import FluxQueryFunction

class GetOption(FluxQueryFunction):
    """debug.getOption() gets the value of an option using a form of reflection.(Required)
Full path of the package.(Required)
Option name.

    Params:
        
        pkg 
        - (Required)
Full path of the package.
        
        name 
        - (Required)
Option name.
        
    """
    name = "getOption"
    package="debug"

    def __init__(self, pkg, name, ):
            super().__init__(pkg=pkg, name=name, )