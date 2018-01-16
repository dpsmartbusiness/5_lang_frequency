import re
import sys
import collections


def load_data(file_path):
    with open(file_path, 'r', encoding='ANSI') as text:
        read_text = text.read()
    return read_text


def get_most_frequent_words(text):
    text = re.split(r'\W+', text)
    duplicate_words_counter = collections.Counter(text)
    return duplicate_words_counter.most_common(10)


if __name__ == '__main__':
    try:
        top_frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
        print ("Список из 10 слов наиболее часто встречающихся в тексте: \n")
        for word,frequency in top_frequent_words:
            print('Cлово: {} | Частота: {}'.format(word, frequency))
    except FileNotFoundError:
        print('Некорректный путь к файлу.')
    except IndexError:
        print('Укажите путь к файлу.')




