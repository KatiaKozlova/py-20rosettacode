# rosetta code. корпусный анализ параллельных программ

***цель*** проекта - обнаружить закономерность в том, *какой язык программирования использует человек* и *какие названия для переменных он выбирает*, или же показать, что никакой значимой корреляции не существует.

### источники
1. [**rosetta code**](http://www.rosettacode.org) - англоязычный сайт, собравший самые известные, популярные или просто интересные задачи программирования, для которых пользователи пишут решения и алгоритмы, используя разные языки программирования;
2.  **документация** языков для *выделение ключевых слов и типов переменных* ([basic](https://docs.microsoft.com/ru-ru/dotnet/visual-basic/language-reference/keywords/), [c](https://en.cppreference.com/w/c/keyword), [c#](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/keywords/), [c++](https://docs.microsoft.com/ru-ru/cpp/cpp/keywords-cpp?view=msvc-160), [fortran](http://fortranwiki.org/fortran/show/Keywords), [icon/unicon](https://www2.cs.arizona.edu/icon/refernce/ref.htm), [java](https://docs.oracle.com/en/java/javase/15/docs/specs/sealed-classes-jls.html#jls-3.9), [pascal](https://www.freepascal.org/docs-html/ref/refse3.html#x11-100001.3), [python](https://docs.python.org/3/reference/lexical_analysis.html#keywords))
3. **библиотеки и модули**:
    * [requests](https://pypi.org/project/requests/) - для *скачивания данных* с сайта
    * [enchant](https://pypi.org/project/pyenchant/) - для *определения, является ли слово существующим* в английском языке
    * [re](https://docs.python.org/3/library/re.html) - для *чистки htlm и списков*
    * [collections](https://docs.python.org/3/library/collections.html) - для составления *частотного списка токенов*
    * [csv](https://docs.python.org/3/library/csv.html) - для *выгрузки в табличном формате*
---
### параметры 
для **переменных**:
1. средняя *длина*;
2. *dash-и*;
3. *заглавные* буквы;
4. *морфологический* анализ (существуют ли в английском)

для **языков**:
1. *близость* (на каком языке основываются, чьим диалектом являются);
2. *цели* использования;
3. *доля переменных* в коде

### задачи
:heavy_check_mark: **(минимум)** собрать данные для **9 языков программирования** и обработать:
|name|[usage](http://www.rosettacode.org/wiki/Language_Comparison_Table)|influenced by<sup>1</sup>|influenced<sup>1</sup>|
|:-------------|:---------------:|:-------------:|:-------------:|
|**basic**|education|fortran|-|
|**c**|system, embedded|fortran|c#, c++, java, python|
|**c#**|application|c, c++, icon, java|java|
|**c++**|application, system|c|c#, java, python|
|**fortran**|scientific and numeric applications|-|basic, c|
|**icon/unicon**|text, data|-|c#, python|
|**java**|application|c, c#, c++, pascal|c#, python|
|**pascal**|application, education, system|-|java|
|**python**|application, education, scripting|c, c++, icon, java|-|

<sup>1</sup>данные взяты из [en.wikipedia.org](en.wikipedia.org)

:question: **(максимум)** обобщить программы, чтобы они работали для любого набора языков:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:heavy_check_mark: находить *общие программы для любого сета языков*;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:heavy_check_mark: *выкачивать все программы из списка* общих для любого языка;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:heavy_check_mark: *дешево чистить и парсить*;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:heavy_check_mark: автоматически *подсчитывать значение параметров* для списка переменных;<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:x: хорошая чистка предполагает *знание особенностей оформления языка*;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:x: для выделения переменных требуется *чтение документации*;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:x: дополнение списка ключевых слов *вручную*;<br/>

### описание каждой из программ
* [project1](https://github.com/KatiaKozlova/py-20rosettacode/blob/main/project1.py) - выделение общего сета проблем для данного языка
* [project2](https://github.com/KatiaKozlova/py-20rosettacode/blob/main/project2.py) - выгрузка кода для всех программ из сета (по-отдельности для каждого из языков)
* [project3](https://github.com/KatiaKozlova/py-20rosettacode/blob/main/project3.py) - чистка кода
* [project4](https://github.com/KatiaKozlova/py-20rosettacode/blob/main/project4.py) - парсинг, выделение токенов -> переменных, статистическая обработка, выгрузка

### результаты
<img align="left" src="/%D0%A1%D1%80%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F%20%D0%B4%D0%BB%D0%B8%D0%BD%D0%B0.png" alt="Средняя длина" width="400"/>

:exclamation: в _python_ ключевые слова сильно короче переменных, что говорит о том, что он:<br/>
&nbsp;&nbsp;1. _прикладной_ (чем короче "служебные слова", тем удобнее);<br/>
&nbsp;&nbsp;2. _используется для обучения_, самый популярный язык (переменные длинные);<br/>
:exclamation: _fortran_ первый язык программирования высокого уровня, получивший практическое применение, он **сбалансирован по длине токенов и переменных**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; возможно, после него языки стремились к развитию в разных сферах, поэтому так сильно разнятся средние<br/>
<br/>
<img align="left" src="/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D0%BD%D0%B0%D1%81%D1%82%D0%BE%D1%8F%D1%89%D0%B8%D1%85%20%D1%81%D0%BB%D0%BE%D0%B2%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%BE%D0%B2.png" alt="Количество настоящих слов на количество токенов" width="400"/>

:arrow_up: **больше всего** "настоящих" слов в *icon/unicon*, который используется _для обработки текста_;<br/>
:arrow_up: также их **много** в *python*;<br/>
:arrow_down: **cамое малое** количество "настоящих" слов в *c*, возможно, из-за того, что он _системный и встренный_ язык;<br/>
:arrow_down: также _системным_ является *pascal*, где их тоже **мало**<br/>
<br/><br/><br/><br/><br/>
<img align="left" src="/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%BE%D0%B2.png" alt="Количество переменных слов на количество токенов" width="400"/>

:arrow_up: **больше всего** переменных на токен в _basic_, но, скорее всего просто _выброс_;<br/>
:arrow_up: **больше среднего** только у _basic_ и _c_, все остальные примерно **на одном уровне**<br/>
<br/><br/><br/><br/><br/><br/><br/>
<img align="left" src="/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B8%D1%85%20%D0%B1%D1%83%D0%BA%D0%B2%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%BE%D0%B2.png" alt="Количество больших букв на количество токенов" width="400"/>

:arrow_up: употребление больших букв в _basic, pascal, fortran_ **больше среднего**, так как они _не чувствительны к регистру_;<br/>
:arrow_up: в _basic_ их **больше всего**, так как в нем названия типов переменных и другие "служебные слова" пишутся также с большой буквы (возможно, _выброс_);<br/>
:arrow_down: **меньше всего** заглавных букв _python_ и _icon/unicon_<br/>
<br/><br/><br/><br/><br/>
<img align="left" src="/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20dash-%D0%B5%D0%B9%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE%20%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%BE%D0%B2.png" alt="Количество dash-ей на количество токенов" width="400"/>

:arrow_up: в _c++_ и _c_ **больше всего** dash-ей;<br/>
:arrow_down: в _c#_ же их **мало** (возможно, из-за того, что он _более прикладной_);<br/>
:arrow_down: такжже **мало** в _fortran_, который повлиял на c#<br/>
<br/>
:exclamation: в среднем, **чем больше dash-ей, тем меньше больших букв** и наоборот<br/>
:exclamation: в группе _c++, c, c#_:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _c#_ отличается по числу **dash-ей и больших букв**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _c_ отличается по **средним длинам**<br/>
<br/>
### над проектом  работали
ваня широков и катя козлова, бкл-202
