import sys
import time
number = 0

while True:
    try:
        print("")
        print(f"Current Number - {number}")
        number = 1 + number
        time.sleep(5)
    except KeyboardInterrupt:
        print("")
        print("[X] Action Stopped")
        sys.exit()