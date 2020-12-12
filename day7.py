day7data = open("day7data.txt").read().split("\n")
processed_data = []
bag_dict = {}
valid_bag_dict = {}
valid_bag_dict2 = {}


for line in day7data:
    processed_data.append(line.split(" bags contain "))

# make dictionary of the bags (outer (big) bag: inner (small) bags)
for bag in processed_data:
    big_bag = bag[0]
    small_bag = bag[1]
    bag_dict[big_bag] = small_bag

# check contents (inner bags) of outer bags for those which contain shiny gold bag. add outer bag to valid dict
for bag in bag_dict:
    if "shiny gold" in bag_dict[bag]:
        valid_bag_dict[bag] = 0
# above loop was manually validated to give correct number of bags (7)

# check contents (inner bags) of outer bags for those which contain valid bags. add outer bag to secondary valid dict
for bag in bag_dict:
    for valid_bag in valid_bag_dict:
        if valid_bag in bag_dict[bag]:  # valid_bag_dict2 used because valid_bag_dict size increases as loop iterates
            valid_bag_dict2[bag] = 0

# combine two valid bag dicts
for bag in valid_bag_dict2:
    valid_bag_dict[bag] = 0

print(len(valid_bag_dict))
