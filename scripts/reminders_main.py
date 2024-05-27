from reminder_utils import process_reminder_request, check_due_reminders
from datetime import datetime

def main():
    reminder_text = input("Enter reminder text: ")
    reminder_time_input = input("Enter reminder time (YYYY-MM-DD HH:MM:SS): ")
    print("Enter the reminder date and time:")
    year = int(input("Year: (e.g., 2024):"))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59):"))
    
# Create a datetime object from the user input, appends the datetime
    reminder_time = datetime(year, month, day, hour, minute)
    
# Process the reminder request
    process_reminder_request(reminder_text, reminder_time)  

# Attempt to parse the input time string into a datetime object
    try:
        reminder_time = datetime.strptime(reminder_time_input, "%Y-%m-%d %H:%M:%S")
        process_reminder_request(reminder_text, reminder_time)
        check_due_reminders()
    except ValueError:
        print("Invalid input format. Please enter the time in the format 'YYYY-MM-DD HH:MM:SS'.")

#def main():
    # Example of adding a new reminder
    # Year, Month, Day, Hour, Minute
    # Process_reminder_request(reminder_text, reminder_time)
    # Optionally, you could add a loop here to handle ongoing inputs or commands.

# Run this script first
# Script to ensure main function is executed when the script is run directly    
if __name__ == "__main__":
    main()
