# combination of environment variables and command line arguments
import os
import sys
user = os.getenv('USERNAME')
file_path = sys.argv[1]
print(f"environment variable is {user}")
print(f"File Path is {file_path}")