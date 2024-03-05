def display_divisible_by(numbers, divider):
    print("Given list: ", numbers)
    print("Divisible by", divider)
    for i in range(len(numbers)):
        if numbers[i]%divider == 0:
            print(numbers[i])



numbers = [10, 20, 33, 46, 55]
display_divisible_by(numbers, 5)