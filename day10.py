day10data = open("day10data.txt").read().split()
day10data_int = [int(line) for line in day10data]

# part1
# volt_diff_3 = []
# volt_diff_1 = []
# previous_line = 0

# for line in sorted(day10data_int):
#     if line - previous_line == 1:
#         volt_diff_1.append(1)
#     if line - previous_line == 3:
#         volt_diff_3.append(1)
#     previous_line = line

# print(len(volt_diff_1) * (len(volt_diff_3) + 1))

# part2
# fuck
