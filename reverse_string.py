def reverse_string(words):
    return words[::-1]

def main():
    user_word = input("Enter a string : ")
    reversed_word = reverse_string(user_word)
    print(f"\nThe reversed string for {user_word} is {reversed_word}.")

if __name__=='__main__':
    main()