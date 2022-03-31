import os

ip = input("IPV4 ADRESS: ")

response = os.popen(f"ping {ip}").read()
if "Received = 4" in response:
        print(f" {ip}: HOST IS UP")
else:
        print(f"{ip}: HOST IS DOWN")