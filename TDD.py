"""
bookstore
"""

import random
import unittest


class MyTestCase(unittest.TestCase):
    """verification tests"""

    def test_1(self):
        self.assertEqual(order(['Book0'], store), 0)

    def test_2(self):
        self.assertEqual(order(['Book3'], store), 3)

    def test_3(self):
        self.assertEqual(order(['Book6'], store), 6)

    def test_discount_5(self):
        self.assertEqual(order(['Book8', 'Book12'], store), 19)

    def test_discount_10(self):
        self.assertEqual(order(['Book9', 'Book11', 'Book10', 'Book17', 'Book13',], store), 54)


class Book:
    """book"""

    def __init__(self, title, price, genre):
        self.title = title
        self.price = price
        self.genre = genre


def buy_book(book_l, name):
    """returns the price of the purchased book"""
    price_book = -1
    for i in range(len(book_l)):
        if name == book_l[i].title:
            price_book = book_l[i].price
            book_l.pop(i)
            break
    return price_book


def order(shopping_list, book_l):
    """returns the amount of books purchased"""
    purchase_price = 0
    for i in shopping_list:
        price = buy_book(book_l, i)
        if price >= 0:
            purchase_price = purchase_price + price
    if (len(shopping_list) >= 5):
        return 0.9 * purchase_price
    if (5 > len(shopping_list) >= 2):
        return 0.95 * purchase_price
    else:
        return purchase_price


def create_store():
    """returns the amount of books purchased"""
    book_list = []
    for i in range(50):
        title_book = "Book" + str(i)
        price_book = i
        genre_book = random.choice(['novel', 'poems', 'drama'])
        book_list.append(Book(title_book, price_book, genre_book))
    return book_list + book_list + book_list + book_list


if __name__ == "__main__":
    store = create_store()
    unittest.main()
