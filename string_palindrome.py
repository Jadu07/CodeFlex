import string

def is_palindrome(s):
    # Clean input by removing punctuation and converting to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Keep only alphanumeric characters
    return cleaned == cleaned[::-1]

def main():
    # Ask the user to input multiple strings separated by commas
    user_input = input("Enter strings separated by commas: ")
    # Split the input into a list of strings
    strings = [s.strip() for s in user_input.split(',')]
    
    # Iterate over each string and check if it's a palindrome
    for s in strings:
        if is_palindrome(s):
            print(f"'{s}' is a palindrome.")
        else:
            print(f"'{s}' is not a palindrome.")

if __name__ == '__main__':
    main()
