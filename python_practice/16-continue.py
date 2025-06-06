#continue example

i = 1
while i <= 10:
    if i == 5:
        i = i + 1  # increment before continue to avoid infinite loop
        continue
    print(f"the number is: {i}")
    i = i + 1
print("Loop ended")