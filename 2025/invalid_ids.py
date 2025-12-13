# Advent of code - 2025 - Day 2: Secret Entrance - https://adventofcode.com/2025/day/2

def sum_all_invalid_ids(ranges) -> int:
    sum = 0
    for arange in ranges:
        for num in range(int(arange[0]), int(arange[1]) + 1):
            if is_invalid_id_part_two(num):
                sum = sum + num
    return sum

def is_invalid_id_part_two(num: int) -> int:
    middle = int(len(str(num)) / 2)
    for nof_digits in range(1, middle + 1):
        pattern = str(num)[:nof_digits]
        repeat = str(num).count(pattern)
        if nof_digits * repeat == len(str(num)):
            return True
    return False

def is_invalid_id(num: int) -> int:
    if len(str(num)) % 2 == 0:
        middle = int(len(str(num)) / 2)
        first = str(num)[:middle]
        second =  str(num)[middle:]
        return int(first) == int(second)

def read_input_from_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        input = file.readline()
    input_ranges = input.split(",")
    
    ranges = []
    for input_range in input_ranges:
        range = input_range.split("-")
        ranges.append(tuple(range))
    return ranges

def main():
    file_name = "invalid_ids.txt"
    ranges = read_input_from_file(file_name)
    result = sum_all_invalid_ids(ranges)
    print(result)

main()