"""
Вы очень любите считать. Не важно что, где и когда, главное посчитать все, что можно.
Вам на вход приходит текст. Ваша программа должна посчитать количество слов в этом тексте и вывести на печать 10
самых частых слов. Если слова встречаются одинаковое количество раз, то они должны быть отсортированы по алфавиту.

Ограничения:
- игнорируем знаки препинания (тире, запятые, многоточия и т.п.)
- слово, это все то, что отделено пробелом, символом табуляции или символом перевода строки.
- регистр игнорируется
- слова короче 3-х символов игнорируются.


Советы:
1) почитать про регулярные выражения в питоне, для визуального представления можно пользоваться сайтом https://regex101.com/
2) вспомнить про sorted, почитать про lambda функции и сортировку с их помощью

для тестирования запустить pytest 2_task/test.py
"""
import re


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    text_without_short_word = re.sub(r"\b\w{1,2}\b", '', text)
    text_without_punctuation = re.split(r"[^\w]", text_without_short_word)
    list_of_separate_words = [i.lower() for i in text_without_punctuation if i != ""]
    sorted_list_separate_words = sorted(list_of_separate_words)

    words_and_their_count = {}

    for word in sorted_list_separate_words:
        words_and_their_count.setdefault(word, 0)
        words_and_their_count[word] += 1
    
    words_and_their_count = dict(sorted(words_and_their_count.items(), key=lambda item: item[1], reverse=True))

    most_common = {}

    for word, count in words_and_their_count.items():
        most_common.setdefault(word, count)
        
        if len(most_common) == 10:
            break

    return most_common
