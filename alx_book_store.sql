CREATE IF NOT EXISTS DATABASE alx_book_store;

CREATE TABLE Books (
    books_id INT NOT NULL PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE 
);

CREATE TABLE Authors (
    author_id INT NOT NULL PRIMARY KEY,
    author_name VARCHAR(215),
)

ALTER TABLE Books;
ADD FOREIGN KEY (author_id) REFERENCES Authors(author_id);
