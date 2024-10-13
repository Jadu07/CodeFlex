def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10
    return total

def main():
    user_number = int(input("Enter an integer : "))
    required_sum = sum_of_digits(user_number)
    print(f"\nThe sum of the digits of the integer {user_number} is {required_sum}.")

if __name__=='__main__':
    main()