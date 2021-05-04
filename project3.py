import re
import enchant
import string
d = enchant.Dict("en_US")
set_of_languages = ['BASIC', 'C sharp', 'C', 'C++', 'Java', 'Python', 'Fortran', 'Pascal', 'Unicon']

for language in set_of_languages:
    with open(language + '.txt', 'r', encoding = 'utf-8') as java:
        with open(language + '_new.txt', 'w', encoding = 'utf-8') as java_new:
            for line in java:
                if not line.startswith('==='):
                    if not line.startswith('{{'):
                        if not line.startswith("''"):
                            if not line.startswith('[['):
                                if not line.startswith('&lt'):
                                    if re.match(r'^\s*\/?\*.*\n', line) == None:
                                        line = re.sub(r'&lt;(\/)?lan.+?;', '', line)
                                        line = re.sub(r'\/\/.*', '', line)
                                        line = re.sub(r'\/\*.*\*\/', '', line)
                                        line = re.sub(r'^[\'\[\]A-Za-z\s_&;0-9]+?:.+\n', '', line)
                                        new_line = line.split( )
                                        q_words = 0
                                        for word in new_line:
                                            word = word.strip('.,:;()')
                                            if word:
                                                if d.check(word):
                                                    if word != 'int' and word != 'for' and word != 'if':
                                                        q_words += 1
                                        if q_words < 10:
                                            java_new.write(line)                    
