import requests
import time

URL = "http://sender:5000/data"
FILE_PATH = "/data/logs.txt"

while True:
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            with open(FILE_PATH, "a") as file:
                file.write(str(response.json()) + "\n")
            print("Data written to file:", response.json())
    except Exception as e:
        print("Error fetching data:", e)
    
    time.sleep(5)  