# reports.py
# Display functions

from vehicles import live_traffic
from storage import read_logs

def show_live_status():
    print("\n----- CURRENT INTERSECTION QUEUE -----")
    for road in live_traffic:
        print("Road: " + road + " | Waiting Vehicles: " + str(live_traffic[road]))
    print("--------------------------------------\n")

def show_history():
    logs = read_logs()
    print("\n---------------- SIGNAL LOG HISTORY ----------------")
    if len(logs) == 0:
        print("No traffic logs recorded yet.")
    else:
        for idx, log in enumerate(logs):
            print(str(idx + 1) + ". Road: " + log["road"] + 
                  " | Vehicles: " + str(log["vehicles"]) + 
                  " | Emergency: " + log["emergency"] + 
                  " | Green Given: " + str(log["green_time"]) + "s")
    print("----------------------------------------------------\n")
