day6data = open("day6data.txt").read().split("\n\n")
processed_data = []

for line in day6data:
    processed_data.append(line.split())

# part 1

# total_answers = 0

# for group in processed_data:
#     questions = {}
#     for response in group:
#         for character in response:
#             questions[character] = 0
#     total_answers += len(questions)

# print(total_answers)

# part 2

total_answers = 0

for group in processed_data:
    character_dict = {}
    questions = []
    for response in group:
        for character in response:
            questions.append(character)
    for character in sorted(questions):
        character_dict[character] = questions.count(character)
    for response_count in character_dict:
        if character_dict[response_count] == len(group):
            total_answers += 1
        else:
            continue

print(total_answers)
