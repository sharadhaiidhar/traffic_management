# signals.py
# Signal calculation logic
from config import DEFAULT_GREEN_TIME, MAX_GREEN_TIME
def calculate_signal_time(vehicle_count, has_emergency):
     
    if has_emergency == "YES":
        return MAX_GREEN_TIME

    if vehicle_count == 0:
        return 5
    elif vehicle_count <= 10:
        return DEFAULT_GREEN_TIME
    elif vehicle_count <= 25:
        return 30
    else:
        return MAX_GREEN_TIME
