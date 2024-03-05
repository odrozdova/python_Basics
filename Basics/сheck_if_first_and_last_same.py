def сheck_if_first_and_last_same(numbers):
    print("Given list: ", numbers)
    result = False
    if numbers[0] == numbers[-1]:
       result = True
    return print("Result: ", result)


numbers_x = [10, 20, 30, 40, 10, 25, 10]
numbers_y = [75, 65, 35, 75, 30, 75, 75]
сheck_if_first_and_last_same(numbers_x)
сheck_if_first_and_last_same(numbers_y)