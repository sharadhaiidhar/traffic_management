# vehicles.py
# Tracks live counts on each road

from config import ROADS
from storage import append_log
from signals import calculate_signal_time

live_traffic = {
    "North": 0,
    "South": 0,
    "East": 0,
    "West": 0
}
def update_density(road, count):
    if road in live_traffic:
        live_traffic[road] = count
        return True
    return False

def process_road(road, emergency_flag):
    count = live_traffic.get(road, 0)
    green_duration = calculate_signal_time(count, emergency_flag)
    
    append_log(road, count, emergency_flag, green_duration)
    
    live_traffic[road] = 0
    return green_duration
