from flux_query_builder.functions.base import FluxQueryFunction

class Integral(FluxQueryFunction):
    """experimental.integral() computes the area under the curve per unit of time of subsequent non-null records.The curve is defined using _time as the domain and record values as the range.Input tables must have _start, _stop, _time, and _valuecolumns._startand_stop` must be part of the group key.Time duration used to compute the integral.Type of interpolation to use. Default is "" (no interpolation).Use one of the following interpolation options:Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - Time duration used to compute the integral.
        
        interpolate 
        - Type of interpolation to use. Default is "" (no interpolation).Use one of the following interpolation options:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "integral"
    package="experimental"

    def __init__(self, unit=None, interpolate=None, tables=None, ):
            super().__init__(unit=unit, interpolate=interpolate, tables=tables, )