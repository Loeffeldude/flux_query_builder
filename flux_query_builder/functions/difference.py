from flux_query_builder.functions.base import FluxQueryFunction

class Difference(FluxQueryFunction):
    """difference() returns the difference between subsequent values.For each input table with n rows, difference() outputs a table with
n - 1 rows.Disallow negative differences. Default is false.When true, if a value is less than the previous value, the function
assumes the previous value should have been a zero.List of columns to operate on. Default is ["_value"].Keep the first row in each input table. Default is false.If true, the difference of the first row of each output table is null.Use zero (0) as the initial value in the difference calculation
when the subsequent value is less than the previous value and nonNegative is
true. Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        nonNegative 
        - Disallow negative differences. Default is false.When true, if a value is less than the previous value, the function
assumes the previous value should have been a zero.
        
        columns 
        - List of columns to operate on. Default is ["_value"].
        
        keepFirst 
        - Keep the first row in each input table. Default is false.If true, the difference of the first row of each output table is null.
        
        initialZero 
        - Use zero (0) as the initial value in the difference calculation
when the subsequent value is less than the previous value and nonNegative is
true. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "difference"
    package=None

    def __init__(self, nonNegative=None, columns=None, keepFirst=None, initialZero=None, tables=None, ):
            super().__init__(nonNegative=nonNegative, columns=columns, keepFirst=keepFirst, initialZero=initialZero, tables=tables, )