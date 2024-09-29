-- Inner Join query
SELECT books.title, authors.first, authors.last
from books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Left Join query
SELECT books.title, authors.first, authors.last
FROM books
LEFT JOIN authors ON books.author_id = authors.author_id;