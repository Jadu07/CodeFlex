def reverse_string(words):
    return words[::-1]

def is_palindrome(words):
    cleaned = ''.join(c.lower() for c in words if c.isalnum())  # Clean the input
    return cleaned == cleaned[::-1]

def main():
    user_word = input("Enter a string: ")
    
    # Reverse the string
    reversed_word = reverse_string(user_word)
    # Count the number of characters
    char_count = len(user_word)
    
    # Output the reversed string and character count
    print(f"\nThe reversed string for '{user_word}' is '{reversed_word}'.")
    print(f"The string has {char_count} characters.")
    
    # Check if the string is a palindrome
    if is_palindrome(user_word):
        print(f"'{user_word}' is also a palindrome.")
    else:
        print(f"'{user_word}' is not a palindrome.")

if __name__ == '__main__':
    main()
