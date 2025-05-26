## Инструкция для изменения успеваемости ученика

- Добавьте файл `scripts.py`.

- Пропишите в терминале команду `python3 manage.py shell`
Запустится Django shell, о чём сообщит надпись:
```
(InteractiveConsole)
```

- Перейдите в файл `scripts.py`.

- Скопируйте функцию `fix_marks`, `remove_chastisements` или `create_commendation`.

- Вставьте функции и нажмите Enter для запуска.

#### Пример запуска скрипта

1. В консоли с Django shell, пропишите данную команду, чтобы импортировать все функции.
```
from scripts import (fix_marks, remove_chastisements, create_commendation)
```
2. Вызовите нужную фам функцию, если все работает, пример вывода будет таким:
```
fix_marks
<function fix_marks at 0x000001A7949AF880>
```

### Значения функций

1. `fix_marks`- исправляет все плохие оценки на 5.
2. `remove_chastisements`- удаляет все замечания, написанные учителями.
3. `create_commendation`- выберает случайным образом предмет и напишет похвалу ученику. 

