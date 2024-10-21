def find_largest_number(numbers):
    if len(numbers) == 0:
        return None  
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
numbers = [12, 35, 1, 10, 34, 1]
print("The largest number is:", find_largest_number(numbers))
