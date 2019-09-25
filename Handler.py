import mqttclient
import pullcerts
import pickling
import threading
import sensors
import pdb

#pdb.set_trace()
auth = pickling.pickle_out_data()

def start_data_exchange():
    to_sensors = threading.Thread(target = sensors.sensor_data())
    to_sensors.start()
    to_cloud = threading.Thread(target = mqttclient.mqttdataexchange())
    to_cloud.start()

if not auth['awshost']:
    response = pullcerts.getcerts()
    if response == "success":
        print("response is success - Proceeding with mqtt data exchange")
        start_data_exchange()
    else:
        print("Certificate for the thing were not updated correctly")

else:
    print("mqttdataexchange")
    start_data_exchange()