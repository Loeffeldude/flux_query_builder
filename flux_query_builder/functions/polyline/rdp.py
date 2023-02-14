from flux_query_builder.functions.base import FluxQueryFunction

class Rdp(FluxQueryFunction):
    """polyline.rdp() applies the Ramer Douglas Peucker (RDP) algorithm to input data to downsample curves composed
of line segments into visually indistinguishable curves with fewer points.Column with Y axis values of the given curve. Default is _value.Column with X axis values of the given curve. Default is _time.Maximum tolerance value that determines the amount of compression.Epsilon should be greater than 0.0.Percentage of points to retain after downsampling.Retention rate should be between 0.0 and 100.0.Input data. Default is piped-forward data (<-).When using polyline.rdp(), leave both epsilon and retention unspecified
to automatically calculate the maximum tolerance for producing a visually
indistinguishable curve.

    Params:
        
        valColumn 
        - Column with Y axis values of the given curve. Default is _value.
        
        timeColumn 
        - Column with X axis values of the given curve. Default is _time.
        
        epsilon 
        - Maximum tolerance value that determines the amount of compression.Epsilon should be greater than 0.0.
        
        retention 
        - Percentage of points to retain after downsampling.Retention rate should be between 0.0 and 100.0.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "rdp"
    package="polyline"

    def __init__(self, valColumn=None, timeColumn=None, epsilon=None, retention=None, tables=None, ):
            super().__init__(valColumn=valColumn, timeColumn=timeColumn, epsilon=epsilon, retention=retention, tables=tables, )