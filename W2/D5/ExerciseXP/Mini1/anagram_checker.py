import os


class AnagramChecker:
    def __init__(self, text):
        self.text_list = text.split()

    @classmethod
    def text_from_file(cls, file_path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/{file_path}", "r", encoding="utf-8") as work_file:
            return cls(work_file.read())

    @staticmethod
    def transform_word(word):
        return word.upper()

    def is_valid_word(self, word):
        return True if self.transform_word(word) in self.text_list else False

    def is_anagram(self, word_to_compare, word_from_list):
        if len(word_from_list) != len(word_to_compare) or word_to_compare == word_from_list:
            return False
        split_list_word = list(word_from_list)
        for character in list(word_to_compare):
            if character in split_list_word:
                split_list_word.remove(character)
        return True if not split_list_word else False

    def get_anagrams(self, word):
        if not self.is_valid_word(word):
            return False
        compare_word = self.transform_word(word)
        list_words = []
        for each_word in self.text_list:
            if self.is_anagram(compare_word, each_word):
                list_words.append(each_word)
        return list_words


file_path = "sowpods.txt"
new_text = AnagramChecker.text_from_file(file_path)

