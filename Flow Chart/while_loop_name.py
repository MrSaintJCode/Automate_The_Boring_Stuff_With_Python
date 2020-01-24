import sys
name = ''
while name != 'Justin':
    try:
        name = input('What is your name: ')
    except KeyboardInterrupt:
        print("")
        print(f"Action Canceled")
        sys.exit()

    
print(f'Hello {name}')