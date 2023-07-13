import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    collector = BooksCollector()
    return collector
@pytest.fixture()
def add_books_rating(collector):
    books_name_list = ['book1', 'book2', 'book3', 'book4', 'book5']
    books_rating_list = [6, 2, 8, 8, 10]
    for i in books_name_list:
        collector.add_new_book(i)
    for i in range(0, 5):
        collector.set_book_rating(books_name_list[i], books_rating_list[i])
    result = collector.books_rating
    return result

@pytest.fixture()
def add_favorites_books(collector):
    books_name_list = ['book1', 'book2', 'book3', 'book4', 'book5']
    books_rating_list = [6, 2, 8, 8, 10]
    for i in books_name_list:
        collector.add_new_book(i)

    for i in range(0, 5):
        collector.set_book_rating(books_name_list[i], books_rating_list[i])

    for i in books_name_list:
        collector.add_book_in_favorites(i)

@pytest.fixture()
def add_book_with_rating(collector):
    collector.add_new_book('book1')
    collector.set_book_rating('book1', 7)

@pytest.fixture()
def add_book_with_rating_in_favorite(collector):
    collector.add_new_book('book1')
    collector.set_book_rating('book1', 10)
    collector.add_book_in_favorites('book1')