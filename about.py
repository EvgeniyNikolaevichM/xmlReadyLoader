about = ("""1.Подготовить diffmodel xml к загрузке на CIM-портал, экспортированный по профилю для организаций.
Данный раздел выполняет следующее:
- Удаляет header;
- Вставляет header diffmodel для загрузки на CIM-портал;
- Удаляет me:className="..." у rdf:Description;
- Обновляет тег <dm:reverseDifferences>.

2.Преобразовать fullmodel xml в diffmodel для загрузки на CIM-портал.
Данный раздел выполняет следующее:
- Добавляет необходимые отступы;
- Удаляет header и footer fullmodel;
- Добавляет header и footer diffmodel.

3.Задать параметры преобразования вручную.
Данный раздел выполняет слудующее:
- Удаление строк по умолчанию ('<me:', '>');
- Удаление me:className="..." у rdf:Description;
- Позволяет задать свои строки для удаления (начальный и конечный символ строки);
- Позволяет задать строку для добавления по индексу;
- Позволяет менять строку на новую строку по точному совпадению.
""")
