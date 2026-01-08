# Exercise 1: Random Sentence Generator
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_words_from_file(user_file):
    with open(f"{dir_path}/{user_file}", "r", encoding="utf-8") as work_file:
        return [word for line in work_file for word in line.split()]


def get_random_sentence(length_sentence):
    return " ".join(random.choices(get_words_from_file("words.txt"), k=length_sentence)).lower()


def validation(sentence_length):
    return int(sentence_length) if sentence_length.isnumeric() and 2 <= int(sentence_length) <= 20 else None


def main():
    sentence_length = input("Please input length of sentence between 2 and 20: ")
    if validation(sentence_length):
        print(get_random_sentence(int(sentence_length)))
    else:
        print("Error")
        return


main()

# Exercise 2: Working with JSON
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

dict_sample = json.loads(sampleJson)
print(dict_sample["company"]["employee"]["payable"]["salary"])
dict_sample["company"]["employee"].update({"birth_date": "2000-05-15"})
with open(f"{dir_path}/WorkSalary.json", "w", encoding="utf-8") as f:
    json.dump(dict_sample, f, indent=2, skipkeys=True)
