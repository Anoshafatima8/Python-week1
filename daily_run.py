import schedule
import time
import os

def run_bulk_rename():
    folder_path = r"C:\Users\Anosha\Pictures\MyImages"  # Change this to your folder
    os.system(f'python bulk_rename.py "{folder_path}"')

# Schedule the task every day at 9:00 AM
schedule.every().day.at("09:00").do(run_bulk_rename)

print("Scheduler is running... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
