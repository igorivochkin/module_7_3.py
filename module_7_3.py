#module_7_3.py
from dataclasses import replace
from pprint import pprint

class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        exclude_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        line_new = ''
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for line in file:#считать строку из файла
                line = line.lower() #строка приведена к строчным
                for char in line:
                    if char in exclude_:
                        line = line.replace(char, '') # исключить символы если есть
                line_new += line
                all_words.update({self.file_name: line_new.split()})
        return all_words

    def find(self, word):
        find_word = {}
        words = self.get_all_words()[self.file_name]
        for i in range(len(words)):
            if words[i] == word.lower():
                find_word.update({self.file_name: i+1})
                return find_word

    def count(self, word):
        count_word = {}
        words = self.get_all_words()[self.file_name]
        count_word.update({self.file_name: words.count(word.lower())})
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
