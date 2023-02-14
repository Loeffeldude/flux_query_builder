from flux_query_builder.functions.base import FluxQueryFunction

class Publish(FluxQueryFunction):
    """mqtt.publish() sends data to an MQTT broker using MQTT protocol.(Required)
MQTT broker connection string.(Required)
MQTT topic to send data to.(Required)
Message to send to the MQTT broker.MQTT Quality of Service (QoS) level. Values range from [0-2].
Default is 0.MQTT retain flag. Default is false.MQTT client ID.Username to send to the MQTT broker.Username is only required if the broker requires authentication.
If you provide a username, you must provide a password.Password to send to the MQTT broker.Password is only required if the broker requires authentication.
If you provide a password, you must provide a username.MQTT connection timeout. Default is 1s.

    Params:
        
        broker 
        - (Required)
MQTT broker connection string.
        
        topic 
        - (Required)
MQTT topic to send data to.
        
        message 
        - (Required)
Message to send to the MQTT broker.
        
        qos 
        - MQTT Quality of Service (QoS) level. Values range from [0-2].
Default is 0.
        
        retain 
        - MQTT retain flag. Default is false.
        
        clientid 
        - MQTT client ID.
        
        username 
        - Username to send to the MQTT broker.Username is only required if the broker requires authentication.
If you provide a username, you must provide a password.
        
        password 
        - Password to send to the MQTT broker.Password is only required if the broker requires authentication.
If you provide a password, you must provide a username.
        
        timeout 
        - MQTT connection timeout. Default is 1s.
        
    """
    name = "publish"
    package="mqtt"

    def __init__(self, broker, topic, message, qos=None, retain=None, clientid=None, username=None, password=None, timeout=None, ):
            super().__init__(broker=broker, topic=topic, message=message, qos=qos, retain=retain, clientid=clientid, username=username, password=password, timeout=timeout, )