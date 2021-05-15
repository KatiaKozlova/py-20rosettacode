import requests
import re

the_language = ''
set_of_languages = ['BASIC', 'C sharp', 'C sharp|C#', 'C', 'C++', 'Java', 'Python', 'Fortran', 'Pascal',
                    'Icon}} and {{header|Unicon']

with open('set.txt', 'r', encoding='utf-8') as the_set:  # открываем файл со списком названий программ
    for problem in the_set:  # проходим по списку
        problem = problem.strip()
        new_link = 'http://www.rosettacode.org/wiki/Special:Export/' + problem
        r_new = requests.get(new_link)  # выгружаем xml-код для каждой программы
        r = re.findall(
            r'=={{header\|(BASIC|C\ssharp|C\ssharp\|C#|C|C\+\+|Java|Python|Fortran|Pascal|Icon}}\sand\s{{header\|Unicon)}}==([^ё]+?)([Oo]utput|=={{header)',
            r_new.text)
        # при помощи регулярки находим места в коде с программами на "наших" языках
        for i in r:  # записываем в отдельный файл для каждого языка
            if i[0] == 'C sharp|C#':
                with open('C sharp.txt', 'a', encoding='utf-8') as file:
                    file.write(i[1] + '\n')
            elif i[0] == 'Icon}} and {{header|Unicon':
                with open('Unicon.txt', 'a', encoding='utf-8') as file:
                    file.write(i[1] + '\n')
            else:
                with open(i[0] + '.txt', 'a', encoding='utf-8') as file:
                    file.write(i[1] + '\n')
