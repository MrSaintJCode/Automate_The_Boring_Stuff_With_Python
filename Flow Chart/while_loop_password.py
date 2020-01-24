import sys
import time


while True:
    try:
        print("")
        name = input("Who are you: ")
        if name == 'Justin':
            print("")
            password = input(f"Hello {name}. What is the password: ")
            if password == '123':
                print(f"Welcome {name}")
                sys.exit()
        print("")
        print(f"[X] Try Again")

    except KeyboardInterrupt:
        print("")
        print("[X] Action Stopped")
        sys.exit()