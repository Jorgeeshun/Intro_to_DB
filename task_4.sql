USE alx_book_store;

-- Query to list all columns and their data types in the Books table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books';
