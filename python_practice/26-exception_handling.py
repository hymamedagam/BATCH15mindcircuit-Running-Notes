try:
    with open('devops_b16.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File was not found, check once again")
except IOError:
    print("Error: IO error occured")
except PermissionError:
    print("Error: You do not have required permissions to reaad the file")
except Exception as e:
    print(f"Unknown error occured: {e}")