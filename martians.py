import random

kms = random.sample(range(1, 8), 3)
km1, km2, km3 = kms

cargo1 = [km1, 250]
cargo2 = [km2, 300]
cargo3 = [km3, 163]

print("Enter 3 marks")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())

while mark1 > 7 or mark2 > 7 or mark3 > 7:
    print("It's only 7 km to city. Martians have made a mistake with their marks. They should enter them again")
    mark1 = int(input())
    mark2 = int(input())
    mark3 = int(input())

if mark1 == km1 and mark2 == km2 and mark3 == km3:
    print("Martians have succesfully found all 713 kg of cargo")
else:
    while mark1 != km1 or mark2 == km2 or mark3 == km3:
        foundcargo = 0
        if mark1 == km1:
            foundcargo += 250
        if mark2 == km2:
            foundcargo += 300
        if mark3 == km3:
            foundcargo += 163

        print("Martians have found only " + str(foundcargo) + " kg of cargo")

        kms = random.sample(range(1, 8), 3)
        km1, km2, km3 = kms

        cargo1 = [km1, 250]
        cargo2 = [km2, 300]
        cargo3 = [km3, 163]

        print("Enter 3 marks")
        mark1 = int(input())
        mark2 = int(input())
        mark3 = int(input())

        while mark1 > 7 or mark2 > 7 or mark3 > 7:
            print("It's only 7 km to city. Martians have made a mistake with their marks. They should enter them again")
            mark1 = int(input())
            mark2 = int(input())
            mark3 = int(input())


        if mark1 == km1 and mark2 == km2 and mark3 == km3:
            print("Martians have succesfully found all 713 kg of cargo")
            break