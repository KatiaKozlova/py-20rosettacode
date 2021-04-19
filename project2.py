import requests
import re

flag = 0
the_language = ''
set_of_languages = ['BASIC', 'C sharp', 'C sharp|C#' , 'C', 'C++', 'Java', 'Python', 'Fortran', 'Pascal', 'Icon}} and {{header|Unicon']

with open('set.txt', 'r', encoding = 'utf-8') as the_set:
    for problem in the_set:
        problem = problem.strip()
        new_link = 'http://www.rosettacode.org/wiki/Special:Export/' + problem
        #print(new_link)
        r_new = requests.get(new_link)
        r = re.findall(r'=={{header\|(BASIC|C\ssharp|C\ssharp\|C#|C|C\+\+|Java|Python|Fortran|Pascal|Icon}}\sand\s{{header\|Unicon)}}==([^ё]+?)([Oo]utput|=={{header)', r_new.text)
        for i in r:
            if i[0] == 'C sharp|C#':
                with open('C sharp.txt', 'a', encoding = 'utf-8') as file:
                    file.write(problem + ':\n' + i[1] + '\n')
            elif i[0] == 'Icon}} and {{header|Unicon':
                with open('Unicon.txt', 'a', encoding = 'utf-8') as file:
                    file.write(problem + ':\n' + i[1] + '\n')
            else:
                with open(i[0] + '.txt', 'a', encoding = 'utf-8') as file:
                    file.write(problem + ':\n' + i[1] + '\n')
