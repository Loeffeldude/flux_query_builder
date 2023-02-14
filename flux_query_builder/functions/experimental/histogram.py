from flux_query_builder.functions.base import FluxQueryFunction

class Histogram(FluxQueryFunction):
    """experimental.histogram() approximates the cumulative distribution of a dataset by counting
data frequencies for a list of bins.A bin is defined by an upper bound where all data points that are less than
or equal to the bound are counted in the bin.
Bin counts are cumulative.(Required)
List of upper bounds to use when computing histogram frequencies,
including the maximum value of the data set.This value can be set to positive infinity (float(v: "+Inf")) if no maximum is known.The following helper functions can be used to generated bins.Convert count values into frequency values between 0 and 1.
Default is false.Note: Normalized histograms cannot be aggregated by summing their counts.Input data. Default is piped-forward data (<-).

    Params:
        
        bins 
        - (Required)
List of upper bounds to use when computing histogram frequencies,
including the maximum value of the data set.This value can be set to positive infinity (float(v: "+Inf")) if no maximum is known.The following helper functions can be used to generated bins.
        
        normalize 
        - Convert count values into frequency values between 0 and 1.
Default is false.Note: Normalized histograms cannot be aggregated by summing their counts.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "histogram"
    package="experimental"

    def __init__(self, bins, normalize=None, tables=None, ):
            super().__init__(bins=bins, normalize=normalize, tables=tables, )