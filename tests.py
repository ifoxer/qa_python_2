from main import BooksCollector
import pytest
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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_rating_1(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    @pytest.mark.parametrize('book_name, rating', [['book1', 1],
                                                   ['book2', 10]])
    def test_set_book_rating_boundary_in_range_values(self, book_name, rating):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)
        assert collector.books_rating[book_name] == collector.get_book_rating(book_name)

    @pytest.mark.parametrize('book_name, rating', [['book1', -1],
                                                   ['book2', 0],
                                                   ['book3', 11]])
    def test_set_book_rating_boundary_out_of_range_values(self, book_name, rating):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)
        assert collector.books_rating[book_name] == 1

    def test_get_book_rating_get_rating_one_book(self, collector, add_book_with_rating):
        assert collector.get_book_rating('book1') == 7

    def test_get_book_rating_rating_nonexistent_book(self, collector):
        assert collector.get_book_rating('nonexistent_book') is None

    def test_get_books_with_specific_rating_in_range(self, collector, add_books_rating):
        assert len(collector.get_books_with_specific_rating(8)) == 2

    def test_get_books_with_specific_rating_out_of_range(self, collector, add_books_rating):
        assert len(collector.get_books_with_specific_rating(12)) == 0

    def test_get_books_rating_list_of_5_books(self, collector, add_books_rating):
        assert len(collector.get_books_rating()) == 5

    def test_add_book_in_favorites_add_one_book_in_favorites_list(self, collector, add_book_with_rating_in_favorite):
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_add_book_from_favorites_list(self, collector, add_book_with_rating_in_favorite):
        collector.add_book_in_favorites('book1')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self, collector, add_book_with_rating_in_favorite):
        collector.delete_book_from_favorites('book1')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_delete_book_is_not_from_list(self, collector, add_book_with_rating_in_favorite):
        collector.delete_book_from_favorites('book2')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books(self, collector, add_favorites_books):
        assert len(collector.get_list_of_favorites_books()) == 5
