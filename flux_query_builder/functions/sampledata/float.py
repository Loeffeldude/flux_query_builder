from flux_query_builder.functions.base import FluxQueryFunction

class Float(FluxQueryFunction):
    """sampledata.float() returns a sample data set with float values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "float"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )