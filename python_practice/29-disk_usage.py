#Write a Python script that checks the disk usage of a directory and prints a warning if it exceeds a certain threshold.


import shutil

#shutil: This module provides a higher-level interface for file operations, including copying entire directories.

monitor_dir = r"C:"
# Disk usage threshold (in percentage)
threshold = 80

# Get disk usage
total, used, free = shutil.disk_usage(monitor_dir)

print(total, used, free)   ## Print total, used, and free bytes on the disk

usage_percent = used / total * 100  

# Check if usage exceeds threshold
if usage_percent > threshold:
    print(f"Warning: Disk usage is {usage_percent:.2f}%")
else:
    print(f"Disk usage is {usage_percent:.2f}%, within the threshold")
	