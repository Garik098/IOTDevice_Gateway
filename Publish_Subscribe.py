import mqttclient
import pullcerts
import config

data = {}
if not config.configuration:
    print("pulling certs")
    response = pullcerts.getcerts()
    mqttclient.mqttdataexchange(data)
 
else:
    print("mqttdataexchange")
    mqttclient.mqttdataexchange(data)
