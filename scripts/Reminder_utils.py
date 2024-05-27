# reminder_utils.py
from datetime import datetime
import json

def read_reminders_from_file():
    try:
        with open("reminders.json", "r") as file:
            reminders = json.load(file)
    except FileNotFoundError:
        reminders = []
    return reminders

def write_reminders_to_file(reminders):
    with open("reminders.json", "w") as file:
        json.dump(reminders, file, indent=4)

def process_reminder_request(reminder_text, reminder_time):
    reminders = read_reminders_from_file()
    reminders.append({
        "text": reminder_text,
        "time": reminder_time.strftime("%Y-%m-%d %H:%M:%S"),  # Added a comma here
        "notes": "notes"  # Removed parentheses around "notes"
    })
    write_reminders_to_file(reminders) # write reminders to reminders.json
    print("Reminder set successfully!")


def check_due_reminders():
    reminders = read_reminders_from_file()
    current_time = datetime.now()
    
    for reminder in reminders:
        reminder_time = datetime.strptime(reminder["time"], "%Y-%m-%d %H:%M:%S")
        if current_time >= reminder_time:
            print(f"Reminder: {reminder['text']} is due!")

if __name__ == "__main__":
    main()
