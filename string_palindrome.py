def string_palindrome(words):
    words = words.lower().replace(" ", "")
    return words == words[::-1]

def main():
    user_word = input("Enter a string : ")
    print(f"\n'{user_word}' is a palindrome.") if string_palindrome(user_word) else print(f"\n'{user_word}' is not a palindrome.")

if __name__=='__main__':
    main()