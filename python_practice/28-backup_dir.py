#Example 2: Create a Directory Backup

#Write a Python script that copies a directory to a backup location.

import shutil
import os
# Directory to backup
source_dir = r"C:\Users\ambat\OneDrive\Desktop\jenkins"

# Backup destination
backup_dir =  r"C:\Users\ambat\OneDrive\Desktop\backupfiles"

# Ensure backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Copy the directory
shutil.copytree(source_dir, os.path.join(backup_dir, os.path.basename(source_dir)))

print("Backup completed successfully")