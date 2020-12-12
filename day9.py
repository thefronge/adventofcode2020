day9data = open("day9data.txt").read().split("\n")
preamble = []


def sum_check(number: str, data_set: list) -> bool:
    number_int = int(number)

    for i in data_set:
        for n in data_set:
            if int(i) + int(n) == number_int:
                if i != n:
                    return True

    return False


# part1
for line in day9data:

    if len(preamble) < 25:
        preamble.append(line)

    elif len(preamble) == 25:
        if sum_check(line, preamble) is True:
            preamble.pop(0)
            preamble.append(line)
        else:
            invalid_number = line
            print(invalid_number)
            break


# part2
def invalid_sum_check(number: str, data_set: list) -> bool:
    number_int = int(number)
    total_sum = 0
    sum_list = []

    for i in data_set:
        sum_list.append(i)
        total_sum += int(i)
        if total_sum < number_int:
            continue
        elif total_sum == number_int:
            sum_list_sorted = sorted(sum_list)
            print(int(sum_list_sorted[0]) + int(sum_list_sorted[-1]))
            return True
        elif total_sum > number_int:
            return False


line_number = 0
for line in day9data:
    data_set = day9data[line_number:]
    if invalid_sum_check(invalid_number, data_set) is True:
        break
    else:
        line_number += 1
