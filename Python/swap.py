def swap():
    number_1 = float(input("Enter first number : "))
    number_2 = float(input("Enter second number : "))

    number_1 = number_1 + number_2
    number_2 = number_1 - number_2
    number_1 = number_1 - number_2

    print(f"\nThe swapped numbers are : {number_1: .2f} and {number_2: .2f} respectively.")

def main():
    swap()

if __name__=='__main__':
    main()