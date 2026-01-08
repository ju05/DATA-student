# Challenge 1: Sorting
def input_words():
    """This function asks the user to input several words separated by commas."""
    user_words = input("Input several words separated by commas (word1,word2,...) or 'q' for quit: ")
    # if condition is for handling errors. In this case is only for quite and empty input
    if user_words == "q":
        return "quit"
    elif len(user_words) == 0:
        print("You have not entered any data! Goodbye")
        return "quit"
    else:
        return user_words


def transform_to_list(words):
    """This function transforms the input string into a list."""
    return words.split(",")


def sert_list(list):
    """This function sorts the list alphabetically."""
    return sorted(list)


def join_result(sorted_list):
    """This function joins the list elements with commas."""
    return ','.join(sorted_list)

# Main code: asks the user for input until they enter 'q' or leave it empty
a = input_words()
while a != "quit":
    print(join_result(sert_list(transform_to_list(a))))
    a = input_words()


# Challenge 2: Longest Word
def input_sentence():
    """This function asks the user to input a sentence. It also checks if the user wants to quit or submits nothing."""
    while True:
        user_sentence = input("Input a sentence or 'q' for quite: ")
        if len(user_sentence) == 0:
            print("Please, insert somthing!")
            continue
        else:
            return user_sentence  # Here can be "q" for quit.


def split_by_words(sentence):
    """This function splits the sentence into a list using space as the separator."""
    return sentence.split()


def long_word(list_words):
    """This function finds and returns the first longest word (by number of characters)."""
    # max_length = max(len(each_list) for each_list in list_words)
    # Uses 'len' as the key for comparison
    longest_list = max(list_words, key=len)
    return longest_list

# Main code: runs until the user inputs 'q'
a = input_sentence()
while a != "q":
    print(long_word(split_by_words(a)))
    a = input_sentence()
