# Write a Python script that checks if a server/host is up by pinging it.

import os

def ping_server(server):
    response = os.system(f"ping {server}")
    return response == 0
server = "google.com"

if ping_server(server):
    print(f"server {server} is up")
else:
    print(f"server {server} is down")
