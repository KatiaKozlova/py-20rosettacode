set_of_languages = ['BASIC', 'C_sharp', 'C', 'C%2B%2B', 'Java', 'Python', 'Fortran', 'Pascal', 'Unicon']
import re
import requests

lang_lang = []

for i in set_of_languages:
    link = 'http://www.rosettacode.org/wiki/Category:' + i
    #print(link)
    r = requests.get(link)
    lang = re.search(r'<h2>Pages\sin\scategory(((.*)\n)*)<\/div><\/div><\/div><div class="printfooter">', r.text)
    languages = re.findall(r'<li><a\shref="\/wiki\/(.[^"]*)"', lang.group())
    lang_lang.append(languages)
set_of_problems = set(lang_lang[0]).intersection(*lang_lang)
set_of_problems = sorted(list(set_of_problems))
#print(set_of_problems)
with open('set.txt', 'w', encoding = 'utf-8') as the_set:
    for problem in set_of_problems:
        the_set.write(problem + '\n')
