# break_continue using while loop

i=1
while(i<=10):
    if i==6:
        break
    print(i)
    i=i+1
print("Loop ended")


# continue using while loop

j=0
while(j<10):
    j=j+1 # increment before to avoid infinite loop
    if j==6:
        continue
    print(j)
print("Loop ended")