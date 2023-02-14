from flux_query_builder.functions.base import FluxQueryFunction

class Derivative(FluxQueryFunction):
    """derivative() computes the rate of change per unit of time between subsequent
non-null records.The function assumes rows are ordered by the _time.The output table schema will be the same as the input table.
For each input table with n rows, derivative() outputs a table with
n - 1 rows.Time duration used to calculate the derivative. Default is 1s.Disallow negative derivative values. Default is false.When true, if a value is less than the previous value, the function
assumes the previous value should have been a zero.List of columns to operate on. Default is ["_value"].Column containing time values to use in the calculation.
Default is _time.Use zero (0) as the initial value in the derivative calculation
when the subsequent value is less than the previous value and nonNegative is
true. Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - Time duration used to calculate the derivative. Default is 1s.
        
        nonNegative 
        - Disallow negative derivative values. Default is false.When true, if a value is less than the previous value, the function
assumes the previous value should have been a zero.
        
        columns 
        - List of columns to operate on. Default is ["_value"].
        
        timeColumn 
        - Column containing time values to use in the calculation.
Default is _time.
        
        initialZero 
        - Use zero (0) as the initial value in the derivative calculation
when the subsequent value is less than the previous value and nonNegative is
true. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "derivative"
    package=None

    def __init__(self, unit=None, nonNegative=None, columns=None, timeColumn=None, initialZero=None, tables=None, ):
            super().__init__(unit=unit, nonNegative=nonNegative, columns=columns, timeColumn=timeColumn, initialZero=initialZero, tables=tables, )