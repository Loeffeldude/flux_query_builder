from flux_query_builder.functions.base import FluxQueryFunction

class To(FluxQueryFunction):
    """kafka.to() sends data to Apache Kafka brokers.(Required)
List of Kafka brokers to send data to.(Required)
Kafka topic to send data to.Kafka load balancing strategy. Default is hash.The load balancing strategy determines how messages are routed to partitions
available on a Kafka cluster. The following strategies are available:Kafka metric name. Default is the value of the nameColumn.Column to use as the Kafka metric name.
Default is _measurement.Time column. Default is _time.List of tag columns in input data.List of value columns in input data. Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        brokers 
        - (Required)
List of Kafka brokers to send data to.
        
        topic 
        - (Required)
Kafka topic to send data to.
        
        balancer 
        - Kafka load balancing strategy. Default is hash.The load balancing strategy determines how messages are routed to partitions
available on a Kafka cluster. The following strategies are available:
        
        name 
        - Kafka metric name. Default is the value of the nameColumn.
        
        nameColumn 
        - Column to use as the Kafka metric name.
Default is _measurement.
        
        timeColumn 
        - Time column. Default is _time.
        
        tagColumns 
        - List of tag columns in input data.
        
        valueColumns 
        - List of value columns in input data. Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "to"
    package="kafka"

    def __init__(self, brokers, topic, balancer=None, name=None, nameColumn=None, timeColumn=None, tagColumns=None, valueColumns=None, tables=None, ):
            super().__init__(brokers=brokers, topic=topic, balancer=balancer, name=name, nameColumn=nameColumn, timeColumn=timeColumn, tagColumns=tagColumns, valueColumns=valueColumns, tables=tables, )