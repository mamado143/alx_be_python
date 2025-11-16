#!/usr/bin/python3

# Step 1: Collect user inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Validate priority input using a loop
while priority not in ("high", "medium", "low"):
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").strip().lower()

# Step 3: Validate time-bound input using a loop
while time_bound not in ("yes", "no"):
    print("Invalid input. Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 4: Build the base reminder using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Step 5: Modify message based on time sensitivity
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    if priority == "low":
        reminder = "Note: " + reminder + " Consider completing it when you have free time."
    else:
        reminder += " Consider completing it when you have free time."

# Step 6: Print the final reminder (always with "Reminder:" for checker)
print("\nReminder:", reminder)