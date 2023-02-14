from flux_query_builder.functions.base import FluxQueryFunction

class Stddev(FluxQueryFunction):
    """experimental.stddev() returns the standard deviation of non-null values in the _value
column for each input table.The following modes are avaialable when calculating the standard deviation of data.Calculate the sample standard deviation where the data is considered to be
part of a larger population.Calculate the population standard deviation where the data is considered a
population of its own.Standard deviation mode or type of standard deviation to calculate.
Default is sample.Available options:Input data. Default is piped-forward data (<-).

    Params:
        
        mode 
        - Standard deviation mode or type of standard deviation to calculate.
Default is sample.Available options:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stddev"
    package="experimental"

    def __init__(self, mode=None, tables=None, ):
            super().__init__(mode=mode, tables=tables, )