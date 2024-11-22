import random

kms = random.sample(range(1, 8), 3)
km1, km2, km3 = kms

cargo1 = [km1, 250]
cargo2 = [km2, 300]
cargo3 = [km3, 163]

mark1 = int(input())
mark2 = int(input())
mark3 = int(input())

if mark1 == km1 and mark2 == km2 and mark3 == km3:
    print("Martians have succesfully found all the 713 kg of cargo")
else:
    while mark1 != km1 and mark2 != km2 and mark3 != km3:
        kms = random.sample(range(1, 8), 3)
        km1, km2, km3 = kms

        cargo1 = [km1, 250]
        cargo2 = [km2, 300]
        cargo3 = [km3, 163]

        mark1 = int(input())
        mark2 = int(input())
        mark3 = int(input())