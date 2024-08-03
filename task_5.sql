USE alx_book_store;

RENAME TABLE CuStomers TO customer;

DELETE FROM customer
WHERE customer_id = 1;


INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

SELECT * FROM customer;