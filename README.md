## Инструкция для изменения успеваемости ученика

- Пропишите в терминале команду `python3 manage.py shell`
Запустится Django shell, о чём сообщит надпись:
```
(InteractiveConsole)
```

- Перейдите в файл `scripts.py`.

- Скопируйте функцию `fix_marks`, `remove_chastisements` или `create_commendation`.

- Вставьте функции и нажмите Enter для запуска.

### Значения функций

1. `fix_marks`- исправляет все плохие оценки на 5.
2. `remove_chastisements`- удаляет все замечания, написанные учителями.
3. `create_commendation`- выберает случайным образом предмет и напишет похвалу ученику. 
