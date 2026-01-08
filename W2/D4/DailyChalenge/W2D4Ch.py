import os
import string
import re


class Text:
    """This class create object with one text parameter type string"""
    def __init__(self, text):
        self.text = text
    @classmethod
    def from_file(cls, file_path):
        """Classmethod for creating text for Text object from the file"""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/{file_path}", "r", encoding="utf-8") as work_file:
            return cls(work_file.read())
    # IT IS PLACE FOR STATICK METHOD
    @property
    def split(self):
        """This is property method which return separate text to the individual words uses spase as a separator"""
        return self.text.lower().split()

    def word_frequency(self, word):
        """This method count how many times certain word is in the text"""
        count = self.split.count(word.lower())
        return count if count != 0 else None

    def most_common_word(self):
        """Method create a dictionary from all words in the text and using method 'frequency' find value for each
        keys"""
        count_word_dict = {}
        for each_word in self.unique_words():
            count_word_dict.update({each_word: self.word_frequency(each_word)})
        return max(count_word_dict, key=count_word_dict.get)

    def unique_words(self):
        """Method create a set (uniq words) from list of words"""
        return set(self.split)




class TextModification(Text):

    def remove_punctuation(self):
        cleaned_text = ''.join(ch for ch in self.text if ch not in string.punctuation)
        return cleaned_text

    def remove_stop_words(self):
        split_words = self.split
        return ' '.join(words for words in split_words if words not in ["and", "is", "a"])

    def remove_special_characters(self, character):
        pattern = re.escape(character)
        return re.sub(pattern, '', self.text)


# text1 = Text("One two free one two two one one two two two two")
# print(text1.word_frequency("two"))
# print(text1.most_common_word())

text2 = TextModification.from_file("workFile.txt")
# print(text2.remove_punctuation())
# print(text2.remove_stop_words())
print(text2.remove_special_characters("4"))
