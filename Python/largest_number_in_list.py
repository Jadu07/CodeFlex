def largest_number_in_list(list1):
    largest_number = 0
    for i in list1:
        if i > largest_number:
            largest_number = i
    return largest_number


def main():
    user_numbers = input("Enter elements of list separtaed by spaces : ").split(" ")
    user_list = [float(elem) for elem in user_numbers]
    largest_value = largest_number_in_list(user_list)
    print(f"\nThe largest number in the list {user_list} is {largest_value}.")

if __name__=='__main__':
    main()