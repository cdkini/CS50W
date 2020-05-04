# program that will take the books and import them into your PostgreSQL database
# users/books/reviews

import csv
import os

from sqlalchemy import create_engine

with open("books.csv") as f:
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        pass
