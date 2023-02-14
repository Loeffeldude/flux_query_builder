from flux_query_builder.functions.base import FluxQueryFunction

class HistogramQuantile(FluxQueryFunction):
    """experimental.histogramQuantile() approximates a quantile given a histogram with the
cumulative distribution of the dataset.Each input table represents a single histogram.
Input tables must have two columns: a count column (_value) and an upper bound
column (le). Neither column can be part of the group key.The count is the number of values that are less than or equal to the upper bound value (le).
Input tables can have an unlimited number of records; each record represents an entry in the histogram.
The counts must be monotonically increasing when sorted by upper bound (le).
If any values in the _value or le columns are null, the function returns an error.Linear interpolation between the two closest bounds is used to compute the quantile.
If the either of the bounds used in interpolation are infinite,
then the other finite bound is used and no interpolation is performed.The output table has the same group key as the input table.
The function returns the value of the specified quantile from the histogram in the
_value column and drops all columns not part of the group key.Quantile to compute ([0.0 - 1.0]).Assumed minimum value of the dataset. Default is 0.0.When the quantile falls below the lowest upper bound, the function
interpolates values between minValue and the lowest upper bound.
If minValue is equal to negative infinity, the lowest upper bound is used.Input data. Default is piped-forward data (<-).

    Params:
        
        quantile 
        - Quantile to compute ([0.0 - 1.0]).
        
        minValue 
        - Assumed minimum value of the dataset. Default is 0.0.When the quantile falls below the lowest upper bound, the function
interpolates values between minValue and the lowest upper bound.
If minValue is equal to negative infinity, the lowest upper bound is used.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "histogramQuantile"
    package="experimental"

    def __init__(self, quantile=None, minValue=None, tables=None, ):
            super().__init__(quantile=quantile, minValue=minValue, tables=tables, )