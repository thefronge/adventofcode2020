# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) OPTIONAL

day4data = open("day4data.txt").read().split(sep=" ")
passport_data = []

for passport in day4data:
    print(passport)
    # passport_data.append(passport.split("\n"))


# for passport in day4data:
#     print(passport)

acceptable_passports = 0
acceptable_data1 = sorted(["byr", "iyr", "eyr", "hgt",
                          "hcl", "ecl", "pid", "cid"])
acceptable_data2 = acceptable_data1.remove("cid")


def read_passport(passport):
    passport_fields = []
    for line in passport:
        if line != "":
            passport_fields.append(line[0:2])
        else:
            break
    if sorted(passport_fields) == acceptable_data1 or sorted(passport_fields) == acceptable_data2:
        return True
    else:
        return False


for passport in day4data:
    if read_passport(passport):
        acceptable_passports += 1
    else:
        continue

print(acceptable_passports)