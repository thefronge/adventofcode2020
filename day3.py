# part1
# day3data = open("day3data.txt").read().splitlines()
# pos = 0
# tree_count = 0

# for line in day3data:
#     if pos < len(line):
#         if line[pos] == "#":
#             tree_count += 1
#             pos += 3
#         else:
#             pos += 3
#     else:
#         pos -= len(line)
#         if line[pos] == "#":
#             tree_count += 1
#             pos += 3
#         else:
#             pos += 3

# print(tree_count)

# part2

day3data = open("day3data.txt").read().splitlines()
first_path = [1, 1]
second_path = [3, 1]
third_path = [5, 1]
fourth_path = [7, 1]
fifth_path = [1, 2]


def toboggan_move(moves: list, forest: list) -> int:
    pos = 0
    tree_count = 0
    horiz_move = moves[0]
    vert_move = moves[1]

    for line in forest:
        if vert_move == 0:
            pos += horiz_move
            if pos < len(line):
                if line[pos] == "#":
                    tree_count += 1
                    vert_move = moves[1] - 1
                else:
                    vert_move = moves[1] - 1
            else:
                pos -= len(line)
                if line[pos] == "#":
                    tree_count += 1
                    vert_move = moves[1] - 1
                else:
                    vert_move = moves[1] - 1
        else:
            vert_move -= 1

    return tree_count


print(toboggan_move(first_path, day3data) *
      toboggan_move(second_path, day3data) *
      toboggan_move(third_path, day3data) *
      toboggan_move(fourth_path, day3data) *
      toboggan_move(fifth_path, day3data))
