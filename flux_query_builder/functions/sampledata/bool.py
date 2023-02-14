from flux_query_builder.functions.base import FluxQueryFunction

class Bool(FluxQueryFunction):
    """sampledata.bool() returns a sample data set with boolean values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "bool"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )