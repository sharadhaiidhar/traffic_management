# storage.py
# Basic text file operations
from config import LOG_FILE
def read_logs():
    records = []
    try:
        f = open(LOG_FILE, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                entry = {
                    "road": parts[0],
                    "vehicles": int(parts[1]),
                    "emergency": parts[2],
                    "green_time": int(parts[3])
                }
                records.append(entry)
    except FileNotFoundError:
        f = open(LOG_FILE, "w")
        f.close()
    return records

def append_log(road, count, emergency, green_time):
    f = open(LOG_FILE, "a")
    line = road + "," + str(count) + "," + emergency + "," + str(green_time) + "\n"
    f.write(line)
    f.close()

def clear_logs():
    f = open(LOG_FILE, "w")
    f.close()
