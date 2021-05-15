import collections
import re
import csv
import enchant

d = enchant.Dict('en_US')
set_of_languages = ['BASIC', 'C sharp', 'C', 'C++', 'Java', 'Python', 'Fortran', 'Pascal', 'Unicon']  # список языков
split_symbols = '?,.=+{}[]();:%&#!<>-*^'  # символы, на которые хотим бить


def code_reading(filename):  # функция, которая вытаскивает строчки из файла
    with open(filename, encoding='utf-8') as code_file:
        code = code_file.readlines()
        return code


def split_words(codename):  # функция, которая бьет на слова и удаляет ненужное
    tokens = []
    for line in codename:
        for split_symbol in split_symbols:
            line = line.replace(split_symbol, ' ')  # заменяем все эти символы на пробел, чтобы было удобнее побить
        line_tokens = line.split(' ')  # бьем
        for token in line_tokens:
            token = token.strip('\n')  # убираем переносы
            token = token.strip('\t')
            token = token.strip(' ')
            if token and not token.isnumeric() and "'" not in token:
                tokens.append(token)  # делаем список
    return tokens


def freq_list(tokens):  # создаем частотный список переменных
    words = []
    count = collections.Counter(tokens)
    count = dict(count)  # делаем из каунтера словарь
    sorted_values = sorted(count.values())  # сортируем получившийся словарь по количеству вхождений
    for i in sorted_values:
        if i > 1:
            for k in count.keys():
                if count[k] == i and k not in words:
                    words.append(k)  # создаем ранжированный список переменных
                    break
    return words[::-1]  # разворачиваем


def tokens_list(filename):  # делаем функцию, которая сразу читает из файла и выдает токены
    return split_words(code_reading(filename))


def parser():  # функция, которая записывает в файл частотный список
    for language in set_of_languages:
        with open(language + '_new.txt', encoding='utf-8'):
            with open(language + '_freq.txt', 'w', encoding='utf-8') as freq_file:
                for word in freq_list(tokens_list(language + '_new.txt')):
                    freq_file.write(word + '\n')


def cleaner():  # функция, которая чистит от всякого
    for language in set_of_languages:
        variables_fin = []
        with open(language + '_freq.txt', 'r', encoding='utf-8') as vars_file:
            variables = vars_file.read()
            variables = variables.split()
            with open(language + '_dict.txt', 'r', encoding='utf-8') as dict_file:  # открываем файл, в котором находятся ключевые слова данного языка
                variables_dict = dict_file.read()
                variables_dict = variables_dict.split()
                for variable in variables:
                    if re.match(r'^[^a-zA-Z]*$', variable) is None:
                        if variable not in variables_dict:
                            variables_fin.append(variable)  # оставляем только те, которые не входят в ключевые слова языка
                with open(language + '_freq1.txt', 'w', encoding='utf-8') as variables_file_fin:  # пишем в новый файл
                    for variable_fin in variables_fin:
                        variables_file_fin.write(variable_fin + '\n')


def stat_counter():  # функция, которая считает статистику и закидывает ее в тсв файл
    with open('all_stat.tsv', 'w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="\t")
        file_writer.writerow(
            ['Язык', 'Средняя длина переменной', 'Средняя длина токена', 'Количество переменных на токен',
             'Количество слов на токен', 'Количество дэшей на токены', 'Количество бб на токены'])
        for language in set_of_languages:
            num = 0
            real_word = 0
            with open(language + '_freq1.txt', 'r', encoding='utf-8') as freq_file:
                tokens = freq_file.read()
                q_dash = tokens.count('_')
                q_upper = len(re.findall(r'[A-Z]', tokens))  # считаем, сколько больших букв
                tokens = tokens.split('\n')
                average_dash = q_dash / len(tokens)
                average_upper = q_upper / len(tokens)  # считаем, сколько дэшей
                average_vars = sum(len(token) for token in tokens) / len(tokens)  # считаем среднюю длину переменной
                average_tokens = sum(len(word) for word in tokens_list(language + '_new.txt')) / len(
                    tokens_list(language + '_new.txt'))  # считаем среднюю длину всех слов
                for item in tokens_list(language + '_new.txt'):
                    if item in tokens:
                        num += 1
                token_per_token = num / len(tokens_list(language + '_new.txt'))  # считаем, сколько переменных в среднем на токен
                for token in tokens:
                    if token:
                        if d.check(token) and len(token) > 1:  # считаем, какая часть переменных является реальными словами английского языка
                            real_word += 1
                average_realwords = real_word / len(tokens)
                file_writer.writerow(
                    [language, average_vars, average_tokens, token_per_token, average_realwords, average_dash,
                     average_upper])  # дописываем все в табличку


parser()
cleaner()
stat_counter()
