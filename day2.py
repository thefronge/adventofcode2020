# part1

# day2data = open("day2data.txt").read().splitlines()
# valid_passwords = 0

# for line in day2data:
#     letter_count = 0
#     rule_num, rule_letter, password = line.split()
#     low_range_str, high_range_str = rule_num.split("-")
#     low_range = int(low_range_str)
#     high_range = int(high_range_str)
#     letter = rule_letter.strip(":")

#     for char in password:
#         if char == letter:
#             letter_count += 1
#         else:
#             continue

#     if low_range <= letter_count and letter_count <= high_range:
#         valid_passwords += 1
#     else:
#         continue

# print(valid_passwords)

# part2

day2data = open("day2data.txt").read().splitlines()
valid_passwords = 0

for line in day2data:
    letter_position = 0
    rule_num, rule_letter, password = line.split()
    position1_str, position2_str = rule_num.split("-")
    position1 = int(position1_str)
    position2 = int(position2_str)
    letter = rule_letter.strip(":")

    if password[position1 - 1] == letter:
        if password[position2 - 1] == letter:
            continue
        else:
            valid_passwords += 1

    if password[position2 - 1] == letter:
        if password[position1 - 1] == letter:
            continue
        else:
            valid_passwords += 1

print(valid_passwords)
