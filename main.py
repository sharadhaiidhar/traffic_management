# main.py
# CLI Controller

from config import ROADS
from vehicles import live_traffic, update_density, process_road
from reports import show_live_status, show_history
from storage import clear_logs

def run():
    while True:
        print("======BHOPAL TRAFFIC AND RAILWAY MANAGEMENT======")
        print("1. Update Road Vehicle Count")
        print("2. Run Signal Cycle for a Road")
        print("3. View Live Intersection Status")
        print("4. View Signal History Logs")
        print("5. Reset All Logs")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            print("Available roads: " + ", ".join(ROADS))
            road = input("Enter road name: ").strip().capitalize()
            if road not in ROADS:
                print("Invalid road name. Please pick from list.")
                continue

            count_str = input("Enter number of waiting vehicles: ").strip()
            if not count_str.isdigit():
                print("Invalid number. Please enter digits only.")
                continue

            update_density(road, int(count_str))
            print("Updated " + road + " count to " + count_str + ".")

        elif choice == "2":
            print("Select road to give GREEN light: " + ", ".join(ROADS))
            road = input("Enter road name: ").strip().capitalize()
            if road not in ROADS:
                print("Invalid road name.")
                continue

            emergency = input("Is there an emergency vehicle? (YES/NO): ").strip().upper()
            if emergency != "YES":
                emergency = "NO"

            allocated_time = process_road(road, emergency)
            print("\n>>> SIGNAL SWITCHED <<<")
            print("Road: " + road + " -> GREEN LIGHT ACTIVE")
            print("Duration: " + str(allocated_time) + " seconds")
            if emergency == "YES":
                print("Note: Emergency priority override was triggered.")
            print("Traffic on " + road + " cleared.\n")

        elif choice == "3":
            show_live_status()

        elif choice == "4":
            show_history()

        elif choice == "5":
            clear_logs()
            print("All signal logs have been wiped.\n")

        elif choice == "6":
            print("Shutting down traffic system. Goodbye!")
            break

        else:
            print("Invalid choice, choose between 1 and 6.\n")

if __name__ == "__main__":
    run()
