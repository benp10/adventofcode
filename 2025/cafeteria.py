# Advent of code - 2025 - Day 5: Cafeteria - https://adventofcode.com/2025/day/5
# Tried a dictionary of id -> bool, doesn't work

# Solution for part 1
def count_fresh_ingedients(fresh_ranges: list[tuple], ingredients: list[int]) -> int:
    # This is O(n*m), not very efficient, but was quick on the input. 
    count = 0
    for ing in ingredients:
        for fresh_range in fresh_ranges:
            if ing >= fresh_range[0] and ing <= fresh_range[1]:
                count = count + 1
                break
    return count

# Solution for part 2
def count_fresh_ids(fresh_ranges: list[tuple]) -> int:
    # kind of an insertion sort I think
    sorted_ranges_list = []
    for fresh_range in fresh_ranges:
        if len(sorted_ranges_list) == 0:
            sorted_ranges_list.append((fresh_range[0], "Begin"))
            sorted_ranges_list.append((fresh_range[1], "End"))
        else:
            idx = 0
            while idx < len(sorted_ranges_list) and fresh_range[0] > sorted_ranges_list[idx][0]:
                idx = idx + 1
            sorted_ranges_list.insert(idx, (fresh_range[0], "Begin"))
            while idx < len(sorted_ranges_list) and fresh_range[1] >= sorted_ranges_list[idx][0]:
                idx = idx + 1
            sorted_ranges_list.insert(idx, (fresh_range[1], "End"))
    print(sorted_ranges_list)

    # Now as long as we got more "Begin" then "End", we count. We could also simply use a stack for this part.
    total_count = 0
    begin_count = 0
    last_start = 0
    for item in sorted_ranges_list:
        if item[1] == "Begin":
            if begin_count == 0:
                last_start = item[0]
            begin_count = begin_count + 1
        if item[1] == "End":
            begin_count = begin_count - 1
            if begin_count == 0:
                total_count = total_count + (item[0] - last_start + 1)
    return total_count

def read_input_from_file(file_name: str) -> tuple:
    fresh_ranges = []
    ingredients = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            if line.find("-") > 0:
                range_str = line.split("-")
                fresh_ranges.append((int(range_str[0]), int(range_str[1])))
            elif line.isnumeric():
                ingredients.append(int(line))
            
    return (fresh_ranges, ingredients)
    
def main():
    file_name = "cafeteria.txt"
    (fresh_ranges, ingredients) = read_input_from_file(file_name)
    result = count_fresh_ids(fresh_ranges)
    print(result)

main()