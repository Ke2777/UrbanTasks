class WordsFinder:
    def __init__(self, *file_name_list):
        self.file_name_list = list(file_name_list)

    def get_all_words(self):
        all_words = {}
        exept = [',', '.', '=', '!', '?', ';', ':', '-']
        for file_name in self.file_name_list:
            list_words = []
            with open(file_name, encoding='utf-8') as f:
                for string in f:
                    string = string.lower()
                    for word in exept:
                        if word in string:
                            string = string.replace(word, '')
                    list_words += string.split()
                    all_words[file_name] = list_words
        return all_words

    def find(self, word):
        word = word.lower()
        found_word = {}
        all_words = self.get_all_words()
        for file_name, words_list in all_words.items():
            word_pos = 0
            for is_word in words_list:
                word_pos += 1
                if word == is_word:
                    found_word[file_name] = word_pos
                    break
        return found_word

    def count(self, word):
        word = word.lower()
        words_count = {}
        all_words = self.get_all_words()
        for file_name, words_list in all_words.items():
            count = 0
            for is_word in words_list:
                if word == is_word:
                    count += 1
            words_count[file_name] = count
        return words_count


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
