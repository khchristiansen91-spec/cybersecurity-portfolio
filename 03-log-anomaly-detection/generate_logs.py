import csv
import random
import datetime

# List of users for synthetic log generation
USERS = ["alice", "bob", "charlie", "david", "erin"]
# Example IP address pool
IPS = [f"192.168.1.{i}" for i in range(2, 255)]
# Authentication status with a bias toward successful logins
STATUSES = ["SUCCESS", "FAILURE"]

NUM_RECORDS = 1000
# Current UTC time for reference
after = datetime.datetime.utcnow()

with open("auth_logs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "user", "ip", "status"])
    for _ in range(NUM_RECORDS):
        # Randomly select a time within the last 24 hours
        delta_minutes = random.randint(0, 60 * 24)
        timestamp = after - datetime.timedelta(minutes=delta_minutes)
        user = random.choice(USERS)
        ip = random.choice(IPS)
        # 90% chance of SUCCESS, 10% chance of FAILURE
        status = random.choices(STATUSES, weights=[9, 1])[0]
        writer.writerow([timestamp.isoformat(), user, ip, status])

print("Generated auth_logs.csv with synthetic authentication log entries.")
