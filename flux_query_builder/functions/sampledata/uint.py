from flux_query_builder.functions.base import FluxQueryFunction

class Uint(FluxQueryFunction):
    """sampledata.uint() returns a sample data set with unsigned integer values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "uint"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )