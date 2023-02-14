from flux_query_builder.functions.base import FluxQueryFunction

class HoltWinters(FluxQueryFunction):
    """holtWinters() applies the Holt-Winters forecasting method to input tables.The Holt-Winters method predicts n seasonally-adjusted values for the
specified column at the specified interval. For example, if interval is six
minutes (6m) and n is 3, results include three predicted values six
minutes apart.seasonality delimits the length of a seasonal pattern according to interval.
If the interval is two minutes (2m) and seasonality is 4, then the
seasonal pattern occurs every eight minutes or every four data points.
If your interval is two months (2mo) and seasonality is 4, then the
seasonal pattern occurs every eight months or every four data points.
If data doesn’t have a seasonal pattern, set seasonality to 0.holtWinters() expects values to be spaced at even time intervales.
To ensure values are spaced evenly in time, holtWinters() applies the
following rules:By default, holtWinters() uses the first value in each time bucket to run
the Holt-Winters calculation. To specify other values to use in the
calculation, use aggregateWindow to normalize irregular times and apply
an aggregate or selector transformation.holtWinters() applies the Nelder-Mead optimization
to include “fitted” data points in results when withFit is set to true.holtWinters() discards rows with null timestamps before running the
Holt-Winters calculation.holtWinters() treats null values as missing data points and includes them
in the Holt-Winters calculation.(Required)
Number of values to predict.(Required)
Interval between two data points.Return fitted data in results. Default is false.Column to operate on. Default is _value.Column containing time values to use in the calculating.
Default is _time.Number of points in a season. Default is 0.Return minSSE data in results. Default is false.minSSE is the minimum sum squared error found when optimizing the holt winters fit to the data.
A smaller minSSE means a better fit.
Examining the minSSE value can help understand when the algorithm is getting a good fit versus not.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of values to predict.
        
        interval 
        - (Required)
Interval between two data points.
        
        withFit 
        - Return fitted data in results. Default is false.
        
        column 
        - Column to operate on. Default is _value.
        
        timeColumn 
        - Column containing time values to use in the calculating.
Default is _time.
        
        seasonality 
        - Number of points in a season. Default is 0.
        
        withMinSSE 
        - Return minSSE data in results. Default is false.minSSE is the minimum sum squared error found when optimizing the holt winters fit to the data.
A smaller minSSE means a better fit.
Examining the minSSE value can help understand when the algorithm is getting a good fit versus not.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "holtWinters"
    package=None

    def __init__(self, n, interval, withFit=None, column=None, timeColumn=None, seasonality=None, withMinSSE=None, tables=None, ):
            super().__init__(n=n, interval=interval, withFit=withFit, column=column, timeColumn=timeColumn, seasonality=seasonality, withMinSSE=withMinSSE, tables=tables, )