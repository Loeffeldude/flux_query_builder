from flux_query_builder.functions.base import FluxQueryFunction

class Integral(FluxQueryFunction):
    """integral() computes the area under the curve per unit of time of subsequent non-null records.integral() requires _start and _stop columns that are part of the group key.
The curve is defined using _time as the domain and record values as the range.Unit of time to use to compute the integral.Column to operate on. Default is _value.Column that contains time values to use in the operation.
Default is _time.Type of interpolation to use. Default is "".Available interplation types:Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - Unit of time to use to compute the integral.
        
        column 
        - Column to operate on. Default is _value.
        
        timeColumn 
        - Column that contains time values to use in the operation.
Default is _time.
        
        interpolate 
        - Type of interpolation to use. Default is "".Available interplation types:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "integral"
    package=None

    def __init__(self, unit=None, column=None, timeColumn=None, interpolate=None, tables=None, ):
            super().__init__(unit=unit, column=column, timeColumn=timeColumn, interpolate=interpolate, tables=tables, )