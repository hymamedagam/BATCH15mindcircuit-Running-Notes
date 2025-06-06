#writing a file
with open('devops_b15.txt', 'w') as file:
    file.write("Hello, AWS DevOps BATCH15 champs\n")
    file.write("Work hard\n")


#reading a file

with open('devops_b15.txt', 'r') as file:
    content = file.read()
    print(content)

#appending a file

with open('devops_b15.txt', 'a') as file:
    file.write("Appending a new line\n")

#reading a file

with open('devops_b15.txt', 'r') as file:
    Updated_content = file.read()
    print(Updated_content)