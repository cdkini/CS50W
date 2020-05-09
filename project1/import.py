
import csv
import os

from application import engine, db
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import scoped_session, sessionmaker


def create_books_table():
    try:
        db.execute("CREATE TABLE books ( "
                        "id SERIAL PRIMARY KEY, "
                        "isbn VARCHAR NOT NULL, "
                        "title VARCHAR NOT NULL, "
                        "author VARCHAR NOT NULL, "
                        "year INTEGER NOT NULL );"
        )
        db.commit()
    except ProgrammingError:
        print("books table already created.")
    

def books_csv_to_db():
    with open("books.csv") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            isbn, title, author, year = row
            db.execute("INSERT INTO books (id, isbn, title, author, year) VALUES (:id, :isbn, :title, :author, :year)",
                {"id": i,
                 "isbn": isbn, 
                 "title": title,
                 "author": author,
                 "year": year})
        print("books table successfully populated with CSV data.")
        db.commit()


def main():
    create_books_table()
    books_csv_to_db()
    

if __name__ == "__main__":
    main()