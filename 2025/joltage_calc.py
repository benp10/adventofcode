# Advent of code - 2025 - Day 3: Secret Entrance - https://adventofcode.com/2025/day/3

def calc_total_joltage(power_banks) -> int:
    sum = 0
    for power_bank in power_banks:
        joltage = calc_bank_joltage(power_bank)
        sum = sum + joltage
    return sum

def calc_bank_joltage(power_bank: str) -> int:
    num_digits = 12
    max_digit = -1
    max_index = -1
    result = 0
    for current_digit in range(1, num_digits + 1):
        for index in range(max_index + 1, len(power_bank) - num_digits + current_digit):
            if int(power_bank[index]) > max_digit or max_digit < 0:
                max_digit = int(power_bank[index])
                max_index = index
            if max_digit == 9:
                break
        result = result + pow(10, num_digits - current_digit) * max_digit
        max_digit = -1
    return result

def calc_bank_joltage_old(power_bank: str) -> int:
    max_digit = -1
    max_index = -1
    index = 0
    # Find first digit
    for index in range(0, len(power_bank) - 1):
        if int(power_bank[index]) > max_digit or max_digit < 0:
            max_digit = int(power_bank[index])
            max_index = index
        if max_digit == 9:
            break
    result = 10 * max_digit
    # Find seond digit
    max_digit = -1
    for index in range(max_index + 1, len(power_bank)):
        if int(power_bank[index]) > max_digit or max_digit < 0:
            max_digit = int(power_bank[index])
        if max_digit == 9:
            break
    result = result + max_digit
    return result

def read_input_from_file(file_name: str) -> list[str]:
    power_banks = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            power_banks.append(str(line))
    return power_banks

def main():
    file_name = "power_banks.txt"
    power_banks = read_input_from_file(file_name)
    result = calc_total_joltage(power_banks)
    print(result)

main()