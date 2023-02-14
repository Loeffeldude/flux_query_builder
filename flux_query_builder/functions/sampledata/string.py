from flux_query_builder.functions.base import FluxQueryFunction

class String(FluxQueryFunction):
    """sampledata.string() returns a sample data set with string values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "string"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )