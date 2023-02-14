from flux_query_builder.functions.base import FluxQueryFunction

class Histogram(FluxQueryFunction):
    """histogram() approximates the cumulative distribution of a dataset by counting
data frequencies for a list of bins.A bin is defined by an upper bound where all data points that are less than
or equal to the bound are counted in the bin. Bin counts are cumulative.Each input table is converted into a single output table representing a single histogram.
Each output table has the same group key as the corresponding input table.
Columns not part of the group key are dropped.
Output tables include additional columns for the upper bound and count of bins.Column containing input values. Column must be of type float.
Default is _value.Column to store bin upper bounds in. Default is le.Column to store bin counts in. Default is _value.(Required)
List of upper bounds to use when computing the histogram frequencies.Bins should contain a bin whose bound is the maximum value of the data set.
This value can be set to positive infinity if no maximum is known.The following helper functions can be used to generated bins.Convert counts into frequency values between 0 and 1.
Default is false.Note: Normalized histograms cannot be aggregated by summing their counts.Input data. Default is piped-forward data (<-).

    Params:
        
        bins 
        - (Required)
List of upper bounds to use when computing the histogram frequencies.Bins should contain a bin whose bound is the maximum value of the data set.
This value can be set to positive infinity if no maximum is known.The following helper functions can be used to generated bins.
        
        column 
        - Column containing input values. Column must be of type float.
Default is _value.
        
        upperBoundColumn 
        - Column to store bin upper bounds in. Default is le.
        
        countColumn 
        - Column to store bin counts in. Default is _value.
        
        normalize 
        - Convert counts into frequency values between 0 and 1.
Default is false.Note: Normalized histograms cannot be aggregated by summing their counts.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "histogram"
    package=None

    def __init__(self, bins, column=None, upperBoundColumn=None, countColumn=None, normalize=None, tables=None, ):
            super().__init__(bins=bins, column=column, upperBoundColumn=upperBoundColumn, countColumn=countColumn, normalize=normalize, tables=tables, )