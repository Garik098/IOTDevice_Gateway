import mqttclient

def sensor_data():
    response = {}
    for i in range(1,100):
        response["temp"] = i
        ack = mqttclient.to_publish(response)
        print(ack)
    return True