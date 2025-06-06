#Write a Python script that starts and stops a system service.

import os

# Function to start a service
def start_service(service_name):
    os.system(f"sudo systemctl start {service_name}")
    print(f"Service {service_name} started")

# Function to stop a service
def stop_service(service_name):
    os.system(f"sudo systemctl stop {service_name}")
    print(f"Service {service_name} stopped")



# Service to manage
service_name = "jenkins"




# Start and stop the service
start_service(service_name)
stop_service(service_name)
