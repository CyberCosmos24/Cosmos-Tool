import os

ip_list = ['1.1.1.1']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f" {ip}: HOST IS UP")
    else:
        print(f"{ip}: HOST IS DOWN")