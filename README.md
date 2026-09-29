# BHOPAL TRAFFIC AND RAILWAY MANAGEMENT

This is a simple console project to manage traffic signals at a standard 4-way intersection (North, South, East, and West). Instead of using fixed timers that make cars wait on empty roads, this program checks how many cars are queued up and decides how many seconds of green light to give. It also allows emergency vehicles to skip the normal wait.

All data is sorted directly in a text file without any database or external packages, and it runs entirely inside the terminal.

## What This Project Does

- Lets you enter the number of waiting cars for each lane.
- Changes green signal time based on road congestion (empty lanes get minimal time, busy lanes get more time).
- Gives immediate priority and maximum green time if an emergency vehicle arrives.
- Saves all signal operations into a simple log file (`traffic_log.txt`).
- Lets you view the current status of all roads and read past logs.

## Requirements

- Python 3 (installed on your system).
- No external librries or pip installations required.

## How to Run

1. Open your terminal or command prompt.
2. Go to the project folder:
   ```bash
   cd traffic_management
