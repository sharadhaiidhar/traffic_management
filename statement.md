
### `statement.md`

```markdown
# Project Statement - Smart Traffic Management System

## Problem Statement
Traditional traffic lights run on hardcoded timers regardless of actual road conditions. This causes unnecessary waiting times when empty lanes get green lights while heavily packed lanes stay stuck on red. Additionally, emergency vehicles like ambulances often get delayed behind regular traffic queues. This project aims to simulate a responsive junction system where signal time adjusts dynamically based on vehicle density and emergency presence.

## Scope of the Project
- Controls a single 4-way junction covering North, South, East, and West roads.
- Accepts vehicle queue inputs per road directly through the command line.
- Dynamically assigns green light duration between 5 to 45 seconds.
- Includes an emergency clearance rule to prevent delays for critical responders.
- Stores operational history in an append-only text file for auditing.

## Target Users
- Traffic junction operators and station supervisors.
- Instructors and students testing basic rule-based queue management logic.

## High-Level Features
- **Dynamic Timing**: Allocates 5s for empty roads, 15s for low traffic, 30s for moderate traffic, and 45s for heavy traffic.
- **Emergency Override**: Instantly gives maximum green clearance when an emergency vehicle is detected.
- **Live Status Display**: Shows current waiting vehicles across all four directions.
- **Log History & Reset**: Saves event history to `traffic_log.txt` and provides an option to clear old records.
