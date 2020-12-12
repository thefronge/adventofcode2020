# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) OPTIONAL

# part1

# day4data = open("day4data.txt").read().split("\n\n")
# processed_data = []

# for line in day4data:
#     processed_data.append(line.split())

# acceptable_passports = 0
# acceptable_data1 = sorted(["byr", "iyr", "eyr", "hgt",
#                           "hcl", "ecl", "pid", "cid"])
# acceptable_data2 = sorted(["byr", "iyr", "eyr", "hgt",
#                           "hcl", "ecl", "pid"])


# def read_passport(passport: list) -> bool:
#     passport_fields = []
#     for line in passport:
#         passport_fields.append(line[0:3])
#     if sorted(passport_fields) == acceptable_data1 or sorted(passport_fields) == acceptable_data2:
#         return True
#     else:
#         return False


# for passport in processed_data:
#     if read_passport(passport):
#         acceptable_passports += 1
#     else:
#         continue

# print(acceptable_passports)

# part 2

day4data = open("day4data.txt").read().split("\n\n")
processed_data = []

for line in day4data:
    processed_data.append(line.split())

acceptable_passports = 0
acceptable_data1 = sorted(["byr", "iyr", "eyr", "hgt",
                          "hcl", "ecl", "pid", "cid"])
acceptable_data2 = sorted(["byr", "iyr", "eyr", "hgt",
                          "hcl", "ecl", "pid"])


def validate_birthyear(birthyear: str) -> bool:
    try:
        birthyear_int = int(birthyear)
    except TypeError:
        return False
    if len(str(birthyear_int)) != 4:
        return False
    elif birthyear_int >= 1920 and birthyear_int <= 2002:
        return True
    else:
        return False


def validate_issueyear(issueyear: str) -> bool:
    try:
        issueyear_int = int(issueyear)
    except TypeError:
        return False
    if len(str(issueyear_int)) != 4:
        return False
    elif issueyear_int >= 2010 and issueyear_int <= 2020:
        return True
    else:
        return False


def validate_expyear(expyear: str) -> bool:
    try:
        expyear_int = int(expyear)
    except TypeError:
        return False
    if len(str(expyear_int)) != 4:
        return False
    elif expyear_int >= 2020 and expyear_int <= 2030:
        return True
    else:
        return False


def validate_height(height: str) -> bool:
    if type(height) != str:
        return False
    if "cm" in height:
        if len(str(height)) != 5:
            return False
        elif int(height[0:3]) >= 150 and int(height[0:3]) <= 193:
            return True
    if "in" in height:
        if len(str(height)) != 4:
            return False
        elif int(height[0:2]) >= 59 and int(height[0:2]) <= 76:
            return True
    else:
        return False


def validate_haircolor(haircolor: str) -> bool:
    valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                        "a", "b", "c", "d", "e", "f"]
    invalid_count = 0

    if type(haircolor) != str:
        return False
    if haircolor[0] != "#":
        return False
    if len(haircolor) != 7:
        return False
    for character in haircolor[1:]:
        if character in valid_characters:
            continue
        else:
            invalid_count += 1
    if invalid_count > 0:
        return False
    else:
        return True


def validate_eyecolor(eyecolor: str) -> bool:
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if type(eyecolor) != str:
        return False
    if len(eyecolor) != 3:
        return False
    if eyecolor in valid_colors:
        return True
    else:
        return False


def validate_passportid(passportid: str) -> bool:
    valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for character in passportid:
        if character in valid_characters:
            continue
        else:
            return False
    if len(passportid) == 9:
        return True
    else:
        return False


def validate_fields(passport: list) -> bool:
    passport_fields = []
    for line in passport:
        passport_fields.append(line[0:3])
    if sorted(passport_fields) == acceptable_data1 or sorted(passport_fields) == acceptable_data2:
        return True
    else:
        return False


def validate_cid(cid: any) -> None:
    pass


validator_dict = {"byr": validate_birthyear, "iyr": validate_issueyear, "eyr": validate_expyear,
                  "hgt": validate_height, "hcl": validate_haircolor, "ecl": validate_eyecolor,
                  "pid": validate_passportid, "cid": validate_cid}


for passport in processed_data:
    invalid_data = 0
    if validate_fields(passport) is False:
        invalid_data += 1
    else:
        for line in passport:
            passport_field = line[0:3]
            passport_data = line[4:]
            call_validator = validator_dict[passport_field](passport_data)
            if call_validator is True:
                continue
            if call_validator is False:
                invalid_data += 1
        if invalid_data <= 0:
            acceptable_passports += 1


print(acceptable_passports)
