# rosetta code. корпусный анализ параллельных программ

***цель*** проекта - обнаружить закономерность в том, *какой язык программирования использует человек* и *какие названия для переменных он выбирает*, или же показать, что никакой значимой корреляции не существует.

### источники
1. [**rosetta code**](http://www.rosettacode.org) - англоязычный сайт, собравший самые известные, популярные или просто интересные задачи программирования, для которых пользователи пишут решения и алгоритмы, используя разные языки программирования;
2.  **документация** языков для *выделение ключевых слов и типов переменных* ([basic](https://docs.microsoft.com/ru-ru/dotnet/visual-basic/language-reference/keywords/), [c](https://en.cppreference.com/w/c/keyword), [c#](https://docs.microsoft.com/ru-ru/dotnet/csharp/language-reference/keywords/), [c++](https://docs.microsoft.com/ru-ru/cpp/cpp/keywords-cpp?view=msvc-160), [fortran](http://fortranwiki.org/fortran/show/Keywords), [icon/unicon](https://www2.cs.arizona.edu/icon/refernce/ref.htm), [java](https://docs.oracle.com/en/java/javase/15/docs/specs/sealed-classes-jls.html#jls-3.9), [pascal](https://www.freepascal.org/docs-html/ref/refse3.html#x11-100001.3), [python](https://docs.python.org/3/reference/lexical_analysis.html#keywords))
3. **библиотеки**:
    * [requests](https://pypi.org/project/requests/) - для *скачивания данных* с сайта
    * [enchant](https://pypi.org/project/pyenchant/) - для *определения, является ли слово существующим* в английском языке
    * [re](https://docs.python.org/3/library/re.html) - для *чистки htlm и списков*
---
### параметры 
для **переменных**:
1. средняя *длина*;
2. *dash-и* или другие *разделители*;
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
