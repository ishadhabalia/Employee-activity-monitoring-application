import win32gui 
import datetime
import csv
import os
import json
import urllib.request
import requests
from time import sleep


def get_location():
    url = "http://ipinfo.io/json"
    response = urllib.request.urlopen(url)
    data = json.load(response)
    print(data)
    remove = ["country", "postal", "timezone", "readme", "org", "region"]
    for i in remove:
        data.pop(i)
    return data


# to get current data
def get_current_data():
    open_win = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    print(win32gui.GetForegroundWindow())
    print(open_win)
    data = {
        "date": datetime.datetime.now(),
    }
    data.update(get_location())
    data["process"] = open_win.split(" - ")
    print(data)
    return data


# to append the row in the csv file
def append_row(data, filename="peek"):
    row = [data["date"], data["process"], data["ip"], data["city"], data["loc"]]
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    csv_dir_name = "csv_data"
    script_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(script_path, csv_dir_name)):
        os.mkdir(os.path.join(script_path, csv_dir_name))
    filepath = os.path.join(script_path, csv_dir_name, f"{filename}--{today}.csv")
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(
                ["Date", "Process-Name", "Name", "IP", "City", "Location"]
            )
    with open(filepath, "a") as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(row)

def send_data(data):
    API_ENDPOINT = "http://localhost:5000/update-activity"
    r = requests.post(url = API_ENDPOINT, json=json.dumps(data))
    print(r)

if __name__ == "__main__":
    print("in script.py")
    data = get_current_data()
    append_row(data)
    send_data(data)
