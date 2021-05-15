import re
import enchant
d = enchant.Dict("en_US")
set_of_languages = ['BASIC', 'C sharp', 'C', 'C++', 'Java', 'Python', 'Fortran', 'Pascal', 'Unicon']

for language in set_of_languages:
    with open(language + '.txt', 'r', encoding='utf-8') as f:
        with open(language + '_new.txt', 'w', encoding='utf-8') as f_new:
            for line in f:
                if not line.startswith('==='):
                    if not line.startswith('{{'):
                        if not line.startswith("''"):
                            if not line.startswith('[['):
                                if not line.startswith("'"):
                                    if re.match(r'^\s*\/?\*.*\n', line) is None:
                                        line = re.sub(r'&lt;(\/)?lan.+?;', '', line)
                                        line = re.sub(r'\/\/.*', '', line)
                                        line = re.sub(r'\/\*.*\*\/', '', line)
                                        line = re.sub(r'#.+\n', '', line)
                                        line = re.sub(r'&lt;.+&gt;', '', line)
                                        line = re.sub(r'!.+\n', '', line)
                                        line = re.sub(r'&quot;', '', line)
                                        line = re.sub(r'&gt;', '', line)
                                        line = re.sub(r'&lt;', '', line)
                                        line = re.sub(r'&amp;', '', line)
                                        line = re.sub(r'^[\'\[\]A-Za-z\s_&;0-9]+?:.+\n', '', line)
                                        line = re.sub(r'.*(\..*?)\(', r'\(', line) #убираем части кода: variable.function(...) -> variable(...)
                                        new_line = line.split( ) #токенизация
                                        q_words = 0
                                        for word in new_line:
                                            word = word.strip('.,:;()') #чистка "слова"
                                            if word:
                                                if d.check(word): #проверка, существует ли данное слово в английском языке
                                                    if word != 'int' and word != 'for' and word != 'if' and word != 'else' and word != 'string': 
                                                        q_words += 1
                                        if q_words < 10: #если строка состоит из 10+ "настоящих" слов, то в итоговый файл она не записывается, чтобы почистить комментарии автора кода
                                            f_new.write(line)           
