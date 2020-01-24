import sys
def hello():
    print("Hello")
    print("Hi")
    print("Hey")

while True:
    try:
        hello()
    except KeyboardInterrupt:
        sys.exit()