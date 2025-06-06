#Python code to get CPU and RAM utilization
	
	
import psutil

# CPU utilization (percentage)
cpu_percent = psutil.cpu_percent(interval=1)  # interval=1 means measure over 1 second
print(f"CPU Utilization: {cpu_percent}%")

# RAM utilization
memory_info = psutil.virtual_memory()
print(f"RAM Utilization: {memory_info.percent}%")
