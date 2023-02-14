from flux_query_builder.functions.base import FluxQueryFunction

class HistogramQuantile(FluxQueryFunction):
    """histogramQuantile() approximates a quantile given a histogram that approximates
the cumulative distribution of the dataset.Each input table represents a single histogram.
The histogram tables must have two columns – a count column and an upper bound column.The count is the number of values that are less than or equal to the upper bound value.
The table can have any number of records, each representing a bin in the histogram.
The counts must be monotonically increasing when sorted by upper bound.
If any values in the count column or upper bound column are null, it returns an error.
The count and upper bound columns must not be part of the group key.The quantile is computed using linear interpolation between the two closest bounds.
If either of the bounds used in interpolation are infinite, the other finite
bound is used and no interpolation is performed.Output tables have the same group key as corresponding input tables.
Columns not part of the group key are dropped.
A single value column of type float is added.
The value column represents the value of the desired quantile from the histogram.Quantile to compute. Value must be between 0 and 1.Column containing histogram bin counts. Default is _value.Column containing histogram bin upper bounds.
Default is le.Column to store the computed quantile in. Default is `_value.Assumed minimum value of the dataset. Default is 0.0.If the quantile falls below the lowest upper bound, interpolation is
performed between minValue and the lowest upper bound.
When minValue is equal to negative infinity, the lowest upper bound is used.Input data. Default is piped-forward data (<-).

    Params:
        
        quantile 
        - Quantile to compute. Value must be between 0 and 1.
        
        countColumn 
        - Column containing histogram bin counts. Default is _value.
        
        upperBoundColumn 
        - Column containing histogram bin upper bounds.
Default is le.
        
        valueColumn 
        - Column to store the computed quantile in. Default is `_value.
        
        minValue 
        - Assumed minimum value of the dataset. Default is 0.0.If the quantile falls below the lowest upper bound, interpolation is
performed between minValue and the lowest upper bound.
When minValue is equal to negative infinity, the lowest upper bound is used.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "histogramQuantile"
    package=None

    def __init__(self, quantile=None, countColumn=None, upperBoundColumn=None, valueColumn=None, minValue=None, tables=None, ):
            super().__init__(quantile=quantile, countColumn=countColumn, upperBoundColumn=upperBoundColumn, valueColumn=valueColumn, minValue=minValue, tables=tables, )