import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize('name', ['a', 'a' * 40])
    def test_add_new_book_valid_length_adds_book(self, name):
        collector = BooksCollector()

        # добавляем книгу с валидной длиной названия: 1 символ и граничное значение 40 символов
        collector.add_new_book(name)

        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'a' * 41])
    def test_add_new_book_invalid_length_not_added(self, name):
        collector = BooksCollector()

        # добавляем книгу с невалидной длиной названия: пустая строка и 41 символ (за границей)
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()

        # добавляем книгу и по очереди устанавливаем ей каждый жанр из списка допустимых
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', genre)

        assert collector.get_book_genre('Понедельник начинается в субботу') == genre

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()

        # добавляем книгу, устанавливаем жанр, проверяем, что метод возвращает именно его
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', 'Фантастика')

        assert collector.get_book_genre('Понедельник начинается в субботу') == 'Фантастика'

    def test_get_book_genre_missing_book_returns_none(self):
        collector = BooksCollector()

        # запрашиваем жанр книги, нет в словаре
        assert collector.get_book_genre('Нет такой книги') is None

    def test_get_books_with_specific_genre_returns_matches(self):
        collector = BooksCollector()

        # добавляем книги разных жанров, ищем только один жанр
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', 'Фантастика')
        collector.add_new_book('Ужас Данвича')
        collector.set_book_genre('Ужас Данвича', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Понедельник начинается в субботу']

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()

        # добавляем книгу с жанром, получаем весь словарь
        collector.add_new_book('Понедельник начинается в субботу')
        collector.set_book_genre('Понедельник начинается в субботу', 'Фантастика')

        assert collector.get_books_genre() == {'Понедельник начинается в субботу': 'Фантастика'}

    def test_get_books_for_children_excludes_age_rated_genre(self):
        collector = BooksCollector()

        # добавляем книгу, возрастной рейтинг
        collector.add_new_book('Ужас Данвича')
        collector.set_book_genre('Ужас Данвича', 'Ужасы')

        assert 'Ужас Данвича' not in collector.get_books_for_children()

    def test_get_books_for_children_includes_no_rating_genre(self):
        collector = BooksCollector()

        # добавляем книгу без возрастного рейтинга
        collector.add_new_book('Пластилиновая ворона')
        collector.set_book_genre('Пластилиновая ворона', 'Мультфильмы')

        assert 'Пластилиновая ворона' in collector.get_books_for_children()

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

        # добавляем книгу в словарь, в избранное
        collector.add_new_book('Понедельник начинается в субботу')
        collector.add_book_in_favorites('Понедельник начинается в субботу')

        assert collector.get_list_of_favorites_books() == ['Понедельник начинается в субботу']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

        # добавляем книгу в избранное, удаляем её
        collector.add_new_book('Понедельник начинается в субботу')
        collector.add_book_in_favorites('Понедельник начинается в субботу')
        collector.delete_book_from_favorites('Понедельник начинается в субботу')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_all(self):
        collector = BooksCollector()

        # добавляем две книги в избранное
        collector.add_new_book('Понедельник начинается в субботу')
        collector.add_new_book('Ужас Данвича')
        collector.add_book_in_favorites('Понедельник начинается в субботу')
        collector.add_book_in_favorites('Ужас Данвича')

        assert collector.get_list_of_favorites_books() == ['Понедельник начинается в субботу', 'Ужас Данвича']

        