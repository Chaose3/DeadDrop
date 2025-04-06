import os
import json
from datetime import datetime, timedelta
import getpass

# Config
PASSWORD = "your_secret_password"  # Change this
MESSAGE = "This is my death drop message."  # Customize this
CHECKIN_FILE = "checkin.json"
DROP_FILE = "death_drop.txt"
ALLOWED_DELAY_HOURS = 24  # 1 day

def save_checkin():
	with open(CHECKIN_FILE, "w") as f:
		json.dump({"last_checkin": datetime.now().isoformat()}, f)

def load_checkin():
	if not os.path.exists(CHECKIN_FILE):
		return None
	with open(CHECKIN_FILE, "r") as f:
		data = json.load(f)
		return datetime.fromisoformat(data["last_checkin"])

def trigger_drop():
	with open(DROP_FILE, "w") as f:
		f.write(f"Death Drop Triggered:\n\n{MESSAGE}")
	print("💀 Death drop triggered! Message written to death_drop.txt")

def main():
	last_checkin = load_checkin()
	now = datetime.now()

	if last_checkin:
		if now - last_checkin > timedelta(hours=ALLOWED_DELAY_HOURS):
			trigger_drop()
			return
	else:
		print("🔔 First time running. Make sure to check in daily!")

	# Prompt for password
	password = getpass.getpass("Enter today's password: ")
	if password == PASSWORD:
		save_checkin()
		print("✅ Check-in successful.")
	else:
		print("❌ Wrong password. No check-in recorded.")

if __name__ == "__main__":
	main()