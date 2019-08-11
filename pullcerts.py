import config
import requests
import secret_info
import time

def getcerts():
    url = secret_info.secrets["url"]
    print("Hitting url"+url)
    requestCerts = requests.get(url, config.authentication)
    response = requestCerts.json()
    print("entered Getcerts")
    print(response)
    time.sleep(5)
    if response['message'] == "Successfully created the thing in AWS":
        cloud_cert = open("cert.pem.crt", "w+")
        cloud_cert.write(response['data']['certpem'])
        cloud_cert.close()
        rootca = open("rootca.pem", "w+")
        rootca.write(response['data']['rootca'])
        rootca.close()
        private_key = open("privatekey.pem.key", "w+")
        private_key.write(response['data']['privatekey'])
        private_key.close()
        config.configuration['awshost'] = response['data']['awshost']
    else:
        print("Thing not created in AWS")