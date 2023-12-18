file = open("./funny.txt", "r")
transfer = open("./transfer.txt", "w")
for lines in file:
    temp = lines.split(" ")
    transfer.write(lines+ " count " + str(len(temp)))
    print(f'{lines},count : {len(temp)}')