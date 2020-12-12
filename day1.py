day1data_str = open("day1data.txt").read().splitlines()
day1data_int = [int(i) for i in day1data_str]

# for firstnumber in day1data_int:
#     for secondnumber in day1data_int:
#         if firstnumber + secondnumber == 2020:
#             print(firstnumber, secondnumber)
#             print(firstnumber * secondnumber)
#         else:
#             continue

for firstnumber in day1data_int:
    for secondnumber in day1data_int:
        for thirdnumber in day1data_int:
            if firstnumber + secondnumber + thirdnumber == 2020:
                print(firstnumber, secondnumber, thirdnumber)
                print(firstnumber * secondnumber * thirdnumber)
            else:
                continue
