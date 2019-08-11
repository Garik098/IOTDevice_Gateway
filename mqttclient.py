import paho.mqtt.client as paho
import os
import socket
import ssl
import config

def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print "Connected to AWS"
    connflag = True
    print("Connection returned result: " + str(rc) )
    client.subscribe("#", 1)

def on_message(client, userdata, msg):                      # Func for receiving msgs
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))


def mqttdataexchange(data):
    mqttclient = paho.Client()                                    
    mqttclient.on_connect = on_connect                               
    mqttclient.on_message = on_message              

    awshost = config.configuration['awshost']
    awsport = 8883                                               
    clientId = config.authentication['sn']                                    
    thingName = config.authentication['sn']                                  
    caPath = "rootca.pem"                                     
    certPath = "cert.pem.crt"                            
    keyPath = "privatekey.pem.key"                         
    
    mqttclient.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)      # pass parameters
    mqttclient.connect(awshost, awsport, keepalive=60)
    mqttclient.loop_forever()
    