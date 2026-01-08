import anagram_checker

while True:
    user_request = input("Type the word or 'q' to quite: ").strip()
    if user_request == "q":
        break
    elif len(user_request.split()) != 1:
        print("You should input only one word!")
    elif not user_request.isalpha():
        print("You shod input only letters!")
    else:
        output_words = anagram_checker.new_text.get_anagrams(user_request)
        if output_words:
            print(f"YOUR WORD: '{user_request.upper()}'\n"
                  f"this is a valid English word.\n"
                  f"Anagrams for your word: {', '.join(output_words).lower()}")
        else:
            print(f"YOUR WORD : '{user_request.upper()}'\n"
                  f"this is not a valid English word.")