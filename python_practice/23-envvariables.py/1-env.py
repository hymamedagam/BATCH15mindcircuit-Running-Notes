import os
user = os.getenv("USERNAME")
sys_home = os.getenv("HOME")
print(f"user environment variable is {user}")
print(f"system home variable is {sys_home}")