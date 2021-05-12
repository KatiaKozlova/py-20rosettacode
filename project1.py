set_of_languages = ['BASIC', 'C_sharp', 'C', 'C%2B%2B', 'Java', 'Python', 'Fortran', 'Pascal', 'Unicon'] #список "наших" языков
import re
import requests

lang_lang = []

for i in set_of_languages: #проходим по списку
    link = 'http://www.rosettacode.org/wiki/Category:' + i 
    r = requests.get(link) #выгружаем html-код списка программ для каждого языка
    lang = re.search(r'<h2>Pages\sin\scategory(((.*)\n)*)<\/div><\/div><\/div><div class="printfooter">', r.text)
    languages = re.findall(r'<li><a\shref="\/wiki\/(.[^"]*)"', lang.group()) #создаем список программ для каждого языка
    lang_lang.append(languages) #делаем список списков программ
set_of_problems = set(lang_lang[0]).intersection(*lang_lang) #пересекаем списки, чтобы найти общие программы для всех языков
set_of_problems = sorted(list(set_of_problems))
with open('set.txt', 'w', encoding = 'utf-8') as the_set: #записываем этот список в файл
    for problem in set_of_problems:
        the_set.write(problem + '\n')
