# qa_python

# BooksCollector — тесты

Юнит-тесты для класса `BooksCollector` (pytest).

## Запуск

```
pytest -v
```

## Список тестов

| Тест | Метод | Что проверяет |
|---|---|---|
| `test_add_new_book_add_two_books` | `add_new_book` | Добавление двух книг — обе попадают в словарь |
| `test_add_new_book_length_limit` | `add_new_book` | Книга с названием > 40 символов не добавляется, книга с названием = 40 символов добавляется |
| `test_set_book_genre_valid_genre` (параметризованный, 5 сценариев) | `set_book_genre` | Установка каждого из допустимых жанров книге |
| `test_get_book_genre_missing_book_returns_none` | `get_book_genre` | Для книги, которой нет в словаре, возвращается None |
| `test_get_books_with_specific_genre_returns_matches` | `get_books_with_specific_genre` | Из книг разных жанров возвращаются только книги запрошенного жанра |
| `test_get_books_genre_returns_full_dict` | `get_books_genre` | Возвращается весь словарь книг с жанрами |
| `test_get_books_for_children_excludes_age_rated_genre` | `get_books_for_children` | Книга жанра с возрастным рейтингом не попадает в список для детей |
| `test_get_books_for_children_includes_no_rating_genre` | `get_books_for_children` | Книга жанра без возрастного рейтинга попадает в список для детей |
| `test_add_book_in_favorites_adds_book` | `add_book_in_favorites` | Книга из словаря добавляется в избранное |
| `test_delete_book_from_favorites_removes_book` | `delete_book_from_favorites` | Книга удаляется из избранного |
| `test_get_list_of_favorites_books_returns_all` | `get_list_of_favorites_books` | Возвращается список всех книг в избранном |

Итого: 11 тестовых функций (с учётом параметризации — 15 запусков), покрыт каждый из 9 методов класса `BooksCollector`. Используется параметризация (`test_set_book_genre_valid_genre`).