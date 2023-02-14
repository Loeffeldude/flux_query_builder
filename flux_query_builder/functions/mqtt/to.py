from flux_query_builder.functions.base import FluxQueryFunction

class To(FluxQueryFunction):
    """mqtt.to() outputs data from a stream of tables to an MQTT broker using MQTT protocol.(Required)
MQTT broker connection string.MQTT topic to send data to.MQTT Quality of Service (QoS) level. Values range from [0-2]. Default is 0.MQTT retain flag. Default is false.MQTT client ID.Username to send to the MQTT broker.Username is only required if the broker requires authentication.
If you provide a username, you must provide a password.Password to send to the MQTT broker.
Password is only required if the broker requires authentication.
If you provide a password, you must provide a username.Name for the MQTT message.MQTT connection timeout. Default is 1s.Column to use as time values in the output line protocol.
Default is "_time".Columns to use as tag sets in the output line protocol.
Default is [].Columns to use as field values in the output line protocol.
Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        broker 
        - (Required)
MQTT broker connection string.
        
        topic 
        - MQTT topic to send data to.
        
        qos 
        - MQTT Quality of Service (QoS) level. Values range from [0-2]. Default is 0.
        
        retain 
        - MQTT retain flag. Default is false.
        
        clientid 
        - MQTT client ID.
        
        username 
        - Username to send to the MQTT broker.Username is only required if the broker requires authentication.
If you provide a username, you must provide a password.
        
        password 
        - Password to send to the MQTT broker.
Password is only required if the broker requires authentication.
If you provide a password, you must provide a username.
        
        name 
        - Name for the MQTT message.
        
        timeout 
        - MQTT connection timeout. Default is 1s.
        
        timeColumn 
        - Column to use as time values in the output line protocol.
Default is "_time".
        
        tagColumns 
        - Columns to use as tag sets in the output line protocol.
Default is [].
        
        valueColumns 
        - Columns to use as field values in the output line protocol.
Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "to"
    package="mqtt"

    def __init__(self, broker, topic=None, qos=None, retain=None, clientid=None, username=None, password=None, name=None, timeout=None, timeColumn=None, tagColumns=None, valueColumns=None, tables=None, ):
            super().__init__(broker=broker, topic=topic, qos=qos, retain=retain, clientid=clientid, username=username, password=password, name=name, timeout=timeout, timeColumn=timeColumn, tagColumns=tagColumns, valueColumns=valueColumns, tables=tables, )