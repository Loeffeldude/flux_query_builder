from flux_query_builder.functions.base import FluxQueryFunction

class Reduce(FluxQueryFunction):
    """reduce() aggregates rows in each input table using a reducer function (fn).The output for each table is the group key of the table with columns
corresponding to each field in the reducer record.
If the reducer record contains a column with the same name as a group key column,
the group key column’s value is overwritten, and the outgoing group key is changed.
However, if two reduced tables write to the same destination group key, the
function returns an error.reduce() drops any columns that:(Required)
Reducer function to apply to each row record (r).The reducer function accepts two parameters:(Required)
Record that defines the reducer record and provides initial values
for the reducer operation on the first row.May be used more than once in asynchronous processing use cases.
The data type of values in the identity record determine the data type of
output values.Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Reducer function to apply to each row record (r).The reducer function accepts two parameters:
        
        identity 
        - (Required)
Record that defines the reducer record and provides initial values
for the reducer operation on the first row.May be used more than once in asynchronous processing use cases.
The data type of values in the identity record determine the data type of
output values.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "reduce"
    package=None

    def __init__(self, fn, identity, tables=None, ):
            super().__init__(fn=fn, identity=identity, tables=tables, )