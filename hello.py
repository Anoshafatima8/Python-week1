from datetime import datetime

# Prints a friendly hello with today's local date (YYYY-MM-DD)
today = datetime.now().strftime("%Y-%m-%d")
print(f"Hello, World! Today is {today}.")