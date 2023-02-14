from flux_query_builder.functions.base import FluxQueryFunction

class To(FluxQueryFunction):
    """sql.to() writes data to an SQL database.(Required)
Driver used to connect to the SQL database.Supported drivers:(Required)
Data source name (DNS) or connection string used
to connect to the SQL database.(Required)
Destination table.Number of parameters or columns that can be queued within each
call to Exec. Default is 10000.If writing to SQLite database, set the batchSize to 999 or less.Input data. Default is piped-forward data (<-).

    Params:
        
        driverName 
        - (Required)
Driver used to connect to the SQL database.Supported drivers:
        
        dataSourceName 
        - (Required)
Data source name (DNS) or connection string used
to connect to the SQL database.
        
        table 
        - (Required)
Destination table.
        
        batchSize 
        - Number of parameters or columns that can be queued within each
call to Exec. Default is 10000.If writing to SQLite database, set the batchSize to 999 or less.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "to"
    package="sql"

    def __init__(self, driverName, dataSourceName, table, batchSize=None, tables=None, ):
            super().__init__(driverName=driverName, dataSourceName=dataSourceName, table=table, batchSize=batchSize, tables=tables, )